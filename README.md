# google-maps-api-data-mining
A self project.

Problem Statement: Return a list of all the liquor stores in Bangalore.

Steps to solve it:
1. Got the list of all the wards in B'lore from Wikipedia, stored it in 'input_data.txt'.
2. Coded 'get_wards.py' to generate a clean list of wards in 'wards_list.txt'
3. In 'locate_ward.py', I used 'geopy' to get the location(latitude, longitude) of each ward and stored it in 'ward_loc.txt'
4. In 'booze_list.py', I used Google Maps Place API's 'nearbysearch' method to get the nearby liquor stores' place ID(google uses it to identify them) and then 'place details' function to get the the contact, no. of reviews etc information, and finally stored it in 'liquor_stores.txt'
