# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:24:14 2022

@author: Osman
"""

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn

url2= 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

dfcase = pd.read_csv(url2)


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
dfv62=dfv6.mean(axis = 0, skipna = True)
dfv72=dfv7.mean(axis = 0, skipna = True)
dfv82=dfv8.mean(axis = 0, skipna = True)
dfv92=dfv9.mean(axis = 0, skipna = True)
dfv102=dfv10.mean(axis = 0, skipna = True)

