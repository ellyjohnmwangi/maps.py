import folium

map=folium.Map(location=[-1.371612, 36.719056], zoom_start=10, tiles="Mapbox Bright")\

fg=folium.FeatureGroup(name="my map")
for coordinate in [[1.37, 36.719],[-0.435305, 36.959052],[-1.038653, 37.083425],[-0.057283, 34.779527],[-0.721058, 37.154714],[-0.275395, 36.377494]]:
    fg.add_child(folium.Marker(location=[1.37, 36.719], popup="a town in kenya", icon=folium.Icon(color='red')))


map.add_child(fg)

map.save("map2.html")
