# from firebase_admin import firebase
# firebase = firebase.FirebaseApplication('https://businesssiteb20-default-rtdb.firebaseio.com/', None)
# data =  { 'Name': 'John Doe',
#         'RollNo': 3,
#         'Percentage': 70.02
#         }
# result = firebase.post('/python-example-f6d0b/Students/',data)
# print(result)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('businesssiteb20-firebase-adminsdk-d36qa-7ca63ab8bb.json')

# Initialize the app with a service account, granting admin privileges
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://businesssiteb20-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('contactus')

users_ref = ref.child('users')
users_ref.update({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'galuk': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})

#print(ref.get())