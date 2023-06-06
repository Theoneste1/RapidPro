import requests
import json

# The last part of the URL indicates what you are requesting.
# See: https://rapidpro-next.idems.international/api/v2/explorer/
url = 'https://rapidpro-next.idems.international/api/v2/contacts.json'
# This is the API token for the workspace.
# To get this, log into RapidPro, select the workspace the bot is in (in this case RwandaNabojBot),
# and find the token there: https://rapidpro-next.idems.international/org/home/
auth = '8d85587d8f67eeea194d305f926b4f96841df10e'
headers = {'Authorization': f'Token {auth}'}
# Depending on what information you want, you may need to send some extra information with the request.
# What exactly, see https://rapidpro-next.idems.international/api/v2/explorer/
data = {
    "groups": ["everyone"],
}

x = requests.get(url, headers=headers, json=data)


# This is just for testing. Ideally, you compile the relevant bits of this information into a spreadsheet
print(json.dumps(json.loads(x.text), indent=4))

# A response looks like this, containing information from each user who has interacted with the bot,
# including how far they have progressed through the different themes.
# For example:
#                 "next_pscl": "5",
#                 "open_pscl": "4 3 2 1",
# means that the open question in PSCL are 1, 2, 3 and 4, and the next question that would get unlocked
# when successfully solving a question is 5. So in this case, the first 4 questions are open, and the student
# hasn't solved any questions in the topic PSCL.
# 
# Note that each response only contains 50 entries.
# The response contains a "next" URL. You should send another request to that URL to get the next 50 entries.
# Write a while loop that keeps doing that until you get all entries (until next == None/null).
# {
#     "next": "https://rapidpro-next.idems.international/api/v2/contacts.json?cursor=cD0yMDIzLTA0LTE0KzE5JTNBNTMlM0EwMi4zNDQ0NzAlMkIwMCUzQTAw",
#     "previous": null,
#     "results": [
#         {
#             "uuid": "db888a38-ebb2-49a5-b604-495f06c9d529",
#             "name": "Ephrem Dushimimana",
#             "language": null,
#             "urns": [
#                 "telegram:6202585454#soulmate250"
#             ],
#             "groups": [
#                 {
#                     "uuid": "b66023f2-acfd-4a46-a07b-80ba207d8c43",
#                     "name": "everyone"
#                 }
#             ],
#             "fields": {
#                 "level": "S2",
#                 "sector": "Shangasha",
#                 "gender": "Male",
#                 "district": "Gicumbi",
#                 "studentname": "Ephrem Dushimimana",
#                 "schoolname": "Gs Shangasha",
#                 "next_pscl": "5",
#                 "open_pscl": "4 3 2 1",
#                 ...
#             },
#             "flow": null,
#             "blocked": false,
#             "stopped": false,
#             "created_on": "2023-04-04T06:32:22.119492Z",
#             "modified_on": "2023-05-31T16:24:19.493297Z",
#             "last_seen_on": "2023-05-31T16:24:19.457411Z"
#         },
#         ...