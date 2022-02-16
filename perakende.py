import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.cluster import KMeans


pd.options.mode.chained_assignment = None  # default='warn

url = 'https://drive.google.com/file/d/18gyHbx6rfogq3yQ-GR9COjcGgyYlCnBZ/view?usp=sharing'
url2020 = 'https://drive.google.com/uc?id=' + url.split('/')[-2]


df20 = pd.read_csv(url2020)
df20=df20.dropna(axis=1,how='all')

url2= 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

dfcase = pd.read_csv(url2)



dfadana = df20.iloc[:1000,:]
dfadana.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dfadana= dfadana.drop(columns=['country_region_code','country_region','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline'
                          ,'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','sub_region_2','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])
dfadana.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')
dfadana1= dfadana.iloc[90:180]
dfadana2= dfadana.iloc[181:271]
dfadana3=dfadana.iloc[272:362]
dfadana4= dfadana.iloc[363:453]
dfadana5=dfadana.iloc[454:544]
dfadana6=dfadana.iloc[545:635]
dfadana7=dfadana.iloc[636:726]
dfadana8= dfadana.iloc[727:817]
dfadana9= dfadana.iloc[818:908]
dfadana10= dfadana.iloc[909:1000]

dfadana12=dfadana1.mean(axis = 0, skipna = True)
dfadana22=dfadana1.mean(axis = 0, skipna = True)
dfadana32=dfadana1.mean(axis = 0, skipna = True)
dfadana42=dfadana1.mean(axis = 0, skipna = True)
dfadana52=dfadana1.mean(axis = 0, skipna = True)
dfadana62=dfadana1.mean(axis = 0, skipna = True)
dfadana72=dfadana1.mean(axis = 0, skipna = True)
dfadana82=dfadana1.mean(axis = 0, skipna = True)
dfadana92=dfadana1.mean(axis = 0, skipna = True)
dfadana102=dfadana1.mean(axis = 0, skipna = True)





dfist = df20.iloc[:72437,:]
dfistanbul = dfist.iloc[71437:,:]

dfistanbul.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dfistanbul= dfistanbul.drop(columns=['country_region_code','country_region','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','sub_region_2','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])
 
dfistanbul.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')
 
dfistanbul1 = dfistanbul.iloc[90:120]
dfistanbul2 = dfistanbul.iloc[121:221]
dfistanbul3 = dfistanbul.iloc[222:322]
dfistanbul4 = dfistanbul.iloc[323:433]
dfistanbul5 = dfistanbul.iloc[434:534]
dfistanbul6 = dfistanbul.iloc[535:635]
dfistanbul7 = dfistanbul.iloc[636:726]
dfistanbul8 = dfistanbul.iloc[727:817]
dfistanbul9 = dfistanbul.iloc[818:908]
dfistanbul10 = dfistanbul.iloc[909:1000]


dfistanbul12=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul22=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul32=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul42=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul52=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul62=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul72=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul82=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul92=dfistanbul1.mean(axis = 0, skipna = True)
dfistanbul102=dfistanbul1.mean(axis = 0, skipna = True)




dfizmir = df20[84645:85645]

dfizmir.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dfizmir= dfizmir.drop(columns=['country_region_code','sub_region_2','country_region','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])
dfizmir.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')



dfizmir1 = dfizmir.iloc[90:160]
dfizmir2=dfizmir.iloc[161:271]
dfizmir3=dfizmir.iloc[272:362]
dfizmir4 = dfizmir.iloc[363:453]
dfizmir5=dfizmir.iloc[454:544]
dfizmir6=dfizmir.iloc[545:635]
dfizmir7=dfizmir.iloc[636:726]
dfizmir8=dfizmir.iloc[727:817]
dfizmir9=dfizmir.iloc[818:908]
dfizmir10=dfizmir.iloc[909:1000]



dfizmir12=dfizmir1.mean(axis = 0, skipna = True)
dfizmir22=dfizmir2.mean(axis = 0, skipna = True)
dfizmir32=dfizmir3.mean(axis = 0, skipna = True)
dfizmir42=dfizmir4.mean(axis = 0, skipna = True)
dfizmir52=dfizmir5.mean(axis = 0, skipna = True)
dfizmir62=dfizmir5.mean(axis = 0, skipna = True)
dfizmir72=dfizmir5.mean(axis = 0, skipna = True)
dfizmir82=dfizmir5.mean(axis = 0, skipna = True)
dfizmir92=dfizmir5.mean(axis = 0, skipna = True)
dfizmir102=dfizmir5.mean(axis = 0, skipna = True)





dfkony = df20.iloc[:109819,:]
dfkonya = dfkony.iloc[108819:,:]
dfkonya.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dfkonya = dfkonya.drop(columns=['country_region_code','sub_region_2','country_region','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])

dfkonya.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')

dfkonya1 = dfkonya.iloc[90:165]
dfkonya2=dfkonya.iloc[166:271]
dfkonya3=dfkonya.iloc[272:362]
dfkonya4=dfkonya.iloc[363:453]
dfkonya5=dfkonya.iloc[454:544]
dfkonya6=dfkonya.iloc[545:635]
dfkonya7=dfkonya.iloc[636:726]
dfkonya8=dfkonya.iloc[727:817]
dfkonya9=dfkonya.iloc[818:908]
dfkonya10=dfkonya.iloc[909:1000]


dfkonya12=dfkonya1.mean(axis = 0, skipna = True)
dfkonya22=dfkonya2.mean(axis = 0, skipna = True)
dfkonya32=dfkonya3.mean(axis = 0, skipna = True)
dfkonya42=dfkonya4.mean(axis = 0, skipna = True)
dfkonya52=dfkonya5.mean(axis = 0, skipna = True)
dfkonya62=dfkonya5.mean(axis = 0, skipna = True)
dfkonya72=dfkonya5.mean(axis = 0, skipna = True)
dfkonya82=dfkonya5.mean(axis = 0, skipna = True)
dfkonya92=dfkonya5.mean(axis = 0, skipna = True)
dfkonya102=dfkonya5.mean(axis = 0, skipna = True)



dfsamsun = df20.iloc[140427:141427]
dfsamsun.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dfsamsun= dfsamsun.drop(columns=['country_region_code','sub_region_2','country_region','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])

dfsamsun.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')
dfsamsun1 = dfsamsun.iloc[90:180]
dfsamsun2=dfsamsun.iloc[181:271]
dfsamsun3=dfsamsun.iloc[272:362]
dfsamsun4=dfsamsun.iloc[363:453]
dfsamsun5=dfsamsun.iloc[454:544]
dfsamsun6=dfsamsun.iloc[545:635]
dfsamsun7=dfsamsun.iloc[636:726]
dfsamsun8=dfsamsun.iloc[727:817]
dfsamsun9=dfsamsun.iloc[818:908]
dfsamsun10=dfsamsun.iloc[909:1000]


dfsamsun12=dfsamsun1.mean(axis = 0, skipna = True)
dfsamsun22=dfsamsun2.mean(axis = 0, skipna = True)
dfsamsun32=dfsamsun3.mean(axis = 0, skipna = True)
dfsamsun42=dfsamsun4.mean(axis = 0, skipna = True)
dfsamsun52=dfsamsun5.mean(axis = 0, skipna = True)
dfsamsun62=dfsamsun5.mean(axis = 0, skipna = True)
dfsamsun72=dfsamsun5.mean(axis = 0, skipna = True)
dfsamsun82=dfsamsun5.mean(axis = 0, skipna = True)
dfsamsun92=dfsamsun5.mean(axis = 0, skipna = True)
dfsamsun102=dfsamsun5.mean(axis = 0, skipna = True)



dferzurum =df20.iloc[57263:58263]
dferzurum.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dferzurum= dferzurum.drop(columns=['country_region_code','country_region','sub_region_2','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])
dferzurum.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')

dferzurum1 = dferzurum.iloc[90:160]
dferzurum2=dferzurum.iloc[161:231]
dferzurum3=dferzurum.iloc[232:332]
dferzurum4=dferzurum.iloc[333:423]
dferzurum5=dferzurum.iloc[424:524]
dferzurum6 = dferzurum.iloc[525:615]
dferzurum7 = dferzurum.iloc[616:706]
dferzurum8 = dferzurum.iloc[717:807]
dferzurum9 = dferzurum.iloc[808:908]
dferzurum10 = dferzurum.iloc[909:1000]



dferzurum12=dferzurum1.mean(axis = 0, skipna = True)
dferzurum22=dferzurum2.mean(axis = 0, skipna = True)
dferzurum32=dferzurum3.mean(axis = 0, skipna = True)
dferzurum42=dferzurum4.mean(axis = 0, skipna = True)
dferzurum52=dferzurum5.mean(axis = 0, skipna = True)
dferzurum62=dferzurum5.mean(axis = 0, skipna = True)
dferzurum72=dferzurum5.mean(axis = 0, skipna = True)
dferzurum82=dferzurum5.mean(axis = 0, skipna = True)
dferzurum92=dferzurum5.mean(axis = 0, skipna = True)
dferzurum102=dferzurum5.mean(axis = 0, skipna = True)







dfgaziantep=df20.iloc[59958:60958]
dfgaziantep.sort_values("retail_and_recreation_percent_change_from_baseline", ascending = True,
                 inplace = True, na_position ='last')
dfgaziantep=dfgaziantep.drop(columns=['country_region_code','sub_region_2','country_region','iso_3166_2_code','place_id','grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
              'transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline'])

dfgaziantep.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')
dfgaziantep1 = dfgaziantep.iloc[90:180]
dfgaziantep2=dfgaziantep.iloc[181:291]
dfgaziantep3=dfgaziantep.iloc[292:382]
dfgaziantep4=dfgaziantep.iloc[383:473]
dfgaziantep5=dfgaziantep.iloc[474:564]
dfgaziantep6=dfgaziantep.iloc[565:655]
dfgaziantep7=dfgaziantep.iloc[666:746]
dfgaziantep8=dfgaziantep.iloc[747:837]
dfgaziantep9=dfgaziantep.iloc[838:918]
dfgaziantep10=dfgaziantep.iloc[919:1000]



dfgaziantep12=dfgaziantep1.mean(axis = 0, skipna = True)
dfgaziantep22=dfgaziantep2.mean(axis = 0, skipna = True)
dfgaziantep32=dfgaziantep3.mean(axis = 0, skipna = True)
dfgaziantep42=dfgaziantep4.mean(axis = 0, skipna = True)
dfgaziantep52=dfgaziantep5.mean(axis = 0, skipna = True)
dfgaziantep62=dfgaziantep5.mean(axis = 0, skipna = True)
dfgaziantep72=dfgaziantep5.mean(axis = 0, skipna = True)
dfgaziantep82=dfgaziantep5.mean(axis = 0, skipna = True)
dfgaziantep92=dfgaziantep5.mean(axis = 0, skipna = True)
dfgaziantep102=dfgaziantep5.mean(axis = 0, skipna = True)




dfturkiyevaka = dfcase.iloc[140148:140808]
dfturkiyevaka.drop(dfturkiyevaka.iloc[:,10:66], inplace = True, axis = 1)

dfturkiyevaka.sort_values("date", ascending = True,
                 inplace = True, na_position ='last')
dfturkiyevaka2020 = dfturkiyevaka.iloc[0:295]
#dfturkiyevaka2021 = dfturkiyevaka.iloc[300:660]
dfturkiyevaka2020.drop(dfturkiyevaka.iloc[:,8:10], inplace = True, axis = 1)

dfturkiyevaka2020=dfturkiyevaka2020.drop(columns=['new_cases_smoothed','excess_mortality_cumulative_per_million','total_cases','total_deaths'])


dfv1 = dfturkiyevaka2020.iloc[0:20]
dfv2 = dfturkiyevaka2020.iloc[21:56]
dfv3 = dfturkiyevaka2020.iloc[57:92]
dfv4 = dfturkiyevaka2020.iloc[93:125]
dfv5= dfturkiyevaka2020.iloc[126:156]
dfv6= dfturkiyevaka2020.iloc[157:187]
dfv7= dfturkiyevaka2020.iloc[188:218]
dfv8= dfturkiyevaka2020.iloc[219:239]
dfv9= dfturkiyevaka2020.iloc[240:272]
dfv10= dfturkiyevaka2020.iloc[273:292]


dfv12=dfv1.mean(axis = 0, skipna = True)
dfv22=dfv2.mean(axis = 0, skipna = True)
dfv32 =dfv3.mean(axis = 0, skipna = True)
dfv42=dfv4.mean(axis = 0, skipna = True)
dfv52=dfv5.mean(axis = 0, skipna = True)
dfv52=dfv6.mean(axis = 0, skipna = True)
dfv52=dfv7.mean(axis = 0, skipna = True)
dfv52=dfv8.mean(axis = 0, skipna = True)
dfv52=dfv9.mean(axis = 0, skipna = True)
dfv52=dfv10.mean(axis = 0, skipna = True)


ilkay= dfadana12.append(dfistanbul12.append(dfizmir12.append(dfkonya12.append(dfsamsun12.append(dferzurum12.append(dfgaziantep12))))))
ikinciay=dfadana22.append(dfistanbul22.append(dfizmir22.append(dfkonya22.append(dfsamsun22.append(dferzurum22.append(dfgaziantep22))))))
ücüncüay=dfadana32.append(dfistanbul32.append(dfizmir32.append(dfkonya32.append(dfsamsun32.append(dferzurum32.append(dfgaziantep32))))))
dördüncüay=dfadana42.append(dfistanbul42.append(dfizmir42.append(dfkonya42.append(dfsamsun42.append(dferzurum42.append(dfgaziantep42))))))
besinciay=dfadana52.append(dfistanbul52.append(dfizmir52.append(dfkonya52.append(dfsamsun52.append(dferzurum52.append(dfgaziantep52))))))
altıncıay=dfadana62.append(dfistanbul62.append(dfizmir62.append(dfkonya62.append(dfsamsun62.append(dferzurum62.append(dfgaziantep62))))))
yedinciay=dfadana72.append(dfistanbul72.append(dfizmir72.append(dfkonya72.append(dfsamsun72.append(dferzurum72.append(dfgaziantep72))))))
sekizinciay=dfadana82.append(dfistanbul82.append(dfizmir82.append(dfkonya82.append(dfsamsun82.append(dferzurum82.append(dfgaziantep82))))))
dokuzuncuay=dfadana92.append(dfistanbul92.append(dfizmir92.append(dfkonya92.append(dfsamsun92.append(dferzurum92.append(dfgaziantep92))))))
sonay=dfadana102.append(dfistanbul102.append(dfizmir102.append(dfkonya102.append(dfsamsun102.append(dferzurum102.append(dfgaziantep102))))))


frame1 = { 'Mart': ilkay}
ilkay= pd.DataFrame(frame1)

ilkay2=ilkay.mean(axis = 0, skipna = True)

frame2 = { 'Nisan': ikinciay}
ikinciay= pd.DataFrame(frame2)
ikinciay2=ikinciay.mean(axis = 0, skipna = True)

frame3 = { 'Mayıs': ücüncüay}
ücüncüay= pd.DataFrame(frame3)
ücüncüay2=ücüncüay.mean(axis = 0, skipna = True)

frame4 = { 'Haziran': dördüncüay}
dördüncüay= pd.DataFrame(frame4)
dördüncüay2=dördüncüay.mean(axis = 0, skipna = True)

frame5 = { 'Temmuz': besinciay}
besinciay= pd.DataFrame(frame5)
besinciay2=besinciay.mean(axis = 0, skipna = True)

frame6 = { 'Ağustos': altıncıay}
altıncıay= pd.DataFrame(frame6)
altıncıay2=altıncıay.mean(axis = 0, skipna = True)

frame7 = { 'Eylül': yedinciay}
yedinciay= pd.DataFrame(frame7)
yedinciay2=yedinciay.mean(axis = 0, skipna = True)

frame8 = { 'Ekim': sekizinciay}
sekizinciay= pd.DataFrame(frame8)
sekizinciay2=sekizinciay.mean(axis = 0, skipna = True)

frame9 = { 'Kasım': dokuzuncuay}
dokuzuncuay= pd.DataFrame(frame9)
dokuzuncuay2=dokuzuncuay.mean(axis = 0, skipna = True)

frame10 = { 'Aralık': sonay}
sonay= pd.DataFrame(frame10)
sonay2=sonay.mean(axis = 0, skipna = True)




data = {'Mart':[-38.9538,-23.1451, -10.0442,541.35 ],'Nisan':[-55.1591,-36.0649 , -18.8975 ,3313.14] ,'Mayıs':[-49.7867,-25.1772,-10.0347, 1179.77] ,'Haziran':[-25.911,13.2504 ,6.65749,1249.31 ]
        ,'Temmuz' :[-16.201,29.5799,8.06773,1021.95] ,'Ağustos':[-16.201,30.432,8.06773,1476.7 ] ,'Eylül':[-15.301,-28.343,6.01535,1585.73]
        ,'Ekim' : [-13.201, 13.2123 ,11.232   ,2118.3 ], 'Kasım':[-16.201,23.565 ,9.134,1223.81],'Aralık':[  -13.301   ,5.2343   ,8.0723  ,1699.95]  
        }  
 

df = pd.DataFrame(data, index =['Perakende', 'Park', 'Market', 'Vaka'    ])



















