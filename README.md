# Oracle assignment

## Deployment

### **Before runing the app you have to add .env file in app folder**
It's necessary to set up for e-mail sending

To set reciever of mail you have to modify mails in **mock_responses/list_users.json**
```
SENDER_EMAIL = <YOUR MAIL>
SENDER_PASSWORD = <YOUR APP PASSWORD> 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
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

___________
## Description
The app runs as a web application and consists primarily of a button that triggers a validity check and a table that appears once the button is clicked. The table displays user ID, email, and the validity of their key. Each row is colored either red or green depending on the key’s validity.

The entire application can be run in Docker.

Data that couldn’t be retrieved from APIs (since I don't have token) is mocked. The JSON files containing the mocked response data can be found in the **mock_responses** folder.

To send emails, you need to create a `.env` file with the necessary email configuration information (e.g., deployment settings).