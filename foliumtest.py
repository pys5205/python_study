import folium

latitude = 37.566345
longitude = 126.977893

map_osm = folium.Map(location=[latitude, longitude])
map_osm.save('d:/study/map1.html')
print(type(map_osm))

map_osm = folium.Map(location=[latitude, longitude], zoom_start=16)
map_osm.save('d:/study/map2.html')

map_osm=folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Terrain')
map_osm.save('d:/study/map3.html')

map_osm = folium.Map(location=[latitude, longitude])
folium.Marker([latitude, longitude],popup='서울특별시청').add_to(map_osm)
map_osm.save('d:/study/map4.html')

map_osm=folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup='서울 특별시청',icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)

folium.CircleMarker([37.5658859, 126.9754788], radius=150, color='blue', 
                   fill_color='red', fill=False, popup='덕수궁').add_to(map_osm)

map_osm.save('d:/study/map5.html')
print('save')

