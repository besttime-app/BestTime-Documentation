
# Introduction

Welcome to the BestTime.app documentation! The documentation includes different sections.

* What is BestTime.app (see below)
* [API reference](#api-reference)


## What is BestTime.app?

BestTime.app is a web (API) service that forecasts how busy a public business (e.g. restaurant, gym, etc) will be at any given hour of the week. Forecasts are based on average visits over the past weeks. Busyness for any given hour is predicted relative to the biggest peak of the week for this business.

Besides hour forecasts, additional analysis are included. For example: the peak hours of the day, if it is now more busy than normal compared to the average, and a ranking of the most busy days of the week.

Once a business has been forecasted additional queries can be made on the forecast. For example: When is today's next peak? When will it be quiet on Saturday? How busy will it be next hour? 


<aside class="notice">
In the documentation and the API the word 'venue' is used to indicate a public business. Therefore the word 'venue' and 'business' will be used interchangable.
</aside>

## Forecasts

A forecast can be made by giving the name and the approximate address of the public business. BestTime.app will try to find the correct business. If there is enough data available it will analyse the data and create a forecast. 

### Public businesses
BestTime.app works in general only for public businesses. For example:

* Restaurants
* Bars
* Gyms
* Shops
* Museums
* Theatres
* Public offices (like customer service points)
* Theme parks

### Results
A forecast is usually created within a few seconds and responds with all primary analysis. Additionally a forecast is stored on the server so it can be queried later again without the need to forecast the business again.

The forecast results include:

- Week analyis with a ranking of most busy days of the week
    - Ranking based on the maximum peak of the day
    - Ranking based on the total visitors volume of the day
- Hour analysis
    - How busy each our of the day will be (rated from -2 to +2)
- Peak analysis
    - Start time of the peak
    - Time of the peak (maximum)
    - End time of the peak
    - Peak intensity (rated from 1 to 5)
- Surge analysis
    - What time are most people going to the business 
    - What time are most people leaving the business
- Busy hours
    - List of all busy hours per day.
- Quiet hours
    - List of all quiet hours per day.

- Live analysis (Only for selected subscription plans)
    - How much more or less busy is this business now (live) compared to the historical average for this hour and day.

### Relative numbers

BestTime.app does not provide absolute business visitor numbers. Data in the forecasts represent an approximate how busy a business will be in a relative number. Each hour of the week is rated on a five point scale from -2 to +2 (Low, below average, average, above average, high). The rating is also depending on the mean busyness of the week.

### Coverage
BestTime.app has world wide coverage,but it depends on multiple factors if a business can be forecasted. A rough guideline is that the business needs to be a public  business and has at least 100 visitors per day. Only when a business can be forecasted credits will be subtracted from your account.

### Data retention
Forecast will only be stored on the server for a specific amount of days. This depends on your subscription plan. Expired forecasts will be automatically deleted. Store a forecast response locally or upgrade your plan to keep using a forecast.

### Updating a forecast
In order to update an existing business forecast you need to create a new forecast. Currently only the latest forecast of each business is accessible through the API. It is up to the user to decide how often a forecast needs to be updated, but in general we recommend to update a forecast every two to four weeks. 

## Queries
Forecasting a (new) business takes a few seconds. Normally a forecast is accurate for at least several weeks (depending on the business), therefore the data from existing forecasts can still be used for a longer period of time. Queries are used to get data from an existing forecasted business. For example the whole forecast, or a specific analysis on a specific day.

A query response is almost instant, includes sometimes additional data, and makes it easier to answer specific questions.

### Recommended usage
Forecasts are based on visits to the business from the past few weeks. We recommend therefore to only forecast (update) a business once every few weeks. Queries should be used in between the forecasts. This reduces API forecast credits and improves the API performance.

### Additional dynamic data
Some queries responses include additional dynamic data on top of the stored forecast. 
The peak-, surge-, busy-, quiet analysis query response include the time remaining until the next event (e.g. 2,5 hours until the first busy hour).

### Query analysis
BestTime.app has several query endpoints:

- Query the whole original forecast (includes all analysis)
- Query a specific day of the week (includes all analysis)
- Query a specific hour of the day 
- Query the current hour of the business with the local business timezone taken into account (or X hours ahead from current hour)
- Query the busy hours of today (or X days ahead from today)
- Query the quiet hours of today (or X days ahead from today)
- Query the peak hours of today (or X days ahead from today)
- Query the surge hours of today (or X days ahead from today)


## Use cases
A few examples how the analysed data can be used in real world:

- Find the most popular hours of a bar using the peak analysis. This way you will never end up in an empty bar, and never end up in the queue.
- Find the most quiet gym by comparing multiple gyms in your neighbourhood.
- Find the best time to go to a museum and avoid the queue.
- Compare your business with the competitors to find the perfect time to launch an event.


## Forecast day window and weekdays
TODO
BestTime.app uses 24 hour notation, displayed from `0` to `23`. Where `0` indicates mightnight and `23` indicates 11PM. In real-life 
Explain day window ranges from 6am till 5am (`hour=6` till `hour=5`). 
Normal day goes from midnight `hour=0` to 
besttime.app does only work weekdays instead of days.
explain 3am is not notated as next day/