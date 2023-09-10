from GPSPhoto import gpsphoto

def get_info(path: str):
    return gpsphoto.getGPSData(path)
