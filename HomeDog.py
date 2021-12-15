from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

#GLOBAL VARIABLES
PATH_TO_SERVICEACCOUNTKEY="watchdog-4475a-firebase-adminsdk-rue2z-bd330db374.json"
PIR_PIN=4

#firestore.firestore.SERVER_TIMESTAMP

def firebase_authentication(PATH_TO_SERVICEACCOUNTKEY):
    cred = credentials.Certificate(PATH_TO_SERVICEACCOUNTKEY)
    firebase_admin.initialize_app(cred)

if __name__=="__main__":
    firebase_authentication(PATH_TO_SERVICEACCOUNTKEY)
    
