# This file uses the 'geopy' library to get the location(lat,long) of a given ward in Bengaluru.
# This program reads the wards from 'ward_list.txt' and writes the corresponding location into
# the 'ward_loc.txt' file. Finally, we have total 165 wards' locations.


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="google maps")
ip = open("ward_list.txt", "r")
op = open("ward_loc.txt","w+")
for i in range(198):
	cur = ip.readline().strip()
	query = cur + " bangalore"
	location = geolocator.geocode(query)
	#print(location.address)
	if location is None:
		continue
	print(i)
	op.write(cur + " " + str(location.latitude) + " " + str(location.longitude) + "\n")
ip.close()
op.close()