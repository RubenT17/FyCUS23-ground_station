def nmea2geodetic(data):
    lat_aux=data[0]/100
    lat_deg=np.trunc(lat_aux)
    lat_min=lat_aux-lat_deg
    lat=lat_deg+lat_min/60

    lon_aux=data[2]/100
    lon_deg=np.trunc(lon_aux)
    lon_min=lon_aux-lon_deg
    lon=lon_deg+lon_min/60

    data[0]=lat
    data[2]=lon  
    return data