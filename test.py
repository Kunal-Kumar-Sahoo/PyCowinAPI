import cowin_api.api as API
from pprint import pprint

obj = API.CoWinAPI()

state_dict = obj.get_states()['states']
print("State ID | State Name")
for i in state_dict:
    print(i['state_id'], i['state_name'], sep=' | ')

state_id = input("Enter your state ID: ")
dist_dict = obj.get_districts(state_id)['districts']
print("District ID | District Name")
for i in dist_dict:
    print(i['district_id'], i['district_name'], sep=' | ')

district_id = input("Enter your district ID: ")
min_age = "18"
avail = obj.get_availability_by_district(district_id, min_age)
centers = avail['centers']
pprint(centers)

for i in centers:
    print(f"Name: {i['name']}")
    print(f"Address: {i['address']}")
    print(f"District Name: {i['district_name']}")
    print(f"Pin Code: {i['pincode']}")
    print(f"Timings: {i['from']} to {i['to']}")
    print(f"Fee Type: {i['fee_type']}")
    for j in i['sessions']:
        print(f"Minimum age limit: {j['min_age_limit']}")
        print(f"Vaccine name: {j['vaccine']}")
        print(f"Time Slots: {j['slots']}")
    print("\n\n")

