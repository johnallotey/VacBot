**Travel Chatbot**

This project creates a travel chatbot which can provide users with request basic flight information including prices, hotel availability and car rentals.


**Prerequsite**

All files would require you install the requirements in requirement.txt and package.json. In addition you would have to set up an account on Dialogflow. You can alternatively log-in with your email if you already have an existing account on the google cloud. 

You can use the npm to initialize for the project with this command:

    npm init-y

Next, copy and paste the contents in the package.json folder into the newly created package.json folder.

Now, use pip to install the package dependencies required for the project from the requirements.txt document:

    pip3 install -r requirements.txt

**Description**

By default, the chatbot goes by its default name ['Dialog Flow Bot'] to respond to users requests. Our chatbot uses Dialog flow for NLU, Slack as an interface and Amadeus as an external fulfillment API to query information based on user requests.

Attached to this repo are intent and entity files needed to build the asisstant on the cloud platform.

**Demo**

You can run this project for yourself after cloned the repo and installing the project requirements with:

    python3 TravelBot/travel.py

**NB**

This is an ongoing project as of April 2020. Thus there would be monthly updates on the repo
