from firebase_admin import firestore
import firebase_admin
import time
from firebase_admin import credentials
#from gpiozero import MotionSensor
#from picamera import PiCamera

#GLOBAL VARIABLES
PATH_TO_SERVICEACCOUNTKEY="WatchDog\watchdog-4475a-firebase-adminsdk-rue2z-bd330db374.json"
PIRSENSOR_PIN=4


# def detectMotion():
#     pir = MotionSensor(PIRSENSOR_PIN)
#     camera = PiCamera()
#     try:
#         while True:
#             pir.wait_for_motion()
#             camera.capture()
#             print("Motion detected!")
#             time.sleep(10)
            
#     except Exception:
#         camera.close()



def firebaseAuthentication():
    cred = credentials.Certificate(PATH_TO_SERVICEACCOUNTKEY)
    firebase_admin.initialize_app(cred)

def sendNotification():
    db=firestore.client()
    home=db.collection('home').document()
    home.set({
        'time':firestore.firestore.SERVER_TIMESTAMP
    })

    
if __name__=="__main__":
    firebaseAuthentication()
    sendNotification()
    
