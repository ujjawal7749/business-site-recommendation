import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import string
import random
from datetime import datetime,date
# def savetocsv(name,email,message):

#     fields = [name, email, message] 
    
#     with open('contactus.csv', 'a') as f:
#         write = csv.writer(f)
#         write.writerow(fields)

def saver1(name,email,message):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) + "-"+str(date.today().strftime("%b-%d-%Y")+datetime.now().strftime("-%H-%M-%S"))
    # Fetch the service account key JSON file contents
    if not firebase_admin._apps:
        cred = credentials.Certificate('businesssiteb20-firebase-adminsdk-d36qa-7ca63ab8bb.json')
        default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://businesssiteb20-default-rtdb.firebaseio.com/'})

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference('contactus')

    users_ref = ref.child('users')
    users_ref.update({
        res: {
            'name':name,
            'email': email,
            'message': message
        }
    })
