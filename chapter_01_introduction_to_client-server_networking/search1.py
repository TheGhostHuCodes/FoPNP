#!/usr/bin/env python3

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = "140 New Montgomery, San Francisco, CA"
    print(Geocoder.geocode(address)[0].coordinates)
