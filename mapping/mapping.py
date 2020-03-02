import folium

map=folium.Map(location=[-1.371612, 36.719056], zoom_start=10, tiles="Mapbox Bright")\

fg=folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[1.37, 36.719], popup="this is kenya", icon=folium.Icon(color='red')))
map.add_child(fg)

map.save("map2.html")
