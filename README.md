# Django Crypto Prices App

<!-- Live Demo can be viewed at https://www.buildproshop.com/ -->

<img src="static\images\prices_page.png">

***
## Description

The web app, built on `Django` and utilizing `HTML`, `CSS`, and the `Binance API`, provides users with real-time cryptocurrency data. With this tool, users can instantly access current cryptocurrency prices, securely log in to access personalized favorite lists, register new accounts, like and monitor preferred cryptocurrencies. Additionally, users can explore the [Telegram Crypto Bot](https://t.me/currency_nllllibeth_bot) project and try it out.


***

## Installation Guide

#### Local Setup
> The setup given here is for a linux environment (Debian/Ubuntu)

- Clone to the local machine 

        $ git clone https://github.com/
        $ cd crypto_prices

- Create and activate virtual environment 

        $ python3 -m venv venv
        $ source venv/bin/activate

- Install dependencies 

        $ pip3 install -U -r requirements.txt


#### Environment Variables

For proper running the app set your own environment variables, that may contain sensetive and secret data from the list below

- `API_KEY` - Get your api key from [Binance API](https://www.binance.com/en/binance-api)
- `SECRET_KEY` - With api key from [Binance API](https://www.binance.com/en/binance-api) you will be provided with a secret key

#### Run app
        $ python3 manage.py runserver
After this command go to the localhost and use the features of the app. 

*** 

## Features 

- `Get cryptocurrencies prices` - Stay informed about current prices for various symbols, including price changes over the past 24 hours
- `Get cryptocurrency info` - Access detailed information about selected symbols, including current, lowest, highest, and open prices
- `Log In / Sign Up` - Log In in the existing account or create a new one   
- `Like a currency` - Add a currency to a favourite list
- `Try crypto bot` - Read about and try out the cryptocurrency bot in Telegram 

***

## Demo Pages 
#### Home Page
<img src="static\images\home_page.png">

#### Single Currency Page
<img src="static\images\single_currency.png">

#### Likes and Favourite List
<img src="static\images\like_page.png">
<img src="static\images\favourite_list_page.png">

#### Login and Signup Pages
<img src="static\images\login_page.png">
<img src="static\images\signup_page.png">

#### Subscription Page
<img src="static\images\subscription_page3.png">

***
## Contact 

You can contact me [@nllllibeth](https://t.me/nllllibeth)
