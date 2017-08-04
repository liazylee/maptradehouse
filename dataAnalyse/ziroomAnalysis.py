# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:16:17 2017

@author: zhanglu01
"""
import json
import pandas as pd
import matplotlib.pyplot as plot
import ziroomAnalysis.geohash as geohash

def line_json_load(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        df = pd.DataFrame()
        i = 0
        for line in lines:
            tmp_df = pd.DataFrame(json.loads(line), index=[i])
            tmp_df["price"] = tmp_df["price"].astype("int")
            tmp_df["area"] = tmp_df["area"].astype("float")
            tmp_df["lng"] = tmp_df["lng"].astype("float")
            tmp_df["lat"] = tmp_df["lat"].astype("float")
            if tmp_df.iloc[0]["time_unit"] == "每天":
                tmp_df.price[i] = tmp_df.price[i]*30
            
            df = df.append(tmp_df)
            i += 1
        return df

filename = 'F:/PyWorkspace/ziroomAnalysis/0729/ziroomBeijing.json'
df = line_json_load(filename)
df = df.drop_duplicates()
df = df[(df['time_unit']!='每天') & (df['direction']!='南北') & (df['floorLoc']!='') & (df['floorTotal']!='')]

#不同租赁方式的统计量
#df["price_per_m2"] = df["price"]/df["area"]
groups = df.groupby(df["rentType"])
rt_count = groups.size()
rt_mean = groups.mean().rename(columns={'price':'mean_price'})
rt_max = groups.max().rename(columns={'price':'max_price'})
rt_min = groups.min().rename(columns={'price':'min_price'})
rt_median = groups.median().rename(columns={'price':'median_price'})
rentTypeDf = pd.concat([rt_mean["mean_price"],pd.DataFrame(rt_count,columns=["count"]),rt_max["max_price"],rt_min["min_price"],rt_median["median_price"]],axis=1)

#df[df['price']==990]["link"]
############合租分析############
#每100元为区间段统计数量
he_intervals = {100*x:0 for x in range(64)}
for price in df[df['rentType']=='合']['price']:
    he_intervals[price//100*100] += 1
plot.bar(he_intervals.keys(), he_intervals.values(), width=100, alpha = .5, color = 'blue')
plot.xlabel(u"月租(元)", fontproperties='SimHei')
plot.ylabel(u"房间数量", fontproperties='SimHei')
plot.show()

#将经纬度转换成字符串编码，将同一个格子里的点合并，目的是减少热力图中的打点数量
geohash_dict = dict()
for house in df[df['rentType']=='合'].iterrows():
    geohash_code = geohash.encode(house[1]["lat"], house[1]["lng"], 6)
    if geohash_code in geohash_dict.keys():
        geohash_dict[geohash_code] += 1
    else:
        geohash_dict[geohash_code] = 1
#将he_position_str的值替换“房间数量热力图.html”中相应的值
he_position_str = ""
for code in geohash_dict:
    he_position_str += '{{"lng": {0}, "lat": {1}, "count": {2}}},\n'.format(geohash.decode_exactly(code)[1],geohash.decode_exactly(code)[0],geohash_dict[code])

#将he_position_price_str的值替换“价格在地图上的分布.html”中相应的值
he_position_price_str = ""
for house in df[df['rentType']=='合'].iterrows():
    if house[1]["price"]<2000:
        he_position_price_str += '{{"lng": {0}, "lat": {1}, "count": {2}}},\n'.format(house[1]["lng"],house[1]["lat"],5)
    elif house[1]["price"]<3000:
        he_position_price_str += '{{"lng": {0}, "lat": {1}, "count": {2}}},\n'.format(house[1]["lng"],house[1]["lat"],10)
    else:
        he_position_price_str += '{{"lng": {0}, "lat": {1}, "count": {2}}},\n'.format(house[1]["lng"],house[1]["lat"],15)




############################地理位置聚类############################
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#用来评估簇的个数是否合适，每个簇的样本点到这个簇的中心点的距离之和越小说明簇分的越好，选取临界点的簇个数
__clfInertia__ = []
for i in range(2,30,1):
    clf = KMeans(n_clusters=i)
    s = clf.fit(df[(df['rentType']=='合') & (df['price']>=3000)][["lng", "lat"]])
    __clfInertia__.append([i, clf.inertia_])
plt.plot([x[0] for x in __clfInertia__], [x[1] for x in __clfInertia__],'b*')
plt.plot([x[0] for x in __clfInertia__], [x[1] for x in __clfInertia__],'r')

#调用kmeans类
clf = KMeans(n_clusters=4)
s = clf.fit(df[(df['rentType']=='合') & (df['price']>=3000)][["lng", "lat"]])
print(s)

#n个中心
print(clf.cluster_centers_)
 




############################随机森林回归############################
from math import radians,sin,cos,degrees,atan2,atan,tan,acos
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
def getDegree(latA, lngA, latB, lngB):  
    """ 
    Args: 
        point p1(latA, lngA) 
        point p2(latB, lngB) 
    Returns: 
        bearing between the two GPS points, 
        default: the basis of heading direction is north 
    """  
    radLatA = radians(latA)  
    radLngA = radians(lngA)  
    radLatB = radians(latB)  
    radLngB = radians(lngB)  
    dLng = radLngB - radLngA  
    y = sin(dLng) * cos(radLatB)  
    x = cos(radLatA) * sin(radLatB) - sin(radLatA) * cos(radLatB) * cos(dLng)  
    brng = degrees(atan2(y, x))  
    brng = (brng + 360) % 360  
    return brng

def getDistance(latA, lngA, latB, lngB):  
    ra = 6378140  # radius of equator: meter  
    rb = 6356755  # radius of polar: meter  
    flatten = (ra - rb) / ra  # Partial rate of the earth  
    # change angle to radians  
    radLatA = radians(latA)  
    radLngA = radians(lngA)  
    radLatB = radians(latB)  
    radLngB = radians(lngB)  
  
    pA = atan(rb / ra * tan(radLatA))  
    pB = atan(rb / ra * tan(radLatB))  
    x = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(radLngA - radLngB))  
    c1 = (sin(x) - x) * (sin(pA) + sin(pB))**2 / cos(x / 2)**2  
    c2 = (sin(x) + x) * (sin(pA) - sin(pB))**2 / sin(x / 2)**2  
    dr = flatten / 8 * (c1 - c2)  
    distance = ra * (x + dr)  
    return distance

df['degree'] = df.apply(lambda row: getDegree(39.915129,116.403981,row.lat,row.lng), axis=1)
df['distance'] = df.apply(lambda row: getDistance(39.915129,116.403981,row.lat,row.lng), axis=1)
#df['distance1'] = df.apply(lambda row: getDistance(39.93573198,116.33882039,row.lat,row.lng), axis=1)
#df['distance2'] = df.apply(lambda row: getDistance(39.9934964,116.45926247,row.lat,row.lng), axis=1)
#df['distance3'] = df.apply(lambda row: getDistance(39.91515228,116.4790283,row.lat,row.lng), axis=1)
#df['distance4'] = df.apply(lambda row: getDistance(40.04388111,116.35319092,row.lat,row.lng), axis=1)
#df['distance5'] = df.apply(lambda row: getDistance(39.929654,116.403119,row.lat,row.lng), axis=1)
rf_data = df[(df.rentType=='合') & (df.time_unit!='每天') & (df.floorLoc!='') & (df.floorTotal!='')][['area','confGen','confType','direction','floorLoc','floorTotal','nearestSubWayDist','privateBalcony','privateBathroom','rooms','halls','district','degree','distance','link','price']]
rf_data = rf_data.reset_index(drop=True) #重置索引
confGenLe = LabelEncoder()
rf_data['confGen']=confGenLe.fit_transform(rf_data['confGen'])
list(confGenLe.classes_)
confTypeLe = LabelEncoder()
rf_data['confType']=confTypeLe.fit_transform(rf_data['confType'])
list(confTypeLe.classes_)
directionLe = LabelEncoder()
rf_data['direction']=directionLe.fit_transform(rf_data['direction'])
list(directionLe.classes_)
districtLe = LabelEncoder()
rf_data['district']=districtLe.fit_transform(rf_data['district'])
list(districtLe.classes_)
rf_data.nearestSubWayDist = rf_data.nearestSubWayDist.replace('','5000')

#one-hot encoding
def one_hot_encode(label_set,data):
    oneHotEnc = OneHotEncoder()
    oneHotEnc.fit(label_set)
    result=oneHotEnc.transform(data).toarray()
    return result

oneHotEncodes = one_hot_encode(
        [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[0,4,4,4],[0,5,5,5],[0,0,6,6],[0,0,7,7],[0,0,0,8],[0,0,0,9],[0,0,0,10],[0,0,0,11],[0,0,0,12]],
        rf_data[['confGen','confType','direction','district']])
#将二维list转dataframe
one_hot_columns = ["confGen0", "confGen1", "confGen2", "confGen3",
                 "confType0", "confType1", "confType2", "confType3", "confType4", "confType5",
                 "direction0", "direction1", "direction2", "direction3", "direction4", "direction5", "direction6", "direction7",
                 "district0", "district1", "district2", "district3", "district4", "district5", "district6", "district7", "district8", "district9", "district10", "district11", "district12"]
rf_data[one_hot_columns] = pd.DataFrame(oneHotEncodes,columns=one_hot_columns)
rf_data=rf_data.drop(['confGen','confType','direction','district'],axis=1)
tmp_link=rf_data[['link','price']]
rf_data=rf_data.drop(['link','price'],axis=1)
rf_data[['link','price']]=tmp_link
X_train, X_test, y_train, y_test = train_test_split(rf_data.iloc[:,0:42], rf_data.iloc[:,[42]], test_size=0.33, random_state=42)

#训练模型_start

#首先对n_estimators进行网格搜索  
param_test1= {'n_estimators':list(range(450,550,10))}
gsearch1= GridSearchCV(estimator = RandomForestRegressor(max_features="log2", min_samples_leaf=2, oob_score=True), param_grid =param_test1, scoring=None, cv=5)  
gsearch1.fit(X_train.iloc[:,0:18],y_train)  
gsearch1.grid_scores_,gsearch1.best_params_, gsearch1.best_score_  

#接着对决策树最大深度max_depth和内部节点再划分所需最小样本数min_samples_split进行网格搜索。  
param_test2= {'max_depth':list(range(80,100,2)), 'min_samples_split':list(range(2,101,2))}  
gsearch2= GridSearchCV(estimator = RandomForestRegressor(n_estimators=50, max_features="log2", min_samples_leaf=2, oob_score=True), param_grid = param_test2,scoring=None,iid=False, cv=5)  
gsearch2.fit(X_train.iloc[:,0:18],y_train)  
gsearch2.grid_scores_,gsearch2.best_params_, gsearch2.best_score_  

#再对内部节点再划分所需最小样本数min_samples_split和叶子节点最少样本数min_samples_leaf一起调参  
param_test3= {'min_samples_split':list(range(2,10,2)), 'min_samples_leaf':list(range(2,20,2))}  
gsearch3= GridSearchCV(estimator = RandomForestRegressor(n_estimators=50, max_features="log2",max_depth=96, oob_score=True), param_grid = param_test3,scoring=None,iid=False, cv=5)  
gsearch3.fit(X_train.iloc[:,0:18],y_train)  
gsearch3.grid_scores_,gsearch3.best_params_, gsearch3.best_score_  

#最后再对最大特征数max_features做调参:  
param_test4= {'max_features':list(range(2,17,1))}  
gsearch4= GridSearchCV(estimator = RandomForestRegressor(n_estimators=50,max_depth=96,min_samples_split=4,min_samples_leaf=2, oob_score=True), param_grid = param_test4,scoring=None,iid=False, cv=5)  
gsearch4.fit(X_train.iloc[:,0:18],y_train)  
gsearch4.grid_scores_,gsearch4.best_params_, gsearch4.best_score_  



rf_classifier = RandomForestRegressor(n_estimators=540,max_features=12,max_depth=96,min_samples_split=4,min_samples_leaf=2, oob_score=True)
rf_classifier.fit(X_train.iloc[:,0:41],y_train)

rf_classifier.oob_score_ #袋外分
pd.Series(rf_classifier.feature_importances_,index=X_train.columns[0:41]).sort_values(ascending=False) #特征重要性排序
#训练模型_end

#模型预测_start
results = rf_classifier.predict(X_test.iloc[:,0:41]).astype(int)
rf_classifier.score(X_test.iloc[:,0:41],y_test) #模型准确度
pddf = pd.DataFrame({'actual':y_test.price,'predict':results,'link':X_test.link,'size':X_test.area})
pddf['diff'] = abs(pddf.predict-pddf.actual)/pddf.actual
pddf_ordered = pddf.sort(columns='diff', ascending=False)
#模型预测_end


#############################灰色关联分析#############################
he_df = df[(df['rentType']=='合') & (df.time_unit!='每天') & (df.area>8) & (df.price<2200)] #过滤超出自己心理预期的数据
he_df['co_distance'] = he_df.apply(lambda row: getDistance(39.988122,116.319725,row.lat,row.lng), axis=1) #计算到公司的距离
#指标无量纲化（离差标准化）
he_feature_max = he_df[['area','price','co_distance']].max()
he_feature_min = he_df[['area','price','co_distance']].min()
he_df['area_nondim'] = he_df.apply(lambda row: (row.area-he_feature_min.area)/(he_feature_max.area-he_feature_min.area), axis=1)
he_df['price_nondim'] = he_df.apply(lambda row: (row.price-he_feature_min.price)/(he_feature_max.price-he_feature_min.price), axis=1)
he_df['co_distance_nondim'] = he_df.apply(lambda row: (row.co_distance-he_feature_min.co_distance)/(he_feature_max.co_distance-he_feature_min.co_distance), axis=1)
#计算关联系数
opt_series = pd.Series([1,0,0], index=['area_nondim','price_nondim','co_distance_nondim']) #设定最优化序列
he_df['area_nondim_opt_diff'] = he_df.apply(lambda row: abs(row.area_nondim-opt_series.area_nondim), axis=1)
he_df['price_nondim_opt_diff'] = he_df.apply(lambda row: abs(row.price_nondim-opt_series.price_nondim), axis=1)
he_df['co_distance_nondim_opt_diff'] = he_df.apply(lambda row: abs(row.co_distance_nondim-opt_series.co_distance_nondim), axis=1)
min_nondim_opt_diff = min(min(he_df['area_nondim_opt_diff']),min(he_df['price_nondim_opt_diff']),min(he_df['co_distance_nondim_opt_diff']))
max_nondim_opt_diff = max(max(he_df['area_nondim_opt_diff']),max(he_df['price_nondim_opt_diff']),max(he_df['co_distance_nondim_opt_diff']))
he_df['area_cor'] = he_df.apply(lambda row: (min_nondim_opt_diff+0.5*max_nondim_opt_diff)/(row.area_nondim_opt_diff+0.5*max_nondim_opt_diff), axis=1)
he_df['price_cor'] = he_df.apply(lambda row: (min_nondim_opt_diff+0.5*max_nondim_opt_diff)/(row.price_nondim_opt_diff+0.5*max_nondim_opt_diff), axis=1)
he_df['co_distance_cor'] = he_df.apply(lambda row: (min_nondim_opt_diff+0.5*max_nondim_opt_diff)/(row.co_distance_nondim_opt_diff+0.5*max_nondim_opt_diff), axis=1)
he_df['room_cor_order'] = he_df['area_cor']/6+he_df['price_cor']/3+he_df['co_distance_cor']/2
he_ordered_df = he_df.sort(columns='room_cor_order', ascending=False) #房间关联系数倒排