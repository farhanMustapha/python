import firebase_admin


firebaseConfig={
     "apiKey": "AIzaSyDTyEj6a0tRA_zKBrHmWS3PXJJ5bFydbIY",
     "authDomain": "demo1-4b88c.firebaseapp.com",
     "projectId": "demo1-4b88c",
     "storageBucket": "demo1-4b88c.appspot.com",
     "messagingSenderId": "184645083218",
     "appId": "1:184645083218:web:fb0f9723d1f6124576ff8b"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

#push data
data={"name":"john","age":30,"adress":["new york","los angeles"]}
db.push(data)