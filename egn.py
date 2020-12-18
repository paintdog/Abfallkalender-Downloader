import csv
import json
from bs4 import BeautifulSoup
import requests


year = 2020
city = "Brüggen"
district = "Bracht"
street = "Agrisstrasse"
house_number = "1"



EGN_URL = "https://www.egn-abfallkalender.de/kalender"
EGN_ALEXA_URL = "https://www.egn-abfallkalender.de/alexa"

garbage_cans = {'bio':  'braune Tonne',
                'hml':  'graue Tonne',
                'hml2': 'None',
                'lvp':  'gelbe Tonne',
                'ppk':  'blaue Tonne',
                'wbm':  'braune Tonne'}

def create_filename(parameter, year):
    ''' creates a filename city-street-street_number '''
    return "{} - {}{} ({}).csv".format(parameter['city'],
                                       parameter['street'],
                                       parameter['street_number'],
                                       year)

def create_parameter(city, district, street, house_number):
    ''' builds the parameter list '''
    return {'city': city,
           'district': district,
           'street': street,
           'street_number': house_number}
    
def load_data(url, parameter):
    ''' download data from www.egn-abfallkalender.de '''
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html5lib")
    meta_token = soup.find("meta", attrs={"name": "csrf-token"})
    data = session.post(url,
                        data=parameter,
                        headers={"x-csrf-token": meta_token.attrs['content']})
    data = json.loads(data.text)
    return data

def filter_calendar_for_year(data, year):
    ''' filters the calendar data by year '''
    output = [['Subject', 'Start date', 'All Day Event']]
    for month in range(1,13):
        for day in data['waste_discharge'][str(year)][str(month)].keys():
            subject = garbage_cans[data['waste_discharge'][str(year)][str(month)][day][0].lower()]
            all_day_event = True
            start_date = "{:02d}/{:02d}/{:02d}".format(month, int(day), year) 
            output.append([subject, start_date, all_day_event])
    return output

def write_csv(calendar_data, parameter, year):
    ''' writes a csv that you can import to Google Kalender'''
    with open(create_filename(parameter, year), 'w', newline='') as csvfile:
        events_writer = csv.writer(csvfile)
        events_writer.writerows(calendar_data)

def main():
    ''' loads calendar data from the egn website and
    creates a csv-file. '''
    parameter = create_parameter(city, district, street, house_number)
    data = load_data(EGN_URL, parameter)
    calendar_data = filter_calendar_for_year(data, year)
    write_csv(calendar_data, parameter, year)
   
if __name__ == "__main__":
    main()
