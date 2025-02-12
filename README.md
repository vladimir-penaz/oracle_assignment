# Oracle assignment


### **Before runing the app you have to add your .env file in app folder**

```
SENDER_EMAIL = <YOUR MAIL>
SENDER_PASSWORD = <YOUR APP PASSWORD> 
```

### **To run the code just execute the commands:**

Build the image:
```
docker build -t flask-app .
```

Run the container:
```
docker run -p 5000:5000 flask-app
```
Then your can accer the app on folowing address
http://127.0.0.1:5000/


___________

If the port 5000 is already in use, you can use different like that (fe: I used 5003):
```
docker run -p 5003:5000 flask-app
```
In this case the address is http://127.0.0.1:5003/