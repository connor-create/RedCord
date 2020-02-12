import json
import firebase_admin
from firebase_admin import credentials, firestore


class Database:
    def __init__(self):
        cred = credentials.Certificate('./ServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(cred)
        self.client = firestore.client()

    def add(self, serverID, channelID, rate, subreddits):
        # need to check for a pre-existing entry for the server and channel
        newEntry = False
        doc_ref = self.client.collection(rate).document(serverID)
        if doc_ref.get().to_dict() == None:
            newEntry = True
            self.client.collection(rate).add(document_id = str(serverID), document_data = {'channelID':str(channelID)})
            doc_ref = self.client.collection(rate).document(serverID)
        nextSub = len(doc_ref.get().to_dict())+1
        if newEntry:
            nextSub -= 1
        for sub in subreddits:
            fieldUpdates = {
                    str(nextSub): sub,
            }
            doc_ref.update(fieldUpdates)
            nextSub+=1

    def set_amount(self, serverID, rate, amount):


    def remove(self, serverID, channelID, rate, subreddits):
        indexList = []
        doc_ref = self.client.collection(rate).document(serverID)
        doc_dict = doc_ref.get().to_dict()
        if doc_dict == None:
            print("already solved")
        print(doc_dict)
        for index, subStored in doc_dict.items():
            for sub in subreddits:
                if sub == subStored:
                    indexList.append(index)
        for item in indexList:
            doc_ref.update({item: firestore.DELETE_FIELD,})

    def remove_all(self, serverID, rate):
        doc_ref = self.client.collection(rate).document(str(serverID))
        doc_ref.delete()
