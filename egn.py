import csv
import json
# from pprint import pprint

# Your settings

year = 2020

null = None 

# put the json-data from your webbrowser here:
data = {"waste_discharge":{"2020":{ __Put your Data here!__ } } }

def main():
    
    garbage_cans = {'bio':  'braune Tonne',
                    'hml':  'graue Tonne',
                    'hml2': 'None',
                    'lvp':  'gelbe Tonne',
                    'ppk':  'blaue Tonne',
                    'wbm':  'braune Tonne'}
    
    null = None

    # pprint(data['waste_discharge'][str(year)])

    # pprint(data['trash_type_colors'])

    output = [['Subject', 'Start date', 'All Day Event']]

    for month in range(1,13):
        for day in data['waste_discharge'][str(year)][str(month)].keys():
            subject = garbage_cans[data['waste_discharge'][str(year)][str(month)][day][0].lower()]
            all_day_event = True
            start_date = "{:02d}/{:02d}/{:02d}".format(month, int(day), year) 
            output.append([subject, start_date, all_day_event])

    with open('egn_{}_calendar.csv'.format(year), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerows(output)



if __name__ == "__main__":
    main()
