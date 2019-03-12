import folium
import pandas as pd
import os
from folium_jsbutton import JsButton

states = os.path.join('data', 'us-states.json')
unemployement_data = os.path.join('data', 'us_unemployment.csv')
state_data = pd.read_csv(unemployement_data)

m = folium.Map(location=[48, -102], zoom_start=3)

JsButton(
    title='<i class="fa fa-home"></i>',function="""
    function() {
        window.location.href = "index.html"
    }
    """).add_to(m)

JsButton(
    title='<i class="fas fa-arrow-circle-left"></i>',function="""
    function() {
        window.location.href = "map.html"
    }
    """).add_to(m)


m.choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate %'
)

folium.LayerControl().add_to(m)

m.save('p_map.html')
