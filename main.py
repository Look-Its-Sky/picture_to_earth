import location, earth

info = location.get_info('test1.jpg')
print(earth.get_url(info.get('Latitude'), info.get('Longitude'), info.get('Altitude')))
