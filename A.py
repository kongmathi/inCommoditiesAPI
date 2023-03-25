
import requests
import csv

areas = ['Eagle_River', 
         'Kincaid_Park',
         'Far_North_Bicentennical_Park',
         'Bear_Valley',
         'Fire_Island']

token = 'Bearer 133326de5eac419883ad9f0859e70378'
file = open('data.csv')

for area in areas:
    url = 'https://incommodities.io/a?area=' + area
    response = requests.post(
                url, 
                headers={'Authorization': token})
    file.write(response)

csvreader = csv.reader(file)
