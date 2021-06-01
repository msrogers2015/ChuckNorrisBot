# Chuck Norris Bot
This is a text bot created using [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Twilio](https://www.twilio.com/) and the [Chuck Norris API](https://api.chucknorris.io/). Official number for this project is 3612-NORRIS (361-266-7747) if you want to try it out

***

# Getting Started
Things you will need to do before getting started:
* TWilio account and number
* Pythonanywhere account or some form of web hosting for python applications

Here is a the [guide](https://pythonhow.com/deploy-flask-web-app-pythonanywhere/#:~:text=Make%20sure%20you%20have%20signed,to%20accept%20the%20project%20path.) I used to set up my Flask application and get it online. There are a few things that aren't covered in here that I personally changed but not completely sure if it was needed (this is my first Flask app). Make sure that you install the requirements.txt into your virtual enviornment. It has all the goodies to make the bot run :)

Once you create your Flask app, replace everything in the 'flask_app.py' file with the code from this repo. And thats it for programming! Now you'll need to get a Twilio number and set up the webhooks. After creating a Twilio account, [buy a number](https://www.twilio.com/console/phone-numbers/search) to use for your text bot. Once you have purchased a number, navigate to your active numbers and click on the one you just purchased. At the very bottom you'll need to set up your webhook. Under "A MESSAGE COMES IN", type your pythonanywhere url (formatted as such: <username>.pythonanywhere.com). If you want, create a 'PRIMARY HANDLER FAILS' TwiML to let users know something went wrong. And thats it!
  
  ***
  # Extras
  So I meantioned that I changed a few things. On pythonanywhere in the web tab, there is a section labeled code. For the source code, I updated the path to be the flask_app.py file so its "/home/<username>/mysite/flask_app.py". I also enabled Force HTTPS.
