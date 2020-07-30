from openalpr import Alpr
import sys
import cv2
import imutils
import requests
import random

from bs4 import BeautifulSoup

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# Parameters - country, path to config file, path to runtime
alpr = Alpr("in", "/home/praful/openalpr/src/build/config/openalpr.conf", "/home/praful/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

# Set to Top 5 results
alpr.set_top_n(5)

# SpreadSheet Credentials and import sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creads = ServiceAccountCredentials.from_json_keyfile_name("creads.json", scope)
client = gspread.authorize(creads)
sheet = client.open("Vehicle_data").sheet1

# URL for scraping info
url = "https://vahaninfos.com/vehicle-details-by-number-plate"

# Random choice variables
CSlist = ['MUM', 'PUNE']
durationlist = [65, 50, 100, 120]


def get_vehicle_details(lic_plate):
    '''Returns Vehicle info from lic_plate'''
    # Create Session
    car_record = dict()
    with requests.Session() as s:
        reponse = s.get(url)
        soup = BeautifulSoup(reponse.text, 'html5lib')
        id = (soup.find('input', id='num2')).get('value')
        # Request Headers
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "referrer": "https://vahaninfos.com/vehicle-details-by-number-plate"
        }
        # Payload
        data = {
            'num': lic_plate,
            'id': id,
        }
        table_body = s.post('https://vahaninfos.com/getdetails.php', headers=headers, data=data)
        data = BeautifulSoup(table_body.text, 'lxml')
        rows = data.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            car_record[cols[0].text.strip()] = cols[2].text.strip()
        # Remove Spaces and return car model name only
        try:
            return car_record['Model/Model Name'].split('/')[1].strip()
        except IndexError:
            # Invalid Number
            return 0


def getrow(fileno):
    '''Get License Plate of Vehicle from Video Stream'''
    vidcap = cv2.VideoCapture('/home/praful/Cars/car' + str(fileno) + '.mp4')
    success, image = vidcap.read()
    while success:
        image = imutils.resize(image, width=800)
        _, enc = cv2.imencode("*.bmp", image)
        results = alpr.recognize_array(enc.tobytes())
        for plate in results['results']:
            for candidate in plate['candidates']:
                if candidate['matches_template']:
                    car_model = get_vehicle_details(candidate['plate'])
                    if(car_model):
                        city = random.choice(CSlist)
                        duration = random.choice(durationlist)
                        stop_time = datetime.now().strftime("%d/%m/%Y %H:%M")
                        start_time = (datetime.now() - timedelta(minutes=duration)).strftime("%d/%m/%Y %H:%M")
                        # Charging rate per hour * (duration/60)
                        consumption = str(round(2.3 * (duration/60), 2))
                        return [candidate['plate'], car_model, city + '00' + str(random.randint(1, 3)),
                                city, str(start_time), str(stop_time), str(duration), consumption]
        success, image = vidcap.read()


def main():
    for i in range(4):
        row_to_add = getrow(i+1)
        sheet.insert_row(row_to_add, 2)


if __name__ == "__main__":
    main()
