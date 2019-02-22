import folium
import os
import json
from branca.element import Template, MacroElement
import matplotlib.pyplot as plt




# Create map object
m = folium.Map(location=[51.522742, -0.041627], zoom_start=13, max_zoom=18, min_zoom=13) #Limiting initial, minimum and maximum zone.

# Global tooltip declarations here
tooltip_1 = 'Click For Air Quality Info'


overlay = os.path.join('data', 'overlay.json')

# Create markers for underground stations
folium.Marker([51.525211, -0.033503],
              popup='<strong>Mile End Station</strong>',
              tooltip=tooltip_1,
              icon=folium.Icon(icon='stats')).add_to(m),
folium.Marker([51.527847, -0.055468],
              popup='<strong>Bethnel Green Station</strong>',
              tooltip=tooltip_1,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([51.521739, -0.046636],
              popup='<strong>Stepney Green Station</strong>',
              tooltip=tooltip_1,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([51.519531, -0.061234],
              popup='<strong>Whitechapel Station</strong>',
              tooltip=tooltip_1,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([51.527002, -0.024764],
              popup='<strong>Bow Road</strong>',
              tooltip=tooltip_1).add_to(m),
folium.Marker([51.522460, -0.017470],
              popup='<strong>Devons Road</strong>',
              tooltip=tooltip_1).add_to(m),
folium.Marker([51.511740, -0.055860],
              popup='<strong>Shadwell</strong>',
              tooltip=tooltip_1).add_to(m),
folium.Marker([51.512350, -0.039466],
              popup='<strong>LimeHouse</strong>',
              tooltip=tooltip_1).add_to(m),
folium.Marker([51.507538, -0.012823],
              popup='<strong>Blackwall DLR</strong>',
              tooltip=tooltip_1).add_to(m),
folium.Marker([51.515800, -0.014330],
              popup='<strong>Langdon Park</strong>',
              tooltip=tooltip_1).add_to(m),


folium.Circle(location = [51.525211, -0.033503],
                    radius = 2500, popup = ' FRI ').add_to(m)

# Geojson overlay
# folium.GeoJson(overlay, name='cambridge').add_to(m)

# Generate map
m.save('map.html')

#Testing commit

#Adding Labels


template = """
{% macro html(this, kwargs) %} 

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Geostatistical Air Pollution Analysis</div>
<div class='legend-title'>Data Analytics Project 2019</div>

<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:red;opacity:0.9;'></span>Legend 1</li>
    <li><span style='background:orange;opacity:0.9;'></span>Legend 2</li>
    <li><span style='background:green;opacity:0.9;'></span>Legend 3</li>

  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)

m
#End of adding labels



m.save('map.html') #Render map
