import requests
import json
import re
import config

my_url = "https://hotels4.p.rapidapi.com/locations/v3/search"


headers = {
	"X-RapidAPI-Key": config.RAPID_API_KEY,
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}


def destination_id(city):
	pattern = '<[^>]*'
	querystring = {"q": city, "locale": "en_US", "currency": "USD"}
	response = requests.get(my_url, headers=headers, params=querystring)
	data = json.loads(response.text)           # десериализация JSON
	with open('descr_city.json', 'a') as city_file:
		json.dump(data, city_file, indent=4)   # сериализация JSON

	possible_city = {}
	for i_city in data['suggestions'][0]['entities']:
		possible_city[i_city['destinationId']] = re.sub(pattern, '', i_city['caption'])
	return possible_city
