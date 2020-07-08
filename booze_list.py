# This file uses Google Maps API to find the nearby '"'liquor_stores' given a location(lat, long).

# https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters
# https://maps.googleapis.com/maps/api/place/textsearch/output?parameters

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY

google_maps_api_key = "AIzaSyAyd3j-9Ad4o-Bx57Ue0VpzHd2JKkrmJRs"
import requests
import json

ip = open("ward_loc.txt", "r")
op = open("liquor_stores.txt", "w+")
# url for nearby search
url_p = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
url_s = "&radius=2000&type=liquor_store&key=AIzaSyAyd3j-9Ad4o-Bx57Ue0VpzHd2JKkrmJRs"
# url for place details
url_pd = "https://maps.googleapis.com/maps/api/place/details/json?place_id="
url_sd = "&fields=name,rating,formatted_phone_number,international_phone_number,user_ratings_total,vicinity&key=AIzaSyAyd3j-9Ad4o-Bx57Ue0VpzHd2JKkrmJRs"

# this set will help us avoid repitition of requeting same place's details
place_id_set = set({})

for i in range(165):
	cur = ip.readline().strip().split()
	location = cur[1] + "," + cur[2]

	# Requesting for nearby places' "place_ID" parameter for the current input location(lat,long)
	maps_url = url_p + location + url_s
	# maps_url = "www.google.com"
	response = requests.get(maps_url)
	# print(response.text)
	data = json.loads(response.text)
	places_nearby = data["results"]

	print("i: ", i)
	# Requesting for place details using the place_ID

	for place in places_nearby:
		cur_id = place['place_id']
		
		# check if we've already visited this place
		if cur_id in place_id_set:
			continue
		place_id_set.add(cur_id)

		# make the request for details of the place with the current place_ID
		place_url = url_pd + cur_id + url_sd
		response1 = requests.get(place_url)
		data1 = response1.text
		data1_dict = json.loads(response1.text)
		# check whether the current place's details contain the phone number or not
		if "formatted_phone_number" not in data1_dict['result']:
			continue
		# "user_ratings_total"
		op.write(data1)

ip.close()
op.close()
