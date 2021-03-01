# Cryptocurrency_App

This is a simple web app that fetch the real-time price for the top 20 cryptocurrencies on the market. 
It will show the change in price that has happened in the past hour, 24 hours, and week.
It will also pull up a historical chart.

------
### Server side
The API was made with Flask. The (/<cryptocurrency's name>) endpoint will take you to see the historical chart for
the currency chosen. 


The information is queried from two different data-providers (CoinMarket and CoinGecko). The CoinMarket API
was used to get the top 20 cryptocurrencies out there currently. CoinGecko API was used to get the historical
charts for the 20 currencies.

The web app is deployed on Heroku.

------
### Client Side
The client side was made with HTML and Jinja. It is a dynamic web page so if there is any
movement from the currencies in terms of market size, the web page should be able to pick
it up and change it accordingly.
