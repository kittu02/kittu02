
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/kirtan/helmet-d508c-firebase-adminsdk-fbsvc-e149af3635.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to handle real-time updates
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f"New Data Received: {doc.id} => {doc.to_dict()}")
print("-------------------------------------")
# Set up real-time listener on the "devices" collection
doc_ref = db.collection("locations").document("A1m2c4n8R")
doc_ref.on_snapshot(on_snapshot)

print("Listening for real-time updates... Press Ctrl+C to stop.")

# Keep the script running
import time
while True:
    time.sleep(1)
