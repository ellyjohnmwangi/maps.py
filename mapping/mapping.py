import folium

map=folium.Map(location=[-1.371612, 36.719056], zoom_start=10, tiles="Mapbox Bright")\

fg=folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[1.37, 36.719], popup="gataka", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[-0.435305, 36.959052], popup="nyeri", icon=folium.Icon(color='orange')))
fg.add_child(folium.Marker(location=[-1.038653, 37.083425], popup="thika", icon=folium.Icon(color='black')))
fg.add_child(folium.Marker(location=[-0.057283, 34.779527], popup="kisumu", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[-0.721058, 37.154714], popup="murang'a", icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(location=[-0.275395, 36.377494], popup="olkalou", icon=folium.Icon(color='beige')))

map.add_child(fg)

map.save("map2.html")
