# -*- coding: utf-8 -*-
"""
GIS Distance Calculator for Civil and Water Engineering Projects
Calculates the great-circle distance between two geographic coordinates.
"""

import math

def haversine_distance(lat1, lon1, lat2, lon2):
    # Earth radius in kilometers
    R = 6371.0
    
    # Convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    
    # Haversine formula
    a = math.sin(d_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    
    distance = R * c
    return distance

if __name__ == "__main__":
    print("--- GIS Distance Calculator for Engineering Projects ---")
    
    # Example coordinates: Tabriz and Ardabil
    lat_tabriz, lon_tabriz = 38.0800, 46.2919
    lat_ardabil, lon_ardabil = 38.2498, 48.2933
    
    dist = haversine_distance(lat_tabriz, lon_tabriz, lat_ardabil, lon_ardabil)
    
    print(f"Point 1 (Tabriz): Latitude {lat_tabriz}, Longitude {lon_tabriz}")
    print(f"Point 2 (Ardabil): Latitude {lat_ardabil}, Longitude {lon_ardabil}")
    print(f"Direct Geographic Distance: {dist:.2f} km")
