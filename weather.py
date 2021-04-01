import requests, json
import matplotlib.pyplot as plt


api_key = "api" # Enter your API key


base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = input("Enter city name : ")


# Complete Url for request
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":     # If city is not found

	y = x["main"]                                # Getting data after forming request with the OWM and it will get
	current_temperature = y["temp"]               # data for current temperature, pressure and humidity.
	current_pressure = y["pressure"]
	current_humidiy = y["humidity"]
	z = x["weather"]


	weather_description = z[0]["description"]

	plt.scatter(current_temperature, current_humidiy)
	plt.xlabel("Temperature")
	plt.ylabel("Pressure")
	plt.title("Analysis of Weather Data")
	plt.show()

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n Atmospheric Pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n Humidity (in percentage) = " +
					str(current_humidiy) +
		"\n Description = " +
					str(weather_description))

else:
	print(" City Not Found ")






