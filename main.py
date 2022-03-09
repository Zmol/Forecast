import requests
from bs4 import BeautifulSoup
'''
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
'''

'''
#LEARNING HOW TO FIND TAGS
#shows the type of each element in list.
#The .children-method returns a list generator, so we call the list-function on it.
#The list comprehension loop shows that the type of element in top level of the page (bs4)
#We are interested in the 3rd <html> which is bs4.element.Tag
print([type(item) for item in list(soup.children)])

#We can now select the html tag and its children by taking the third item in the list:
#Each item in the list returned by the children property is also a BeautifulSoup object,
#so we can also call the children method on new list called "html".
html = list(soup.children)[2]

body = list(html.children)[3]

#Once we’ve isolated the tag, we can use the get_text method to extract all of the text inside the tag:
p = list(body.children)[1]
print(p.get_text())

#What we did above was useful for figuring out how to navigate a page,
#but it took a lot of commands to do something fairly simple.

#If we want to extract a single tag, we can instead use the find_all
#method, which will find all the instances of a tag on a page.
'''

'''
#FINDING ALL INSTANCES OF A TAG AT ONCE
#find_all returns a list, so we’ll have to loop through, or use list indexing, it to extract text:
#Her er først bogens eksempel og dernæst mit loop - samme resultat

print(soup.find_all('p')[0].get_text())

x = soup.find_all('p')
for i in x:
    print(i.get_text())

#f you instead only want to find the first instance of a tag,
# you can use the find method, which will return a single BeautifulSoup object:
'''

#SEARCHING FOR TAGS BY CLASS AND ID

#page = requests.get('https://www.molslinjen.dk/fartplan')
#print(page.content)
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#time_table = soup.find_all('div', class_="Departure-eta")
#print(time_table)

import datetime
today = datetime.datetime.today()
#datetime.datetime(2022,3,30)
url = "https://www.molslinjen.dk/umbraco/api/departure/getdepartures"
data ={
  "date": today.strftime("%Y-%m-%d"), #2022-03-04
  "departureRegionId": "SJÆ",
  "transportId": "10",
}

req = requests.post(url, json=data)
#print(req.json())



result = req.json()
for r in result:
    print(r[0])
    for key, val in r[0].items():
        print(key, type(key))

        if key == "arrivalTime":
            tmp = val.split(":")
            hour = int(tmp[0])
            minut = int(tmp[1])
            today = today.replace(hour=hour, minute=minut)
            print(today)
            #minut = minut += 10
            surf = today.replace(minute=minut)
            print(surf)

    #for key, val in r[0].items():
        #print(key, val)


#[[{'id': 'SJÆ_3_20220330_0720', 'date': '2022-03-30T00:00:00', 'departureTime': '07:20:00', 'arrivalTime': '08:35:00', 'travelTime': '01:15:00', 'price': 449.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 4', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_0820', 'date': '2022-03-30T00:00:00', 'departureTime': '08:20:00', 'arrivalTime': '09:35:00', 'travelTime': '01:15:00', 'price': 399.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 3', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_0920', 'date': '2022-03-30T00:00:00', 'departureTime': '09:20:00', 'arrivalTime': '10:35:00', 'travelTime': '01:15:00', 'price': 299.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 2', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1100', 'date': '2022-03-30T00:00:00', 'departureTime': '11:00:00', 'arrivalTime': '12:15:00', 'travelTime': '01:15:00', 'price': 224.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 4', 'limitedAvailability': True, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1200', 'date': '2022-03-30T00:00:00', 'departureTime': '12:00:00', 'arrivalTime': '13:15:00', 'travelTime': '01:15:00', 'price': 199.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 3', 'limitedAvailability': True, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1300', 'date': '2022-03-30T00:00:00', 'departureTime': '13:00:00', 'arrivalTime': '14:15:00', 'travelTime': '01:15:00', 'price': 224.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 2', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1430', 'date': '2022-03-30T00:00:00', 'departureTime': '14:30:00', 'arrivalTime': '15:45:00', 'travelTime': '01:15:00', 'price': 249.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 4', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1530', 'date': '2022-03-30T00:00:00', 'departureTime': '15:30:00', 'arrivalTime': '16:45:00', 'travelTime': '01:15:00', 'price': 274.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 3', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1630', 'date': '2022-03-30T00:00:00', 'departureTime': '16:30:00', 'arrivalTime': '17:45:00', 'travelTime': '01:15:00', 'price': 299.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 2', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1800', 'date': '2022-03-30T00:00:00', 'departureTime': '18:00:00', 'arrivalTime': '19:15:00', 'travelTime': '01:15:00', 'price': 324.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 4', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_1915', 'date': '2022-03-30T00:00:00', 'departureTime': '19:15:00', 'arrivalTime': '20:30:00', 'travelTime': '01:15:00', 'price': 249.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 3', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}, {'id': 'SJÆ_3_20220330_2045', 'date': '2022-03-30T00:00:00', 'departureTime': '20:45:00', 'arrivalTime': '22:00:00', 'travelTime': '01:15:00', 'price': 199.0, 'information': '', 'route': 'Odden - Aarhus', 'routeId': 'SJÆ3', 'categoryId': '1', 'cssClass': 'lavpris', 'categoryName': 'Lavpris', 'ferry': 'Express 2', 'limitedAvailability': False, 'soldOut': False, 'cancelled': False, 'departureHarbor': 'Odden', 'departureHarborId': 'ODD', 'isPopularTicket': False, 'softPassengersOnly': False, 'departureCode': '0', 'routeTypes': [0]}], '0']





'''
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)
'''



'''
#print([item for item in list(soup2.children)])

html = list(soup.children)[3]
print([type(item) for item in html])

#print([type(item) for item in list(html.children)])

#y = soup2.find_all(class_="outer-text")
#print(y)
'''


