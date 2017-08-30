import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("UofTFoodBotData").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

def find_restaurant(requestedname):
    i = 0
    list_of_reviews = []
    review_string = ""
    end_result = ""
    while i < len(list_of_hashes):
        curr_restaurant = list_of_hashes[i]
        restaurant_name = curr_restaurant['Name']
        if requestedname.lower() == restaurant_name.lower():
            print("restaurant found")
            review_string =  "Name: " + list_of_hashes[i]['Name'] + "\n \n Price: " + list_of_hashes[i]['Price'] + "\n \n Rating: " + list_of_hashes[i]['Rating'] + "\n \n Comment: " + list_of_hashes[i]['Comments'] +  "\n \n Username: " + list_of_hashes[i]['Reddit Username']
            list_of_reviews.append(review_string)
        i += 1
    for review in list_of_reviews:
        end_result += review + "\n \n" + "-----" + "\n \n"
    return end_result


def list_restaurants():
    my_list = []
    i = 0
    while i < len(list_of_hashes):
        curr_restaurant = list_of_hashes[i]
        my_list.append(curr_restaurant['Name'])
        i += 1
    return my_list

