import json
from temba_client.v2 import TembaClient
client = TembaClient('https://rapidpro-next.idems.international', '8d85587d8f67eeea194d305f926b4f96841df10e')

for contact_batch in client.get_contacts(group='everyone').iterfetches():
    for contact in (contact_batch):
        c = contact.serialize()
        # Here I'm just print some of the stats from each student.
        # You can see the relevant fields by looking at one of the students in RapidPro: https://rapidpro-next.idems.international/contact/read/2e05e0c3-c90f-4d8f-b711-53c9d2ff361b/
        # Name is the Student's Telegram name; studentname is the name the student gave us during registration
        # print([c.get('name'), c.get('fields').get('studentname'), c.get('fields').get('next_pscl'), c.get('fields').get('open_pscl')])
        print([c.get('name'), c.get('fields').get('studentname'), c.get('fields').get('next_data'),c.get('fields').get('open_data')])
