# -*- coding: utf-8 -*-
"""
Created on Mon Jan  29 11:11:41 2019

@author: aj-nok

about: PYTHON code for importing CSV file and applying mean, groupby, order by 

dataset:realestatetransactions.csv
"""

#CODE:

import pandas as pd
data=pd.read_csv("realestatetransactions.csv",index_col=0)
#df = pd.DataFrame(data['city'])
print("mean of price: ")
print(data['price'].mean())
print("mean of beds: ")
print(data['beds'].mean())
print("mean of baths: ")
print(data['baths'].mean())
print("mean of sq__ft: ")
print(data['sq__ft'].mean())
print("group by: ")
print(data.groupby('city').price.min())
print("order by: ")
print(data.sort_values(['zip', 'city'], ascending=[1, 0]))

# =============================================================================
# OUTPUT:
# mean of price: 
# 234144.26395939087
# mean of beds: 
# 2.9116751269035532
# mean of baths: 
# 1.7766497461928934
# mean of sq__ft: 
# 1314.9167512690356
# group by: 
# city
# ANTELOPE           115000
# AUBURN             260000
# CAMERON PARK       119000
# CARMICHAEL         139500
# CITRUS HEIGHTS      30000
# COOL               300000
# DIAMOND SPRINGS    216033
# EL DORADO          205000
# EL DORADO HILLS    235738
# ELK GROVE           71000
# ELVERTA            126000
# FAIR OAKS          142500
# FOLSOM             200000
# FORESTHILL         194818
# GALT               106716
# GARDEN VALLEY      490000
# GOLD RIVER         299000
# GRANITE BAY        600000
# GREENWOOD          395000
# LINCOLN              1551
# LOOMIS             295000
# MATHER             237800
# MEADOW VISTA       230000
# NORTH HIGHLANDS     63000
# ORANGEVALE         183200
# PENRYN             506688
# PLACERVILLE        205000
# POLLOCK PINES      175000
# RANCHO CORDOVA      94905
# RANCHO MURIETA      97750
# RIO LINDA           30000
# ROCKLIN            230095
# ROSEVILLE          115000
# SACRAMENTO          40000
# SHINGLE SPRINGS    275000
# SLOUGHHOUSE          2000
# WALNUT GROVE       380000
# WEST SACRAMENTO    147000
# WILTON             372000
# Name: price, dtype: int64
# order by: 
#                                   city    zip     ...       latitude   longitude
# street                                            ...                           
# 1740 HIGH ST                    AUBURN  95603     ...      38.891935 -121.084340
# 2231 COUNTRY VILLA CT           AUBURN  95603     ...      38.931671 -121.097862
# 220 OLD AIRPORT RD              AUBURN  95603     ...      38.939802 -121.054575
# 1484 RADCLIFFE WAY              AUBURN  95603     ...      38.935579 -121.079018
# 820 DANA CT                     AUBURN  95603     ...      38.865246 -121.094869
# 5332 SANDSTONE ST           CARMICHAEL  95608     ...      38.662105 -121.313945
# 5907 ELLERSLEE DR           CARMICHAEL  95608     ...      38.664468 -121.326830
# 4010 ALEX LN                CARMICHAEL  95608     ...      38.637028 -121.312963
# 5925 MALEVILLE AVE          CARMICHAEL  95608     ...      38.666564 -121.325717
# 2109 HAMLET PL              CARMICHAEL  95608     ...      38.602754 -121.329326
# 5709 RIVER OAK WAY          CARMICHAEL  95608     ...      38.602461 -121.330979
# 7032 FAIR OAKS BLVD         CARMICHAEL  95608     ...      38.628563 -121.328297
# 7110 STELLA LN Unit 15      CARMICHAEL  95608     ...      38.637396 -121.300055
# 5847 DEL CAMPO LN           CARMICHAEL  95608     ...      38.671995 -121.324339
# 4622 MEYER WAY              CARMICHAEL  95608     ...      38.649130 -121.310667
# 4734 GIBBONS DR             CARMICHAEL  95608     ...      38.635580 -121.353639
# 5733 ANGELINA AVE           CARMICHAEL  95608     ...      38.622634 -121.330846
# 5532 ENGLE RD               CARMICHAEL  95608     ...      38.631730 -121.335286
# 5118 ROBANDER ST            CARMICHAEL  95608     ...      38.657267 -121.310352
# 6326 APPIAN WAY             CARMICHAEL  95608     ...      38.662660 -121.316858
# 2949 PANAMA AVE             CARMICHAEL  95608     ...      38.618369 -121.326187
# 3621 WINTUN DR              CARMICHAEL  95608     ...      38.629929 -121.323086
# 4748 SALEM WAY              CARMICHAEL  95608     ...      38.634111 -121.353376
# 3230 SMATHERS WAY           CARMICHAEL  95608     ...      38.623372 -121.347665
# 5429 HESPER WAY             CARMICHAEL  95608     ...      38.665104 -121.315901
# 7944 SYLVAN OAK WAY     CITRUS HEIGHTS  95610     ...      38.710388 -121.261096
# 6344 BONHAM CIR         CITRUS HEIGHTS  95610     ...      38.682358 -121.272876
# 6824 OLIVE TREE WAY     CITRUS HEIGHTS  95610     ...      38.689239 -121.267737
# 6019 CHESHIRE WAY       CITRUS HEIGHTS  95610     ...      38.676437 -121.279165
# 8215 PEREGRINE WAY      CITRUS HEIGHTS  95610     ...      38.715493 -121.262930
#                                ...    ...     ...            ...         ...
# 5312 MARBURY WAY              ANTELOPE  95843     ...      38.710221 -121.341651
# 5712 MELBURY CIR              ANTELOPE  95843     ...      38.705849 -121.334701
# 8108 FILIFERA WAY             ANTELOPE  95843     ...      38.717042 -121.354680
# 8020 WALERGA RD               ANTELOPE  95843     ...      38.716070 -121.364468
# 3318 DAVIDSON DR              ANTELOPE  95843     ...      38.705753 -121.388917
# 4508 OLD DAIRY DR             ANTELOPE  95843     ...      38.722860 -121.358939
# 8721 SPRUCE RIDGE WAY         ANTELOPE  95843     ...      38.727657 -121.391028
# 3305 RIO ROCA CT              ANTELOPE  95843     ...      38.725079 -121.387698
# 5308 MARBURY WAY              ANTELOPE  95843     ...      38.710221 -121.341707
# 4712 PISMO BEACH DR           ANTELOPE  95843     ...      38.707705 -121.354153
# 4741 PACIFIC PARK DR          ANTELOPE  95843     ...      38.709299 -121.353056
# 3361 ALDER CANYON WAY         ANTELOPE  95843     ...      38.727649 -121.385656
# 3536 SUN MAIDEN WAY           ANTELOPE  95843     ...      38.709680 -121.382328
# 4008 GREY LIVERY WAY          ANTELOPE  95843     ...      38.718460 -121.370862
# 8716 LONGSPUR WAY             ANTELOPE  95843     ...      38.724083 -121.358400
# 7901 GAZELLE TRAIL WAY        ANTELOPE  95843     ...      38.711740 -121.342675
# 4085 COUNTRY DR               ANTELOPE  95843     ...      38.706209 -121.369509
# 8316 NORTHAM DR               ANTELOPE  95843     ...      38.720767 -121.376678
# 4240 WINJE DR                 ANTELOPE  95843     ...      38.708840 -121.359559
# 4636 TEAL BAY CT              ANTELOPE  95843     ...      38.704554 -121.354753
# 7921 DOE TRAIL WAY            ANTELOPE  95843     ...      38.711927 -121.343608
# 4509 WINJE DR                 ANTELOPE  95843     ...      38.709513 -121.359357
# 3604 KODIAK WAY               ANTELOPE  95843     ...      38.706175 -121.379776
# 8636 LONGSPUR WAY             ANTELOPE  95843     ...      38.725873 -121.358560
# 8428 MISTY PASS WAY           ANTELOPE  95843     ...      38.722959 -121.347115
# 4004 CRESTA WAY             SACRAMENTO  95864     ...      38.591618 -121.370626
# 3847 LAS PASAS WAY          SACRAMENTO  95864     ...      38.588672 -121.373916
# 909 SINGINGWOOD RD          SACRAMENTO  95864     ...      38.581471 -121.388390
# 4204 LUSK DR                SACRAMENTO  95864     ...      38.606569 -121.368424
# 3863 LAS PASAS WAY          SACRAMENTO  95864     ...      38.588936 -121.373606
# 
# [985 rows x 11 columns]
# 
# =============================================================================
