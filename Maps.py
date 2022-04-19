import pandas as pd
import numpy as np
import folium
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from google.colab import drive
drive.mount('/content/drive')

data= pd.read_csv('/content/drive/MyDrive/Project/Crime (18-p)/Crime - (18-p) 1_data3.csv')

data=data.dropna()
data[['District', 'Ward','Community Area']] = data[['District', 'Ward','Community Area']].astype('str')
data[['District', 'Ward','Community Area']] = data[['District', 'Ward','Community Area']].astype('str')

data.columns= data.columns.str.strip().str.lower().str.replace(' ','_')

style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
								
								
ward_geo = r'https://data.cityofchicago.org/api/geospatial/sp34-6z76?method=export&format=GeoJSON'

WardData = pd.DataFrame(data['ward'].value_counts(ascending=True).astype(float))
WardData = WardData.reset_index()
WardData.columns = ['ward', 'Crime_Count']
 
#myscale = (WardData['Crime_Count'].quantile((0, 0.50, 0.65, 0.90, 0.98, 1))).tolist()

map1 = folium.Map(location=[41.815117282, -87.669999562], zoom_start=11,)# tiles='')
map1.choropleth(geo_data = ward_geo, 
                data = WardData,
                columns = ['ward', 'Crime_Count'],
                key_on = 'feature.properties.ward',
                fill_color = 'Reds', 
                fill_opacity = 0.7, 
                line_opacity = 0.2,
                #tooltip = 'hi',
                #threshold_scale=myscale, #[0, 50000, 100000, 150000, 200000, 300000],
                highlight=True,
                legend_name = 'Number of incidents per police ward')

feature = folium.features.GeoJson(
        ward_geo,
        style_function=style_function,
        control=False,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=[
                'ward',
            ],
            aliases=[
                "Ward Number: ",
            ],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
            )
        )

map1.add_child(feature)
map1.keep_in_front(feature)


map1

district_geo = r'https://data.cityofchicago.org/api/geospatial/fthy-xz3r?method=export&format=GeoJSON'

#calculating total number of incidents per district
DisData = pd.DataFrame(data['district'].value_counts(ascending=True).astype(float))
DisData = DisData.reset_index()


DisData.columns = ['district', 'Crime_Count']
 
#myscale = (DisData['Crime_Count'].quantile((0,0.40,0.60,0.9,0.98,1))).tolist()

map2 = folium.Map(location=[41.815117282, -87.669999562], zoom_start=11, )#tiles='Mapbox Bright')
map2.choropleth(geo_data = district_geo, 
                data = DisData,
                columns = ['district', 'Crime_Count'],
                key_on = 'feature.properties.dist_num',
                fill_color = 'Reds', 
                fill_opacity = 0.7, 
                line_opacity = 0.2,
                #threshold_scale=myscale,
                highlight=True,
                legend_name = 'Number of incidents per police district',

               )


feature = folium.features.GeoJson(
        district_geo,
        style_function=style_function,
        control=False,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=[
                'dist_num',
                'dist_label',
            ],
            aliases=[
                "District Number: ",
                "District Label: "
            ],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
            )
        )

        
map2.add_child(feature)
map2.keep_in_front(feature)

map2

com_geo = r'https://data.cityofchicago.org/api/geospatial/cauq-8yn6?method=export&format=GeoJSON'

#calculating total number of incidents per district
ComData = pd.DataFrame(data['community_area'].value_counts().astype(float))
ComData = ComData.reset_index()


ComData.columns = ['community_area', 'Crime_Count']
 
#myscale = (DisData['Crime_Count'].quantile((0,0.40,0.60,0.9,0.98,1))).tolist()

map3 = folium.Map(location=[41.815117282, -87.669999562], zoom_start=11, tiles='Mapbox Bright')
map3.choropleth(geo_data = com_geo, 
                data = ComData,
                columns = ['community_area', 'Crime_Count'],
                key_on = 'feature.properties.area_numbe',
                fill_color = 'Reds', 
                fill_opacity = 0.7, 
                line_opacity = 0.2,
                #threshold_scale=myscale,
                highlight=True,
                legend_name = 'Number of incidents per police district')

feature = folium.features.GeoJson(
        com_geo,
        style_function=style_function,
        control=False,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=[
                'area_numbe',
                'community',
                  
            ],
            aliases=[
                "Area Number: ",
                "Name: "
            ],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
            )
        )

    
map3.add_child(feature)
map3.keep_in_front(feature)

map3								