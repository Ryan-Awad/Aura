from algorithm.input_and_output import listen_input, speak, yes_or_no
import requests
from bs4 import BeautifulSoup

# http://weather.service.msn.com/find.aspx?src=outlook&weadegreetype=F&culture=en-US&weasearchstr=San%20Franscisco,%20California

speak("What city or postal code would you like to check?", True)
loc = listen_input()

main_url = "http://weather.service.msn.com/find.aspx"
url_params = "?src=outlook&weadegreetype=C&weasearchstr=" + str(loc)
url = main_url + url_params

response = requests.get(url) # YOU MIGHT GET MORE THAN ONE RESULT WITH YOUR LOCATION, HANDLE THAT!!!
xml = BeautifulSoup(response.content, 'html.parser')

data = xml.find("weatherdata").find("weather")
current = data.find("current")
weekly = data.find_all("forecast")

location = data.get("weatherlocationname")

current_date = current.get("date")
current_day = current.get("day")
current_tempC = current.get("temperature")
current_tempF = str((int(current_tempC) * 9 / 5) + 32)
current_feelslikeC = current.get("feelslike")
current_feelslikeF = str((int(current_feelslikeC) * 9 / 5) + 32)
current_humidity = current.get("humidity")
current_sky = current.get("skytext")
current_wind = current.get("winddisplay")

weekly_date = []
weekly_day = []
weekly_lowC = []
weekly_lowF = []
weekly_highC = []
weekly_highF = []
weekly_sky = []
weekly_precip = []

for _day in weekly:
    date = _day.get("date")
    day = _day.get("day")
    lowC = _day.get("low")
    lowF = str((int(lowC) * 9 / 5) + 32)
    highC = _day.get("high")
    highF = str((int(highC) * 9 / 5) + 32)
    sky = _day.get("skytextday")
    precip = _day.get("precip")

    weekly_date.append(date)
    weekly_day.append(day)
    weekly_lowC.append(lowC)
    weekly_lowF.append(lowF)
    weekly_highC.append(highC)
    weekly_highF.append(highF)
    weekly_sky.append(sky)
    weekly_precip.append(precip)


print("\n\nToday's Weather:\n" + "-" * 50)
print("Location: " + location)
print("Date: " + current_date)
print("Day: " + current_day)
print("Temperature (°C): " + current_tempC + " °C")
print("Temperature (°F): " + current_tempF + " °F")
print("Feels like (°C): " + current_feelslikeC + " °C")
print("Feels like (°F): " + current_feelslikeF + " °F")
print("Sky: " + current_sky)
print("Humidity: " + current_humidity + "%")
print("Wind: " + current_wind)

speak("For today's weather in " + location + ", the current temperature is " + current_tempC + " degrees celsius or " + current_tempF + " degrees fahrenheit, and it feels like " + current_feelslikeC + " degrees celsius or " + current_feelslikeF + " degrees fahrenheit. The sky is " + current_sky + " and the humidity is at " + current_humidity + " percent. And also, the wind speed is at " + current_wind + ".", False)
print("\n")
speak("Would you like to look at this weeks weather?", True)
week_weather = listen_input()
if week_weather != None:
    yes = yes_or_no(week_weather)

    if yes:
        print("\n\n\nThis Week's Weather:\n" + "-" * 50)
        for i in range(len(weekly)):
            print("Day: " + weekly_day[i])
            print("Date: " + weekly_date[i])
            print("High (°C): " + weekly_highC[i] + " °C")
            print("High (°F): " + weekly_highF[i] + " °F")
            print("Low (°C): " + weekly_lowC[i] + " °C")
            print("Low (°F): " + weekly_lowF[i] + " °F")
            print("Sky: " + weekly_sky[i])
            print("Precipitation: " + weekly_precip[i] + "%\n" + "-" * 50)
        
        speak("Here is this week's weather!", False)