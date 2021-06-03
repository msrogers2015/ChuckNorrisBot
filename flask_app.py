# Imports
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

# Create the Flask application
app = Flask(__name__)
status_error = "Sorry, couldn't fetch a joke. Try again later"

# All of the accepted categories from the api
categories = ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]

# The main page. The decorator does some fancy stuff that creates your url( still learning)
@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body','').lower()

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message

    # Get a random joke
    if body[:6] == 'random':
        r = requests.get('https://api.chucknorris.io/jokes/random')
        chuck = r.json()
        joke = chuck['value']
        if r.status_code == 200:
            resp.message(joke)
        else:
            resp.message(status_error)
    # Get a random joke from a category
    elif body[:8] == 'category':
        global categories
        body_parse = body.split(' ')
        category = body_parse[1].lower()
        resp.message(category)
        if  category in categories:
            r = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
            chuck = r.json()
            joke = chuck['value']
            if r.status_code == 200:
                resp.message(joke)
            else:
                resp.message(status_error)

    # Messaging options
    elif body[:7] == 'options':
        resp.message("Text 'categories' for a list of accepted categories. Text 'random' for a random joke. Text 'category'  followed by a category to get a random joke.")
    # Get the accpeted catories
    elif body[:10] == 'categories':
        cat = ''
        for i in categories:
            cat += i + ', '
        resp.message(cat)
    else:
        resp.message("Sorry, couldn't find that command. Text 'options' for more help")


    return str(resp)
