import requests
from dotenv import load_dotenv
import os
from skyfield.api import load, wgs84, N, W
from skyfield.iokit import parse_tle_file
from serial import Serial
import time
from io import BytesIO

load_dotenv()

#  ------------------- Variables -----------------------


NORAD_ID = 25544 # ISS NORAD ID for now
BASE_URL = r"https://api.n2yo.com/rest/v1/satellite/"
API_KEY = os.getenv("N2YO_API_KEY")
GS_LAT = 21.3167
GS_LON = -157.9430
GS_ALT = 4 # In meters
SERIAL_PORT = '/dev/ttyUSB0'
BAUD = 9600 # GS-232 default
MIN_ELEVATION = 10 # In degrees
CALIBRATED_AZ = 0
CALIBRATED_EL = 0


# ------------------------------------------------------

ser = Serial(SERIAL_PORT, BAUD, timeout=1)
location = wgs84.latlon(GS_LAT, GS_LON, GS_ALT)
ts = load.timescale()

def get_tle(norad_id):
    tle = requests.get(f"{BASE_URL}/tle/{norad_id}&apiKey={API_KEY}").json()['tle']
    with open(f"{norad_id}.tle", mode="w") as f:
        f.write(tle)
    return tle

def get_next_radio_pass(norad_id, min_elevation: int = 10, prediction_days: int = 3):
    passes = requests.get(f"{BASE_URL}/radiopasses/{norad_id}/{GS_LAT}/{GS_LON}/{GS_ALT}/{prediction_days}/{min_elevation}&apiKey={API_KEY}").json()
    if len(passes['passes']) > 0:
        next_pass = passes['passes'][0]
        return next_pass
    else: return None


def track_to(az, el):
    """
    Expects az and el in integer degrees
    """
    command = f"W{az:03d} {el:03d}"
    ser.write(command.encode())

try:
    get_tle(NORAD_ID)
    print(f"[+] Loaded TLE data for NORAD ID: {NORAD_ID}")
except: print(f"[-] Failed to get TLE data for NORAD ID: {NORAD_ID}")

try:
    ts = load.timescale()
    with load.open(f'{NORAD_ID}.tle') as f:
        satellite = list(parse_tle_file(f, ts))[0]
    print(f"[+] Satellite {NORAD_ID} epoch is {satellite.epoch.utc_jpl()}")
except: print(f"Failed to parse TLE data")

while True:
    difference = satellite - location
    topocentric = difference.at(ts.now())
    alt, az, distance = topocentric.altaz()
    # if alt.degrees < MIN_ELEVATION:
    #     print('[-] The selected satellite is below the minimum elevation threshold')
    #     break
    print(f"Azimuth: {round(az.degrees, 2)}°, Elevation: {round(alt.degrees, 2)}°                  ", end="\r")
    track_to(round(az.degrees), round(alt.degrees))
    time.sleep(.25)