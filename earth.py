import ee  
import location

#uncomment if authentication is needed
#ee.Authenticate()
ee.Initialize()

def dd_to_dms(deg: float) -> dict:
    degrees = deg
    minutes = int((deg - degrees) * 60)
    seconds = ((deg - degrees) * 3600) - (minutes * 60)

    return {
        'degrees': degrees,
        'minutes': minutes,
        'seconds': seconds
    }

def get_url(longitude: float, latitude: float, altitude: float):
    return f'https://earth.google.com/web/search/@{longitude},{latitude},{100}a/' 
