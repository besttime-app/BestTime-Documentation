# Query endpoints

All query endpoints are used to retrieve all data or specific analysis from an existing forecast.
The `venue_id` is the primary parameter to query an existing forecast.

Query endpoints:  
- Query the whole **week** (original forecast includes all analysis)  
- Query a specific **day** of the week (includes all analysis)  
- Query a specific **hour** of the day  
- Query the **current hour** of the business with the local business timezone taken into account (or X hours ahead from the current hour)  
- Query the **peak hours** of today (or X days ahead from today)  
- Query the **busy hours** of today (or X days ahead from today)  
- Query the **quiet hours** of today (or X days ahead from today)  
- Query the **surge hours** of today (or X days ahead from today)  


## Query all venues

[{
        "epoch_analysis": 1583911633,
        "updated_on": "Wed, 11 Mar 2020 07:27:14 GMT",
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_forecasted": true,
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_lat": 37.7235448,
        "venue_lng": -122.455458,
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles",
        "venue_week_rank_max": [
            5,
            5,
            1,
            3,
            7,
            6,
            2
        ],
        "venue_week_rank_mean": [
            5,
            4,
            2,
            2,
            3,
            6,
            7
        ]
    }
]