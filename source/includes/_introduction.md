
# Introduction

Welcome to the BestTime.app documentation! The documentation includes different sections.

* What is BestTime.app (see below)
* [API reference](#api-reference)


## What is BestTime.app?
BestTime.app is a foot traffic data (API) service that forecasts how busy a public business (venues) will be at any given hour of the week. 
The data is provided for 150+ countries using anonymous phone signals, and is available for retail, restaurants, bars, gyms, museums, and more. 
Foot traffic forecasts are based on average visits over the past weeks. 
Busyness for any given hour is predicted relative to the biggest peak of the week for this business. 
The foot traffic data is presented as percentages for each hour of the week from 0% (empty/ closed) to 100% (visitor peak of the week). 

<b>Highly recommended to read:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>

Additional BestTime functionality:
<ul>
<li>Live updates if a venue is more or less busy than normal (real-time).</li>
<li>Foot traffic analyses, like peaks, quiet hours, week overviews</li>
<li>Search venue foot traffic based on category (e.g. supermarkets in London) or name (e.g. McDonalds in San Fransisco).
</li>
<li>
    Filter and sort venues in a whole area based on foot traffic data, dwell time, day, time, and business type, location, and more.
</li>
<li>Integrate all data directly into your applications/ research using the developer REST-API.
</li>
</ul>
You could compare it with a supercharged FourSquare foot traffic data/ Google Popular Times API with more footfall data analytic functionality.


## Use cases
Below are a few example use-cases how the analyzed data can be used in real-world:

- Inform visitors what the best time is to visit a venue.
- Find the most popular hours of a bar nearby. This way you will never end up in an empty bar, and never end up in the queue.
- Find the quietest gym by comparing multiple gyms in your neighborhood.
- Find the best time to go to a museum and avoid the queue.
- Find out of a venue is more crowded than normal at this moment with the live data.
- Create a dashboard for your venue (e.g. reception, kitchen, etc) to keep your employees informed how busy it is now (live), how busy it will be next hour (forecasted), and when the next peak is coming.
- Compare your business with the competitors to find the perfect time to launch a promotion.
- Behavioral research: Get insights on how people behave in certain areas. E.g. in general gyms tend to peak around 7 am and 7 pm, restaurants tend to peak around 1 pm and 9 pm, shops tend to peak around 4 pm.


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
* Malls
* Supermarkets
* Public offices (like customer service points)
* Theme parks

### Results
A forecast is usually created within a few seconds and responds with all primary analyses. Additionally, a forecast is stored on the server so it can be queried later again without the need to forecast the business again.

The forecast results include:

- Relative foot traffic intensity percentage data for every hour of the week.
- Week analysis
    - Peak busyness per day percentage
    - Average busyness (volume) per day percentage
    - Ranking based on the maximum peak of the day
    - Ranking based on the total visitor's volume of the day
- Hour analysis
    - How busy each hour of the day will be (rated from -2 to +2)
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

### Relative numbers

BestTime.app does not provide absolute business visitor numbers. Data in the forecasts represent an approximate how busy a business will be in a relative number. Each hour of the week is rated on a five-point scale from -2 to +2 (Low, below average, average, above average, high). The rating is also depending on the mean busyness of the week.

### Coverage
BestTime.app has coverage in 150+ countries. It depends on multiple factors if a business can be forecasted. A rough guideline is that the business needs to be a public business and has at least 100 visitors per day. 

### Data retention
Forecast will only be stored on the server for a specific number of days. This depends on your subscription plan. Expired forecasts will be automatically deleted. Store a forecast response locally or upgrade your plan to keep using a forecast.

### Updating a forecast
To update an existing business forecast you need to create a new forecast. Currently, only the latest forecast for each business is accessible through the API. It is up to the user to decide how often a forecast needs to be updated, but in general, we recommend to update a forecast every two to four weeks. Live data is the current relative activity for the current hour. It is therefore suggested to update the live data every hour.

## Queries
Forecasting a (new) business takes a few seconds. Normally a forecast is accurate for at least several weeks (depending on the business), therefore the data from existing forecasts can still be used for a longer period. Queries are used to get data from an existing forecasted business. For example the whole forecast, or a specific analysis on a specific day.

A query response is almost instant, includes sometimes additional data, and makes it easier to answer specific questions.

### Recommended usage
Forecasts are based on visits to the business from the past few weeks. We recommend therefore to only forecast (update) a business once every few weeks. Queries should be used in between the forecasts. This reduces API forecast credits and improves the API performance.

### Additional dynamic data
Some query responses include additional dynamic data on top of the stored forecast. 
The peak-, surge-, busy-, quiet analysis query responses include the time remaining until the next event (e.g. 2,5 hours until the first busy hour).

### Query analysis
BestTime.app has several query endpoints:

Venue queries:
- Query the details of a specific venue
- Query all forecasted venues
- Query all venues matching the busyness, location, time & day, and/or type filter

Forecast of a single venue queries:
- Query the whole original forecast (includes all analysis) of a venue
- Query a specific day of the week (includes all analysis)
- Query a specific hour of the day 
- Query the current hour of the business with the local business timezone taken into account (or X hours ahead from the current hour)
- Query the busy hours of today (or X days ahead from today)
- Query the quiet hours of today (or X days ahead from today)
- Query the peak hours of today (or X days ahead from today)
- Query the surge hours of today (or X days ahead from today)


## Forecast day window and weekdays
BestTime.app uses 24-hour notation, displayed from `0` to `23`. Where `0` indicates midnight and `23` indicates 11 pm. 
To make forecasts more useful in real-life the window for one day has been set from 6 am until 5 am next day. This is for example useful for public venues with late opening times like bars and nightclubs. If you query for example the data for a Monday. The result includes the hours for Monday 6 am until Tuesday 5 am.