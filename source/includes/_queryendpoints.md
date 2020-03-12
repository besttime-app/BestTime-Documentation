# Query endpoints

All query endpoints are used to retrieve all data or specific analysis from an existing forecast.
The `venue_id` is the primary parameter to query an existing forecast.

Query endpoints:  

**Venues**
Query all previously forecasted venues, including venue details.  

**Week**
Query the forecast for the whole week, including all analysis. This gives the same response as the original 'new forecast' endpoint.  

**Day**
Query a specific day of the week including all analysis.  

**Hour**
Query a specific hour of the day.  

**Current Hour**
Query the current hour of the business with the local business timezone taken into account.  

**Peak Hours**
Query the peak hours of today. Peaks will also include peak start, end times, and how intense the peak will be.

**Busy Hours**
Query the busy hours of today.  

**Quiet Hours**
Query the quiet hours of today.  

**Surge Hours**
Query the surge hours of today. Surge analysis shows when most people come to a venue, or leave the venue.  
