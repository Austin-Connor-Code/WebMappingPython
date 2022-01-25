import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

map = folium.Map(location=[latitude[0], longitude[0]],
                 zoom_start=6)

fg1 = folium.FeatureGroup(name="Volcano Elevation")

fg2 = folium.FeatureGroup(name='Population')


def calc_elevation(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation >= 1500 and elevation <= 3000:
        return 'orange'
    else:
        return 'red'


for i, j, k in zip(latitude, longitude, elevation):
    fg1.add_child(folium.CircleMarker(
        location=[i, j], radius=6, popup=str(k) + "m", color='grey', fill_color=calc_elevation(k), fill=True, fill_opacity=0.7))

fg2.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg2)
map.add_child(fg1)

map.add_child(folium.LayerControl())

map.save("Map.html")
