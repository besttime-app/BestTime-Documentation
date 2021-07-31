# Query endpoints

All query endpoints are used to retrieve all data or specific analysis from an existing forecast. Query endpoints often also include dynamic information (e.g. remaining time until it will be busy according to the forecast).
The `venue_id` is the primary parameter to query an existing forecast. 

It is also possible to update a venue forecast in combination with the query in one API call. This way you can retrieve query-specific data:
-  with a fresh forecast
- don't having to worry about the retention days (maximum days a forecast is stored on the server)
- use the venue name and address as API input instead of the venue_id

Check the query endpoint itself for more information. This will be counted as new forecast credit.


Query endpoints:  

**Venues**
Lists all previously forecasted venues, and venue_id's.

**Venues filtered (Radar tool)**
Query earlier forecasted venues that match the filter on busyness, location, time, day and venue type.

**Venue**
Query a forecasted venue, with detailed venue information.  

**Week**
Query the forecast for the whole week, including all analysis. This gives the same response as the original 'new forecast' endpoint.  

**Week raw**
Query the forecast for the whole week, in raw percentages. 

**Week overview**
Qeury a week overview for the venue. Including day maximum, day mean, day maximum ranking, day mean ranking, and open/closing times.

**Day**
Query a specific day of the week including all analysis.  

**Day raw**
Query the forecast for a specific day of the week, in raw percentages. 

**Hour**
Query a specific hour of the day.  

**Hour raw**
Query the forecast for a specific day and hour of the week, in raw percentages.  

**Now**
Query the current hour of the business with the local business timezone taken into account. 

**Now raw**
Query the current hour of the business with the local business timezone taken into account, in raw percentages. 

**Peak Hours**
Query the peak hours of today. Peaks will also include peak start, end times, and how intense the peak will be.

**Busy Hours**
Query the busy hours of today.  

**Quiet Hours**
Query the quiet hours of today.  

**Surge Hours**
Query the surge hours of today. Surge analysis shows when most people come to a venue, or leave the venue.  

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>