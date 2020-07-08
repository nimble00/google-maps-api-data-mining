# google-maps-api-data-mining
A self project.

Problem Statement: Return a list of all the liquor stores in Bangalore.

Steps to solve it:
1. I got the list of all the wards in Bangalore from Wikipedia, stored it in 'input_data.txt'.
2. Then, I coded 'get_wards.py' to generate a clean list of wards in 'wards_list.txt'
3. In 'locate_ward.py', I used 'geopy' to get the location(latitude, longitude) of each ward and stored it in 'ward_loc.txt'
4. In 'booze_list.py', I used Google Maps Place API's 'nearbysearch' method to get the nearby liquor stores' place ID(google uses it to identify them) and then 'place details' function to get the the contact, no. of reviews etc information, and finally stored it in 'liquor_stores.txt'

Done!

Moreover, 'google_search.py' contains the basic data mining everyone should know.
