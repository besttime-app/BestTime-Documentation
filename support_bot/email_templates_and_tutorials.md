<EMAIL TEMPLATES and tutorials>

# Customer Email Templates

This document contains email templates that can be used to inform and answer questions related to BestTime.app

## General BestTime Foot Traffic Info

What kind of foot traffic data is available?
BestTime only offers foot traffic data for public venues. This includes bars, restaurants, cafes, supermarkets, malls, parks, beaches, museums, popular sightseeing attractions, and other public places. BestTime only offers relative foot traffic data, and no absolute visitor numbers This means that the data is relative to the visitor peak of the week. For example, if a venue has a peak of 100% on a Friday, and a value of 50% on a Monday, this means that the venue is half as busy on a Monday compared to a Friday.

Where do you get the data from?
The data is based on anonymized smartphone GPS signals. Third-party mobile apps collect the data from users who opt-in. The data is aggregated and normalized directly. We don't collect personal data, not even anonymized personal identification numbers. Consequently, we can't link any of our internal data with a single person.

What is a foot traffic forecast?
A foot traffic forecasts is based on visitor patterns from the past few weeks in a venue. The data is used to forecast foot traffic by hour throughout the week. Forecast values are displayed as percentages, ranging from 0 to 100%. The percentage indicates how busy a venue approximately is relative to its peak of the week. See 'live data' for a more accurate real-time value. The forecast result also includes different analysis, e.g.:

- Most busy days of the week (maximum, and mean)
- Daily peak hours, start, end, and intensity of the peaks
- What time most visitors come and leave the venue
- The quietest hours of the day

What is live foot traffic data?
Live data indicates the real-time foot traffic activity of a venue - expressed as a percentage - for the current hour of the day. When the live value is similar to the forecast value, it is busy as usual. The venue is busier than usual when the live value exceeds the forecasted value. The live values can also exceed 100%. A live value of 150%, for instance, indicates that it is approximately 50% busier compared to the forecasted peak of the week for that venue.

Does it work on all venues?
No. Venues need enough foot traffic (visitors) to make accurate forecasts. This volume needs to be even higher for real-time live data. The venue will become automatically available on BestTime when the foot traffic level is high enough. Foot traffic forecast data can be accessed 24/7, if available. When available, live data will only be shown during opening hours of the venue. At the moment, we do not add missing venues manually to our platform. You can use our free demo to see if we have data available for your desired venues.

## Foot Traffic Data Accuracy

The foot traffic data is not always 100% accurate. The foot traffic patterns are calculated using a ‘sample' from the 'total population’ using mobile/ GPS data (when talking from a mathematical statistical perspective). Or in other words: we measure only a small number of visitors from the total number of visitors in a building. Therefore, we cannot give absolute visitor numbers in a venue. If the sample size is big enough, we can provide relative foot traffic (percentages) for every hour of the week.
If the sample size is not big enough, we just don’t provide any data (we want to keep the quality high). The API will then also mention this (something like ‘the venue is found, but not enough data is available at this moment’). Using our online demo, you can test out if your desired venues have enough data.

When we do provide the data, the patterns are usually a very good indication of the visitor flow throughout the week. We usually try to compare our data to the Google Maps data. If you compare the data yourself, you will see that our data is slightly different, but is usually not more than 5% off.

This Google data is of course also not always perfect. A second factor that occasionally impacts the foot traffic data for a venue is a sudden large number of visitors in nearby areas of a venue. The visitor sample size is counted within the geographic boundaries of a venue. Mobile phone GPS accuracy is usually within a few meters. Sometimes mobile GPS devices still have an offset, that makes it look like a visitor is outside or in another nearby venue. Most unreliable data/ outliers do get filtered (e.g. GPS positions that jump around quickly).

With the above in mind, you can imagine that big event in a nearby venue or street could skew the data a little bit.
To partially solve this, the forecast foot traffic data per hour is averaged using the visitor patterns in the past few weeks.
Some venues also have live data that is updated every hour. It is also displayed as a percentage and shows how busy it is in the current clock hour compared to the forecast. So if the foot traffic forecast indicates 60%, while the live data indicates e.g. 120%, it is currently 60% busier than usual.

I’m now talking mostly about the downsides of this technology, but most of our customers are happy with the data. We started 2,5 years ago, and we have several customers who have been using the API nonstop for almost 2 years already.

## Foot Traffic Data Source

I understand your reason to ask this, Sometimes the public/ press can be critical about the privacy of the data.
For competitive reasons we usually don’t provide the exact third party apps we are using for the data source.

## Foot Traffic Live data

A foot traffic forecasts is based on visitor patterns from the past few weeks to a venue. The foot traffic data from BestTime based on anonymized smartphone GPS signals. Third-party mobile apps collect the data from users who opt-in. The data is aggregated and normalized directly. This data is only a sample of the total number of visitors (not all visitors have this tracking enabled). BestTime can therefore not give an absolute number of visitors. However, a sample is enough to accurately provide relative foot traffic data as percentages. The foot traffic forecast is given for each hour of the week from 0 to 100%, wherein 100% is the peak hour of the week. BestTime can therefore accurately forecast that a certain hour of the week is probably going to be the busiest hour/ day of the week, but BestTime cannot tell you how many people will be there.

Also not every venue has foot traffic data available. This is very dynamic so we cannot predict which venues have it. In general the more popular places are available. You can also use the demo on our website to see if the venues you like have foot traffic data available.

The live foot traffic percentage is based on the sample of visitors in the current hour in a venue and compared to the foot traffic forecast for this hour. Based on sample data in the previous weeks, BestTime could for example predict that there will be 60% foot traffic at Thursday 8 PM. If the Live feature detects that the sample of visitors is higher for this hour - compared to the historical visits in the past few weeks on this hour - it gives a higher foot traffic percentage (for example 80% - meaning it is 20% more busy than normal).


# Pricing
<INSTRUCTIONS>
Suggest the likely cheapest subscription plan based on the user query/ use-case. However after discussing the option give a conclusion on which plan is the best fit. So if a package subscription is cheaper, suggest it first. Skip the Basic Metered if it is more expensive than the Pro Metered. Always show the Basic package as comparison and how much the user would save versus the Pro package (but explain the pro package has live data)
</INSTRUCTIONS>

BestTime has two categories of subscription plans:
Metered plans (pay per API requests/ flexible pricing per month)
Package plans (a fixed price per month, with foot traffic for a fixed number of venues per calendar month)
On our pricing page, you can find the prices for each plan:


You have to take API credits into account if you subscribe to a Metered plan (Basic or Pro metered). This is different for each API endpoint.

Using the table on this page you can see how many credits are billed for each API request.
When choosing the Basic Metered plan you can calculate your monthly price by multiplying the total number of credits times $0.04. (e.g. 1000 API credits * $0.04 = $40 USD. (The minimum costs per month is $29 USD) This plan is useful with a low amount of API credits to test the BestTime service.
With higher volumes, we recommend using the Pro Metered subscription. The number of credits used stays the same, but the cost per API credit is much lower with higher volumes:

$0.009 / API credit

$0.006 > 10 K / API credit

$0.0001 > 100 K / API credit

-

$99.00/ month (Additionally, on top of the credits for the Pro metered plan)

So when you for example use 11K API credits/month you will pay: $0.009 * 10K + 1K * $0.006 + $99 = 195 USD. The more API credits used the higher the discount.

The Pro & Basic Package plans with fixed monthly prices have the benefit that you don’t have to think about API credits anymore. With all packaged plans you can refresh the foot traffic forecast data as much as you want. The Pro Packages also include unlimited Live data.

The packaged plans also have improved worldwide caching. This will help improve your app performance when a lot of users are requesting the same data over and over again. We use Cloudflare’s 270+ worldwide datacenters to temporarily store the data close to the user's location.

There are currently 8 different ‘Pro Package’ subscriptions and 3 different ‘Basic Package’ subscriptions. Each option has a maximum number of unique venues per calendar month.

You can also choose one of the metered plans and add a caching system yourself to reduce the number of API credits used.

For more information, please visit our pricing page: <https://besttime.app/subscription/pricing>

Free accounts include a limited amount of API credits that do not renew monthly. It is useful to test the API and get an overview of the data.
When you are planning to build a bigger project, we recommend to subscribe to one of the packaged plans to keep the monthly pricing predictable.
The package plans are great when integrating and testing the BestTime API into your new project and make a lot of repetitive requests.

# Package plans (fixed price per month)

Basic package plans are useful for bigger projects with a lot of venues, however they do not include live data.

## Basic - Package Max 10K unique venues / month

===

-10M Venue foot traffic - by filter
-Unlimited * Venue foot traffic - by ID
-10000 Venue foot traffic - by name
-Venue live data not included in package
-Search venues - by query (Fast) - not included
-10000 Search venues - by query (Normal) included
-CDN caching included
$299.00 / month
===

## Basic - Package Max 100K unique venues / month
===

- 100M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 100000 Venue foot traffic - by name
- Venue live data not included in package
- Search venues - by query (Fast) - not included
- 50000 Search venues - by query (Normal) included
- Search venues - by query (Normal)
- CDN caching

$999 / month
===

## Basic - Package - Max 1M unique venues / month

===

- 500M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 1000000 Venue foot traffic - by name
- Venue live data not included in package
- Search venues - by query (Fast) - not included
- 100000 Search venues - by query (Normal) included
- CDN caching

$2999 / month
===

The big difference with the Basic package plans is that Pro packages include include unlimited live data (for the venues in the package) and the fast search venues API.

## Pro - Package - Max 1 unique venue / month

- 2K Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 1 Venue foot traffic - by name
- Unlimited *Venue live data
- 0 Search venues - by query (Fast)
- 0 Search venues - by query (Normal)
- CDN caching
$66.00 / month

## Pro - Package - Max 50 unique venues / month

- 100K Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 50 Venue foot traffic - by name
- Unlimited *Venue live data
- 50 Search venues - by query (Fast)
- 500 Search venues - by query (Normal)
- CDN caching
$96.00 / month

## Pro - Package - Max 100 unique venues / month

- 200K Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 100 Venue foot traffic - by name
- Unlimited *Venue live data
- 100 Search venues - by query (Fast)
- 5000 Search venues - by query (Normal)
- CDN caching
$119.00 / month

## Pro - Package - Max 500 unique venues / month

- 1M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 500 Venue foot traffic - by name
- Unlimited *Venue live data
- 500 Search venues - by query (Fast)
- 7000 Search venues - by query (Normal)
- CDN caching
$199.00 / month

## Pro - Package - Max 1K unique venues / month

- 2M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 1000 Venue foot traffic - by name
- Unlimited *Venue live data
- 1000 Search venues - by query (Fast)
- 10000 Search venues - by query (Normal)
- CDN caching
$249.00 / month

## Pro - Package - Max 5K unique venues / month

- 10M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 5000 Venue foot traffic - by name
- Unlimited *Venue live data
- 2000 Search venues - by query (Fast)
- 20000 Search venues - by query (Normal)
- CDN caching
$399.00 / month

## Pro - Package - Max 20K unique venues / month

- 40M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 20000 Venue foot traffic - by name
- Unlimited *Venue live data
- 5000 Search venues - by query (Fast)
- 30000 Search venues - by query (Normal)
- CDN caching
$999.00 / month

## Pro - Package - Max 100K unique venues / month

- 200M Venue foot traffic - by filter
- Unlimited *Venue foot traffic - by ID
- 100000 Venue foot traffic - by name
- Unlimited *Venue live data
- 10000 Search venues - by query (Fast)
- 100000 Search venues - by query (Normal)
- CDN caching
$2999.00 / month

## Free account
Free accounts include 2x 1000 API credits. 1000 for foot traffic forecast data and 1000 credits for quering existing forecasts through the venue filter and query endpoints.

## Optimize costs

Key Strategies to Reduce API Costs
For users on metered plans, minimizing API credit consumption is crucial. For all users, efficient data management improves application performance. Caching is the most effective method to achieve both.

1. Implement Data Caching
Caching involves storing frequently accessed data locally, so subsequent requests for the same data can be served directly from your cache instead of making new API calls. This significantly reduces API requests and improves response times for your users.

Data Types to Cache and Recommended Caching Durations:

Foot Traffic Forecast Data (Venue Foot traffic - by ID, Venue Foot traffic - by name, Venue Filter, Venue Search):

What to Cache: Hourly foot traffic percentages for the entire week (7 days x 24 hours).

Recommended Duration: At least one week, and potentially up to one month. Foot traffic patterns are generally consistent over weeks and even months, so refreshing forecast data less frequently can drastically reduce API calls.

Live Foot Traffic Data (Live foot traffic API, Venue Filter API with live=true):

What to Cache: Live data percentage for the current clock hour.

Recommended Duration: Cache for the current clock hour. Live data is updated hourly, so there's no benefit in caching it for longer than an hour.

Venue Filter API:

What to Cache: The venue filter returns foot traffic data for multiple venues according to the filter for a specific day. Therefore we recommend caching the venue filter results for a whole day (take the local timezone into account). If you request live data through the venue filter it is recommended to cache the response for the current clock hour only.

The venue filter is also often used to show venues nearby a user within a certain radius or bounding box. Therefore often the exact user coordinates are send to the venue filter. This exact coordinates usually contains a lot of decimal places. Therefore the request of each individual user is an unique API request even if the users are 100 ft away from each other.
To optimize the Venue Filter cost and speed, we suggest rounding down the (user) coordinates to 2 decimals. This would ensure that all users within roughly a 1.1km / 0.68 miles radius will get the same cached result from the CDN nearby the location. This could, for example, reduce the loading time from 5 seconds to 50ms and also reduce the API credits used.
See <https://en.wikipedia.org/wiki/Decimal_degrees> for more information.

Venue Search API Results:
The venue search API is relatively slow and expensive compared to the venue filter. We recommend only using this endpoint if the Venue Filter configuration is not sufficient or if venues are missing in BestTime. An example would be if you want to let your users search for venues in natural language like "brunch places in Manhattan NYC", or "McDonalds nearby the Eifel Tower".
What to Cache: The entire JSON response from the Venue Search API for specific search queries.
Recommended Duration: At least one week. Venue search results for common queries are also relatively stable over time.
By implementing caching for these data types, you can serve a significant portion of user requests from your local cache, dramatically reducing your API credit usage and improving your application's speed.
It would be more efficient to use the Venue Filter API and select the coordinates of the Eifel Tower and set FAST_FOOD as venue type.

2. Optimize Live Data Usage
Live data provides real-time foot traffic information and is incredibly valuable, but it's also the most API credit-intensive data type because it needs to be updated frequently (every clock hour). Consider these strategies to optimize live data usage:

Prioritize Forecast Data: For many use cases, forecast data is sufficient. Forecast data provides accurate predictions based on historical patterns and is much cheaper to access. Use forecast data as your primary data source and only use live data when absolutely necessary for real-time insights.

On-Demand Live Data Requests: Instead of proactively refreshing live data for all venues continuously, consider fetching live data only when a user specifically requests it, such as when they click on a venue to view detailed information. This user-initiated approach significantly reduces unnecessary live data API calls.

Selective Live Data Updates: If you need to actively update live data, consider these optimizations:

Update only during venue opening hours: Live data is only relevant when venues are open. Avoid refreshing live data during closed hours.

Focus on peak hours or relevant times: If your application targets specific times (e.g., nightlife), you might only need to update live data during those hours (e.g., evenings for bars and clubs).

Target audience behavior: Consider your users' behavior. If they primarily use your app during specific times of the day, focus live data updates during those periods.

By strategically implementing these caching and live data optimization techniques, you can effectively manage your API costs, ensure efficient data usage, and deliver a fast and responsive experience to your users.

# Pricing projections example email

Let's break down the cost projections for you. BestTime.app offers two main pricing models: Metered plans (pay-as-you-go based on API credits) and Package plans (fixed monthly fee for a set number of venues).

Metered Plans: Cost Projections Based on User Volume
With Metered plans (Basic Metered or Pro Metered), you pay for the API credits your application consumes. The cost per credit depends on your chosen plan and volume.
Here's a simplified example to illustrate the cost per user, assuming each user request in your app triggers a Venue Filter API call (which is the most cost-effective and fastest API for most use cases like yours). Let's also assume each user makes 10 Venue Filter API requests per month in your app (This gives results for 100 venues).
In the example I don't take into account caching (later explained).

Each Venue Filter API request costs 0.1 API credit per venue returned. If we assume on average your app returns 10 venues per Venue Filter API request, then each API request will cost 1 API credit (10 venues * 0.1 credits/venue = 1 credit).

Therefore, each user, making 10 API requests per month, would consume 10 API credits per month (for 100 venues data points). Now let's project the costs for different user volumes, considering both the Basic Metered and Pro Metered plans:

**1. For 100 Users:**

- Total API Credits per month: 100 users * 10 credits/user = 1000 API credits.

  - **Basic Metered Plan:**  1000 API credits * **$0.04/credit** = **$40 USD/month**. (Remember the minimum monthly cost for the Basic Metered plan is $29 USD, so this projection is valid).

  - **Pro Metered Plan:** 1000 API credits * **$0.009/credit** + **$99 platform fee** = **$9 + $99 = $108 USD/month**.

**2. For 1000 Users:**

- Total API Credits per month: 1000 users * 10 credits/user = 10,000 API credits.

  - **Basic Metered Plan:** 10,000 API credits * **$0.04/credit** = **$400 USD/month**.

  - **Pro Metered Plan:** 10,000 API credits * **$0.009/credit** + **$99 platform fee** = **$90 + $99 = $189 USD/month**.

    In this case, the Pro Metered plan becomes significantly more cost-effective than the Basic Metered plan.

**3. For 5000 Users:**

- Total API Credits per month: 5000 users * 10 credits/user = 50,000 API credits.

  - **Basic Metered Plan:** 50,000 API credits * **$0.04/credit** = **$2000 USD/month**.

  - **Pro Metered Plan:** To calculate the Pro Metered cost with volume discounts, we break it down:
    - First 10K credits: 10,000 credits * **$0.009/credit** = $90
    - Next 40K credits: 40,000 credits * **$0.006/credit** = $240
    - Platform fee: $99
    - Total Pro Metered cost: $90 + $240 + $99 = **$429 USD/month**.

    At this user volume, the Pro Metered plan is substantially more cost-effective compared to the Basic Metered plan.

**Important Notes for Metered Plans:**
These are estimated costs. Actual costs may vary depending on user behavior and the number of API requests per user.
The Pro Metered plan becomes increasingly cost-effective as your API credit consumption grows due to the volume-based discounts.
To optimize costs with Metered plans, consider implementing caching strategies (explained later) to reduce API requests.

Package Plans: Fixed Monthly Costs for Venue Volumes
Package plans offer a fixed monthly price, which can be beneficial for budget predictability, especially as your user base grows. They are structured around the maximum number of unique venues for which you can request foot traffic data within a calendar month.
Let's look at package options relevant to your request, focusing on Pro Packages as you mentioned interest in options with live data:

Pro Packages (Include Unlimited Live Data):
Here are Pro Package options that might be suitable for your app, depending on the number of unique venues you anticipate needing data for each month:

1. Pro - Package - Max 500 Unique Venues / Month:
Price: $199.00 / month
Includes:
1M Venue foot traffic - by filter API calls
Unlimited Venue foot traffic - by ID API calls
500 Venue foot traffic - by name API calls
Unlimited Venue live data API calls
500 Search venues - by query (Fast) API calls
7000 Search venues - by query (Normal) API calls
CDN caching
This package would be suitable if your app primarily focuses on a curated list of around 500 venues or less per month, and you want to heavily utilize live data.

2. Pro - Package - Max 5K Unique Venues / Month:
Price: $399.00 / month
Includes:
10M Venue foot traffic - by filter API calls
Unlimited Venue foot traffic - by ID API calls
5000 Venue foot traffic - by name API calls
Unlimited Venue live data API calls
2000 Search venues - by query (Fast) API calls
20000 Search venues - by query (Normal) API calls
CDN caching
This package is ideal if you need data for up to 5000 unique venues per month and want to offer a wide selection of venues with live data in your app.

3. Pro - Package - Max 20K Unique Venues / Month:
Price: $999.00 / month
Includes:
40M Venue foot traffic - by filter API calls
Unlimited Venue foot traffic - by ID API calls
20000 Venue foot traffic - by name API calls
Unlimited Venue live data API calls
5000 Search venues - by query (Fast) API calls
30000 Search venues - by query (Normal) API calls
CDN caching

This package is designed for apps requiring a larger venue database, up to 20,000 unique venues per month, with comprehensive live data access.

Basic Packages (Without Live Data):
If live data is not a critical feature for your initial app version, or if you want to explore more cost-effective options, Basic Packages might be considered. They do not include live data, but offer very high volumes for forecast data:

1. Basic - Package - Max 10K Unique Venues / Month:
Price: $299.00 / month
Includes:
10M Venue foot traffic - by filter API calls
Unlimited Venue foot traffic - by ID API calls
10000 Venue foot traffic - by name API calls
Venue live data not included in package
Search venues - by query (Fast) - not included
10000 Search venues - by query (Normal) included
CDN caching

2. Basic - Package - Max 100K Unique Venues / Month:
Price: $999 / month
Includes:
100M Venue foot traffic - by filter API calls
Unlimited Venue foot traffic - by ID API calls
100000 Venue foot traffic - by name API calls
Venue live data not included in package
Search venues - by query (Fast) - not included
50000 Search venues - by query (Normal) included
CDN caching

Price Comparison - Package vs. Metered (Example):
Let's compare the Pro Metered plan with the Pro Package for 5K Venues, assuming 50,000 API credits usage per month (as in the 5000 user example above):
Pro Metered Plan (50,000 credits): $429 USD/month (calculated above)
Pro Package for 5K Venues: $399 USD/month
In this scenario, the Pro Package for 5K venues is slightly more cost-effective and also provides a fixed cost, which is helpful for budgeting. Furthermore, the package includes unlimited live data, which could be valuable for your app's features.

Strategies to Reduce API Costs (Especially for Metered Plans):
Implement Caching: Caching foot traffic data (especially forecast data, which is relatively stable) can dramatically reduce API requests and credit consumption. For example, you can cache hourly forecasts for at least a week, or even a month. Live data should be cached for the current hour.
Optimize Live Data Usage: Consider using live data selectively. For example, only refresh live data when users specifically request it or during peak hours for nightlife venues. Forecast data is often sufficient for general trends and can be used as the primary data source.
Venue Filter Optimization: When using the Venue Filter API, round down coordinates to 2 decimal places. This can significantly improve CDN caching efficiency and reduce costs, especially when filtering venues nearby users. This ensures that users within a 1.1km radius share the same cached results.

You can find detailed pricing information and a plan comparison on our pricing page: <https://besttime.app/subscription/pricing>

To help you decide the best plan, it would be helpful to estimate:
The number of unique venues you plan to include in your app's database each month.
The importance of live foot traffic data for your app's core features.
Your anticipated user growth and API request volume over time.

Based on these estimates, we can refine the cost projections and help you select the most suitable and cost-effective plan.

Let me know if you have any other questions.

# FAQ

What kind of foot traffic data is available?
BestTime only offers foot traffic data for public venues. This includes bars, restaurants, cafes, supermarkets, malls, parks, beaches, museums, popular sightseeing attractions, and other public places. BestTime only offers relative foot traffic data, and no absolute visitor numbers This means that the data is relative to the visitor peak of the week. For example, if a venue has a peak of 100% on a Friday, and a value of 50% on a Monday, this means that the venue is half as busy on a Monday compared to a Friday.

What is a foot traffic forecast?
A foot traffic forecasts is based on visitor patterns from the past few weeks in a venue. The data is used to forecast foot traffic by hour throughout the week. Forecast values are displayed as percentages, ranging from 0 to 100%. The percentage indicates how busy a venue approximately is relative to its peak of the week. See 'live data' for a more accurate real-time value. The forecast result also includes different analysis, e.g.:

- Most busy days of the week (maximum, and mean)
- Daily peak hours, start, end, and intensity of the peaks
- What time most visitors come and leave the venue
- The quietest hours of the day

### What is a query?
A query gets specific data from an existing generated and stored forecast. It is faster than generating a new venue foot traffic forecast Queries can be used to e.g.:
A specific part of the analysis for a specific day. (e.g. only the peak analysis for Friday).
Get the foot traffic forecast for the current hour, with the venues local timezone taken into account.
Get the remaining time (in seconds) until the next peak.

### What is live foot traffic data?
Live data indicates the real-time foot traffic activity of a venue - expressed as a percentage - for the current hour of the day. When the live value is similar to the forecast value, it is busy as usual. The venue is busier than usual when the live value exceeds the forecasted value. The live values can also exceed 100%. A live value of 150%, for instance, indicates that it is approximately 50% busier compared to the forecasted peak of the week for that venue.

### Where do you get the data from?
The data is based on anonymized smartphone GPS signals. Third-party mobile apps collect the data from users who opt-in. The data is aggregated and normalized directly. We don't collect personal data, not even anonymized personal identification numbers. Consequently, we can't link any of our internal data with a single person.

### Does it work on all venues?
No. Venues need enough foot traffic (visitors) to make accurate forecasts. This volume needs to be even higher for real-time live data. The venue will become automatically available on BestTime when the foot traffic level is high enough. Foot traffic forecast data can be accessed 24/7, if available. When available, live data will only be shown during opening hours of the venue. At the moment, we do not add missing venues manually to our platform.

### Are forecasted automatically updated?
No, after a forecast is made it will be stored on the server. Using the website or API a venue forecast can be updated.  

### Can I use this data on my website, or somewhere else?
Yes, you can integrate the data on your website, or in your apps using our software API.

### Do you provide historical foot-traffic data?
No, we do not provide historical data. You could keep track of our foot-traffic yourself to analyse trends in the spread of relative foot-traffic data over the hours of the week. You could also use our Live data API endpoint every hour to see if there is more or less foot-traffic this current hour compared to the past weeks.

Do you provide absolute foot-traffic (visitor) volume numbers?
No we only provide relative foot-traffic numbers at the moment.

### How do you deal with privacy?
We care about privacy! BestTime.app only collects location & time based data as part of the foot-traffic data. We do not collect personal data from foot-traffic data, not even anonymized personal identification numbers. Additionally, we only provide aggregated data to our customers. Both our internal and external data can therefore not be traced to a single person. When using the API only the API key usage is logged. No personal information is saved when you or your customers use the software API. Our website uses Google Analytics and SmartLook only to optimize the user experience. We do not collect or sell personal information for other purposes.

### Does the demo count towards my quota?
No, when using the demo requests are not counted towards your quota (the demo tools are different than a free account with some free API credits). However, the demo is limited in terms of how fresh the data is and the amount of data that is returned. Additionally the demo does not have API access. You can use the demo to get a feel for the data (availabillity).

### Some venues are not available or do not have foot traffic data. Can BestTime add them to the platform?
It depends. The Venue Filter only returns venues with foot traffic data are already available on the platform. If a venue is missing from there the 'New Venue Foot Traffic' endpoint can be used to add venues by name and address. To add multiple venues at once using a query (e.g. brunch places in San Francisco) the 'Venue Search' endpoint can be used. Once venues are added they are available in the Venue Filter and through the Query API endpoints (by venue_id).

Sometimes when using the New Venue Foot Traffic endpoint using a name and address, the API responds that the venue cannot be found or does not have foot traffic data. Sometimes it can help to make the address less specific (e.g. without street number, state, country.). As last resort you can try to use the Venue Search endpoint. However, this endpoint is much slower and costs more credits.

### Can the dashboards in the compare tool be saved and reused?
Yes, the dashboards in the compare tool can be saved and opened. From the [Compare page](https://besttime.app/api/v1/compare) you can create a new dashboard, or open an existing one. The dashboards are saved per computer. So if you want to open a dashboard on a different computer you can copy and paste the URL of the dashboard into the browser of the other computer.

# Foot traffic VS venue

why a venue's maximum capacity isn't the same as 100% foot traffic in BestTime's data?

BestTime's foot traffic data is based on the analysis of anonymized smartphone GPS signals. The foot traffic percentages are calculated relative to the busiest hour of the week for that specific venue.

Therefore, 100% foot traffic does not represent the venue's maximum capacity. Instead, it represents the busiest predicted hour of the week for that particular venue, based on historical data.

Here's a breakdown of the key reasons why 100% foot traffic doesn't equal maximum venue capacity:

Relative Measurement: BestTime uses a relative scale (0-100%) to show how busy a venue is compared to its own peak hours, not its absolute maximum capacity. A venue might have a maximum capacity of 500 people, but its busiest hour might typically see 300 people. In this case, 100% foot traffic would represent approximately 300 people, not 500.

Forecast, Not Headcount: The foot traffic data is a forecast based on historical patterns. It doesn't provide an exact headcount of people in the venue at any given time.

Data Source and Methodology: The data is derived from aggregated and anonymized smartphone GPS signals. While it provides a good indication of relative busyness and trends, it's not designed to measure the absolute number of people inside a venue.

Live Data Can Exceed 100%: BestTime also offers live foot traffic data, which can sometimes exceed 100%. This happens when the current number of visitors is higher than the venue's typical busiest hour. For example, if a venue normally peaks at 300 people (100%) but a special event draws 450 people, the live data might show 150%.

In essence:

100% foot traffic on BestTime indicates the relative peak busyness of a venue based on historical data.
It does not indicate the venue's maximum legal or physical capacity.
Live data can exceed 100% when a venue is busier than its usual peak.

## Missing venues/ places

The Venue Filter only returns venues with foot traffic data are already available on the platform. If a venue is missing from there the 'New Venue Foot Traffic' endpoint can be used to add venues by name and address. To add multiple venues at once using a query (e.g. brunch places in San Francisco) the 'Venue Search' endpoint can be used. Once venues are added they are available in the Venue Filter and through the Query API endpoints (by venue_id).

Sometimes when using the New Venue Foot Traffic endpoint using a name and address, the API responds that the venue cannot be found or does not have foot traffic data. Sometimes it can help to make the address less specific (e.g. without street number, state, country.). As last resort you can try to use the Venue Search endpoint. However, this endpoint is much slower and costs more credits.

You can use our free demo to see if we have data available for your desired venues.

Our foot traffic data API provides relative foot traffic data for public venues, including bars, restaurants, cafes, supermarkets, malls, parks, beaches, museums, popular sightseeing attractions, and other public places.

The data is based on anonymized smartphone GPS signals collected from third-party mobile apps.

To get a venue listed on BestTime, they need to have enough foot traffic (visitors) to make accurate forecasts. This volume needs to be even higher for real-time live data. The venue will become automatically available on BestTime when the foot traffic level is high enough.


## Student discount

For university students I can give 10000 free API Credits.

Additionally, I can give you 50% discount on all monthly subscriptions for a maximum duration of 1 year.

Please register at BestTime.app with a valid university/ public research institute email address. After that, email us the email address of the registered student account.

Could you add a small link to the BestTime website on your website/ document sources in return for the discount? This would help us for our visibility on Google. It would also be great if you could fill in a testimonial.

## Request a call/ meeting

Thank you for your interest in BestTime.

Yes we can organize a call. However, usually before we organize a call we first like to understand your use-case better.

This will help us to ensure that a call is the most productive next step for both of us.

Sometimes potential customers put in a lot of effort in organizing a meeting, and after 1 minute in the call it turns out the use-case hard to realize using the BestTime tools.

So please tell me first about your ideas, company use-case and other questions. I’m happy to help.

## Venue Filter Live data

The Venue Filter can provide both foot traffic day data and live data for multiple venues in one API call. You can sort the live data in descending order. Based on your use-case, there are a few options:

1. You can use the Venue Update endpoint once per hour to update both the week foot traffic data and live data for ALL venues in your account. After this, you can use the Venue filter with a radius around the user. You can sort the venues based on the live data without refreshing it (as it is already done once per hour for all venues). By using live=true, it will return the live data, but not refresh it. This way, the Venue Filter user does not have to wait for the live data to refresh. To optimize the Venue Filter speed, I suggest rounding down the coordinates to 2 decimals. This would ensure that all users within roughly a 1.1km / 0.68 miles radius will get the same cached result from the CDN nearby the location. This could, for example, reduce the loading time from 5 seconds to 50ms.

2. You can use the Venue Filter, but also include live_refresh=True in the API call, besides live=true. This way, it will only refresh the live data of the venues that meet the filter (e.g., user radius). It will only refresh them automatically if the data is from the previous clock hour. However, refreshing the live data on demand makes the venue filter endpoint significantly slower and uses more API credits (applicable for metered plans).

3. Refreshing the live data for all venues individually once per hour using the Live endpoint is also a possibility. However, in that case, you might run into rate limits faster. With a package plan (which you currently have), the live data is automatically cached at a CDN location nearby the user for a whole clock hour. So, if multiple users get the same venue Live data from the same city, it would not count towards your rate-limit. Alternatively, you can store all live data in your own DB and distribute it to your users yourself.

# Tutorials

# Using collections for advanced Venue Filtering

In this example we demonstrate how collections can be used to show predefined sets of venues to users. We can use a collection that contain all venues, or one that contain all sports bars, or one that contain all cocktail bars.
For demonstration purposes we add 5 venues to the All venues collection, 2 sports bars to the sports bars collection and 2 cocktail bars to the cocktail bars collection.

# Preparing setup

---

# Creating collections

I'm creating the following collections. One for all venues, one for cocktail bars and one for sports bars. We loop over the collection names and using the Collection Create endpoint, and we store the collection_id's for later.

## All venues collection

POST

===
/api/v1/collection?api_key_private={{api_key_private}}&name=All venues
===

Returns

===json
{
    "collection": {
        "api_key_private": "X",
        "collection_id": "col_05feffe112fa4b35aa91d999964316e9",
        "name": "All venues"
    },
    "status": "OK"
}
===

## Cocktail bar collection

POST

===
/api/v1/collection?api_key_private={{api_key_private}}&name=Cocktail bars
===

Returns

===json
{
    "collection": {
        "api_key_private": "X",
        "collection_id": "col_0afd0b3114704d55a5f6802099171173",
        "name": "Cocktail bars"
    },
    "status": "OK"
}
===

## Sports bars collection

POST

===
/api/v1/collection?api_key_private={{api_key_private}}&name=Sports bars
===

Returns

===json
{
    "collection": {
        "api_key_private": "X",
        "collection_id": "col_a1931f2f77f84443bdde3bb6a6f5d565",
        "name": "Sports bars"
    },
    "status": "OK"
}
===

# Adding venues to the right collections

## Adding to sports bars collection

We add the following two sports bars to the sports bars collection: By looping over the venue_id's and using the Collection Add endpoint

- Happiest Hour: ven_415149775a732d724c774b52596f545a717a51754e66624a496843
- The Toasted Monkey: ven_4d43346d6c56553869504952673477436371333146617a4a496843

Happiest Hour:

POST

===
/api/v1/collection/col_a1931f2f77f84443bdde3bb6a6f5d565/ven_415149775a732d724c774b52596f545a717a51754e66624a496843?api_key_private={{api_key_private}}
===

returns

===json
{
    "collection_id": "col_a1931f2f77f84443bdde3bb6a6f5d565",
    "message": "Venue added to collection",
    "status": "OK",
    "venue_id": "ven_415149775a732d724c774b52596f545a717a51754e66624a496843"
}
===

The Toasted Monkey
POST

===
/api/v1/collection/col_a1931f2f77f84443bdde3bb6a6f5d565/ven_4d43346d6c56553869504952673477436371333146617a4a496843?api_key_private={{api_key_private}}
===

returns

===json
{
    "collection_id": "col_a1931f2f77f84443bdde3bb6a6f5d565",
    "message": "Venue added to collection",
    "status": "OK",
    "venue_id": "ven_4d43346d6c56553869504952673477436371333146617a4a496843"
}
===

## Adding to cocktail bars collection

- Bahama Breeze: ven_73754670614f346e61674352676f7770447478384939504a496843
- CVI.CHE 105: ven_55586365586437456e767552675932736d5650624365624a496843

Bahama breeze

===
/api/v1/collection/col_0afd0b3114704d55a5f6802099171173/ven_73754670614f346e61674352676f7770447478384939504a496843?api_key_private={{api_key_private}}
===

===json
{
    "collection_id": "col_0afd0b3114704d55a5f6802099171173",
    "message": "Venue added to collection",
    "status": "OK",
    "venue_id": "ven_73754670614f346e61674352676f7770447478384939504a496843"
}
===

CVI.CHE 105

POST

===
/api/v1/collection/col_0afd0b3114704d55a5f6802099171173/ven_55586365586437456e767552675932736d5650624365624a496843?api_key_private={{api_key_private}}
===

===json
{
    "collection_id": "col_0afd0b3114704d55a5f6802099171173",
    "message": "Venue added to collection",
    "status": "OK",
    "venue_id": "ven_55586365586437456e767552675932736d5650624365624a496843"
}
===

## Adding all 4 venues to the 'All venues' collection

We add all previous 4 venues to the 'All venues' collection by looping over the venue_id's and using the Collection Add endpoint. This is basically the same as above only we use the 'All venues' collection_id 'col_05feffe112fa4b35aa91d999964316e9' instead of the sports bars or cocktail bars collection_id's.

For demonstration purposes we also add a 5th venue ONLY to the All venues collection (and not to the other venue type specific collections)

- STK Steakhouse: ven_636264726f4b5334487a6d52675939454d3070565437304a496843

POST

===
/api/v1/collection/col_05feffe112fa4b35aa91d999964316e9/ven_636264726f4b5334487a6d52675939454d3070565437304a496843?api_key_private={{api_key_private}}
===

# Letting users use your collections

We now use the Venue Filter to filter venues using the right collection.

- All venues: col_05feffe112fa4b35aa91d999964316e9
- Cocktail bars: col_0afd0b3114704d55a5f6802099171173
- Sports bars: col_a1931f2f77f84443bdde3bb6a6f5d565

## Get all venues

We use the 'col_05feffe112fa4b35aa91d999964316e9' (all venues) to get all 5 venues.

===
/api/v1/venues/filter?collection_id=col_05feffe112fa4b35aa91d999964316e9&api_key_private={{api_key_private}}
===

> Note: at the bottom of the API response you will see the total number of returned venues.

<details>
<summary>Click for full JSON response with 5 venues</summary>

===json
{
    "status": "OK",
    "venues": [
        {
            "day_info": {
                "day_int": 5,
                "day_max": 100,
                "day_mean": 75,
                "day_rank_max": 1,
                "day_rank_mean": 2,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 23,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11:30am–11pm"
                    ],
                    "24h": [
                        {
                            "closes": 23,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                0,
                50,
                75,
                90,
                95,
                100,
                100,
                100,
                95,
                85,
                70,
                40,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.9,
            "reviews": 34782,
            "venue_address": "19501 Biscayne Blvd Aventura, FL 33180 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_55586365586437456e767552675932736d5650624365624a496843",
            "venue_lat": 25.9580354,
            "venue_lng": -80.1419752,
            "venue_name": "CVI.CHE 105",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 5,
                "day_max": 100,
                "day_mean": 66,
                "day_rank_max": 1,
                "day_rank_mean": 1,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                25,
                45,
                65,
                75,
                80,
                85,
                90,
                100,
                100,
                90,
                80,
                65,
                50,
                30,
                15,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 16904,
            "venue_address": "3045 N Rocky Point Dr E Tampa, FL 33607 United States",
            "venue_dwell_time_max": 120,
            "venue_dwell_time_min": 60,
            "venue_id": "ven_73754670614f346e61674352676f7770447478384939504a496843",
            "venue_lat": 27.96983,
            "venue_lng": -82.56264,
            "venue_name": "Bahama Breeze",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 5,
                "day_max": 100,
                "day_mean": 43,
                "day_rank_max": 1,
                "day_rank_mean": 2,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                5,
                10,
                15,
                20,
                20,
                30,
                35,
                35,
                40,
                50,
                70,
                90,
                100,
                80,
                50,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.3,
            "reviews": 4707,
            "venue_address": "2616 Olive St Dallas, TX 75201 United States",
            "venue_dwell_time_max": 150,
            "venue_dwell_time_min": 45,
            "venue_id": "ven_415149775a732d724c774b52596f545a717a51754e66624a496843",
            "venue_lat": 32.791142,
            "venue_lng": -96.806687,
            "venue_name": "Happiest Hour",
            "venue_type": "BAR"
        },
        {
            "day_info": {
                "day_int": 5,
                "day_max": 87,
                "day_mean": 55,
                "day_rank_max": 2,
                "day_rank_mean": 2,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                25,
                35,
                50,
                60,
                65,
                65,
                70,
                75,
                85,
                85,
                80,
                60,
                40,
                25,
                10,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 3140,
            "venue_address": "678 75th Ave St Pete Beach, FL 33706 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_4d43346d6c56553869504952673477436371333146617a4a496843",
            "venue_lat": 27.740851,
            "venue_lng": -82.7538416,
            "venue_name": "The Toasted Monkey",
            "venue_type": "BAR"
        }
    ],
    "venues_n": 4,
    "window": {
        "day_window": "Saturday 6AM until Sunday 5AM",
        "day_window_end_int": 6,
        "day_window_end_txt": "Sunday",
        "day_window_start_int": 5,
        "day_window_start_txt": "Saturday",
        "time_local": 4,
        "time_local_12": "4AM",
        "time_local_index": 22,
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_end_ix": 23,
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "time_window_start_ix": 0
    }
}
===

</details>

## Get all cocktail bars

We use the 'col_a1931f2f77f84443bdde3bb6a6f5d565' (sports bars) to get all sports bars.

GET

===
/api/v1/venues/filter?collection_ids=col_0afd0b3114704d55a5f6802099171173&api_key_private={{api_key_private}}
===

Results in two venues:

- Bahama Breeze
- CVI.CHE 105

<details>
<summary>Click for full JSON response with 2 venues</summary>

===json
{
    "status": "OK",
    "venues": [
        {
            "day_info": {
                "day_int": 5,
                "day_max": 100,
                "day_mean": 75,
                "day_rank_max": 1,
                "day_rank_mean": 2,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 23,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11:30am–11pm"
                    ],
                    "24h": [
                        {
                            "closes": 23,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                0,
                50,
                75,
                90,
                95,
                100,
                100,
                100,
                95,
                85,
                70,
                40,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.9,
            "reviews": 34782,
            "venue_address": "19501 Biscayne Blvd Aventura, FL 33180 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_55586365586437456e767552675932736d5650624365624a496843",
            "venue_lat": 25.9580354,
            "venue_lng": -80.1419752,
            "venue_name": "CVI.CHE 105",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 5,
                "day_max": 100,
                "day_mean": 66,
                "day_rank_max": 1,
                "day_rank_mean": 1,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                25,
                45,
                65,
                75,
                80,
                85,
                90,
                100,
                100,
                90,
                80,
                65,
                50,
                30,
                15,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 16904,
            "venue_address": "3045 N Rocky Point Dr E Tampa, FL 33607 United States",
            "venue_dwell_time_max": 120,
            "venue_dwell_time_min": 60,
            "venue_id": "ven_73754670614f346e61674352676f7770447478384939504a496843",
            "venue_lat": 27.96983,
            "venue_lng": -82.56264,
            "venue_name": "Bahama Breeze",
            "venue_type": "RESTAURANT"
        }
    ],
    "venues_n": 2,
    "window": {
        "day_window": "Saturday 6AM until Sunday 5AM",
        "day_window_end_int": 6,
        "day_window_end_txt": "Sunday",
        "day_window_start_int": 5,
        "day_window_start_txt": "Saturday",
        "time_local": 5,
        "time_local_12": "5AM",
        "time_local_index": 23,
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_end_ix": 23,
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "time_window_start_ix": 0
    }
}
===

</details>

## Get all sports bars

We use the 'col_a1931f2f77f84443bdde3bb6a6f5d565' (sports bars) to get all sports bars.

GET

===
/api/v1/venues/filter?collection_ids=col_a1931f2f77f84443bdde3bb6a6f5d565&api_key_private={{api_key_private}}
===

Results in two venues:

- Happiest Hour
- The Toasted Monkey

<details>
<summary>Click for full JSON response with 2 venues</summary>

===json
{
    "status": "OK",
    "venues": [
        {
            "day_info": {
                "day_int": 5,
                "day_max": 100,
                "day_mean": 43,
                "day_rank_max": 1,
                "day_rank_mean": 2,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                5,
                10,
                15,
                20,
                20,
                30,
                35,
                35,
                40,
                50,
                70,
                90,
                100,
                80,
                50,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.3,
            "reviews": 4707,
            "venue_address": "2616 Olive St Dallas, TX 75201 United States",
            "venue_dwell_time_max": 150,
            "venue_dwell_time_min": 45,
            "venue_id": "ven_415149775a732d724c774b52596f545a717a51754e66624a496843",
            "venue_lat": 32.791142,
            "venue_lng": -96.806687,
            "venue_name": "Happiest Hour",
            "venue_type": "BAR"
        },
        {
            "day_info": {
                "day_int": 5,
                "day_max": 87,
                "day_mean": 55,
                "day_rank_max": 2,
                "day_rank_mean": 2,
                "day_text": "Saturday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 5,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                25,
                35,
                50,
                60,
                65,
                65,
                70,
                75,
                85,
                85,
                80,
                60,
                40,
                25,
                10,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 3140,
            "venue_address": "678 75th Ave St Pete Beach, FL 33706 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_4d43346d6c56553869504952673477436371333146617a4a496843",
            "venue_lat": 27.740851,
            "venue_lng": -82.7538416,
            "venue_name": "The Toasted Monkey",
            "venue_type": "BAR"
        }
    ],
    "venues_n": 2,
    "window": {
        "day_window": "Saturday 6AM until Sunday 5AM",
        "day_window_end_int": 6,
        "day_window_end_txt": "Sunday",
        "day_window_start_int": 5,
        "day_window_start_txt": "Saturday",
        "time_local": 5,
        "time_local_12": "5AM",
        "time_local_index": 23,
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_end_ix": 23,
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "time_window_start_ix": 0
    }
}
===

</details>

## Combining collection_id

The Venue filter API accepts both a 'collection_id' parameter to filter one collection, but since recently also the 'collection_ids' parameter to filter multiple collections.

We can combine both parameters to filter for example sports bars and cocktail bars at the same time.

GET

===
api/v1/venues/filter?collection_ids=col_0afd0b3114704d55a5f6802099171173,col_a1931f2f77f84443bdde3bb6a6f5d565&api_key_private={{api_key_private}}
===

This results in 4 venues:

- Bahama Breeze
- CVI.CHE 105
- Happiest Hour
- The Toasted Monkey

As you can see the Steak restaurant is not included in the result.

<details>
<summary>Click for full JSON response with 4 venues</summary>
===json
{
    "status": "OK",
    "venues": [
        {
            "day_info": {
                "day_int": 3,
                "day_max": 49,
                "day_mean": 41,
                "day_rank_max": 4,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 22,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11:30am–10:30pm"
                    ],
                    "24h": [
                        {
                            "closes": 22,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                20,
                30,
                40,
                45,
                45,
                45,
                45,
                50,
                50,
                45,
                40,
                20,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.9,
            "reviews": 34782,
            "venue_address": "19501 Biscayne Blvd Aventura, FL 33180 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_55586365586437456e767552675932736d5650624365624a496843",
            "venue_lat": 25.9580354,
            "venue_lng": -80.1419752,
            "venue_name": "CVI.CHE 105",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 52,
                "day_mean": 35,
                "day_rank_max": 4,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 0,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–12am"
                    ],
                    "24h": [
                        {
                            "closes": 0,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                20,
                30,
                35,
                30,
                30,
                35,
                40,
                50,
                50,
                50,
                40,
                25,
                15,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 16904,
            "venue_address": "3045 N Rocky Point Dr E Tampa, FL 33607 United States",
            "venue_dwell_time_max": 120,
            "venue_dwell_time_min": 60,
            "venue_id": "ven_73754670614f346e61674352676f7770447478384939504a496843",
            "venue_lat": 27.96983,
            "venue_lng": -82.56264,
            "venue_name": "Bahama Breeze",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 32,
                "day_mean": 21,
                "day_rank_max": 3,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 16,
                "venue_open_close_v2": {
                    "12h": [
                        "4pm–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 16
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                15,
                20,
                25,
                25,
                30,
                30,
                30,
                20,
                10,
                5,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.3,
            "reviews": 4707,
            "venue_address": "2616 Olive St Dallas, TX 75201 United States",
            "venue_dwell_time_max": 150,
            "venue_dwell_time_min": 45,
            "venue_id": "ven_415149775a732d724c774b52596f545a717a51754e66624a496843",
            "venue_lat": 32.791142,
            "venue_lng": -96.806687,
            "venue_name": "Happiest Hour",
            "venue_type": "BAR"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 57,
                "day_mean": 35,
                "day_rank_max": 4,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 0,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–12am"
                    ],
                    "24h": [
                        {
                            "closes": 0,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                15,
                20,
                25,
                30,
                35,
                40,
                45,
                50,
                55,
                50,
                40,
                25,
                15,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 3140,
            "venue_address": "678 75th Ave St Pete Beach, FL 33706 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_4d43346d6c56553869504952673477436371333146617a4a496843",
            "venue_lat": 27.740851,
            "venue_lng": -82.7538416,
            "venue_name": "The Toasted Monkey",
            "venue_type": "BAR"
        }
    ],
    "venues_n": 4,
    "window": {
        "day_window": "Thursday 6AM until Friday 5AM",
        "day_window_end_int": 4,
        "day_window_end_txt": "Friday",
        "day_window_start_int": 3,
        "day_window_start_txt": "Thursday",
        "time_local": 5,
        "time_local_12": "5AM",
        "time_local_index": 23,
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_end_ix": 23,
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "time_window_start_ix": 0
    }
}
===
</details>

## Combining All venues + Sports bar

To demonstrate that combining collections does not result in duplicate we combine the All Venues and Sports Bar collection in the Venue Filter API. The All Venues Collection contains 5 venues, and the Sports bar collection 2. The Venue Filter result is 5 venues.

GET

===
/api/v1/venues/filter?collection_ids=col_05feffe112fa4b35aa91d999964316e9,col_a1931f2f77f84443bdde3bb6a6f5d565&api_key_private={{api_key_private}}
===

Result

<details>
<summary>Click for full JSON response with 5 venues</summary>
===json
{
    "status": "OK",
    "venues": [
        {
            "day_info": {
                "day_int": 3,
                "day_max": 49,
                "day_mean": 41,
                "day_rank_max": 4,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 22,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11:30am–10:30pm"
                    ],
                    "24h": [
                        {
                            "closes": 22,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                20,
                30,
                40,
                45,
                45,
                45,
                45,
                50,
                50,
                45,
                40,
                20,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.9,
            "reviews": 34782,
            "venue_address": "19501 Biscayne Blvd Aventura, FL 33180 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_55586365586437456e767552675932736d5650624365624a496843",
            "venue_lat": 25.9580354,
            "venue_lng": -80.1419752,
            "venue_name": "CVI.CHE 105",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 52,
                "day_mean": 35,
                "day_rank_max": 4,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 0,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–12am"
                    ],
                    "24h": [
                        {
                            "closes": 0,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                20,
                30,
                35,
                30,
                30,
                35,
                40,
                50,
                50,
                50,
                40,
                25,
                15,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 16904,
            "venue_address": "3045 N Rocky Point Dr E Tampa, FL 33607 United States",
            "venue_dwell_time_max": 120,
            "venue_dwell_time_min": 60,
            "venue_id": "ven_73754670614f346e61674352676f7770447478384939504a496843",
            "venue_lat": 27.96983,
            "venue_lng": -82.56264,
            "venue_name": "Bahama Breeze",
            "venue_type": "RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 44,
                "day_mean": 32,
                "day_rank_max": 6,
                "day_rank_mean": 5,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 23,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–11:30pm"
                    ],
                    "24h": [
                        {
                            "closes": 23,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                15,
                20,
                20,
                25,
                30,
                35,
                35,
                40,
                45,
                45,
                40,
                35,
                30,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 4,
            "rating": 4.5,
            "reviews": 13873,
            "venue_address": "1075 Peachtree St NE Atlanta, GA 30309 United States",
            "venue_dwell_time_max": 150,
            "venue_dwell_time_min": 90,
            "venue_id": "ven_636264726f4b5334487a6d52675939454d3070565437304a496843",
            "venue_lat": 33.7840453,
            "venue_lng": -84.3827642,
            "venue_name": "STK Steakhouse",
            "venue_type": "STEAK_RESTAURANT"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 32,
                "day_mean": 21,
                "day_rank_max": 3,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 2,
                "venue_open": 16,
                "venue_open_close_v2": {
                    "12h": [
                        "4pm–2am"
                    ],
                    "24h": [
                        {
                            "closes": 2,
                            "opens": 16
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                15,
                20,
                25,
                25,
                30,
                30,
                30,
                20,
                10,
                5,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.3,
            "reviews": 4707,
            "venue_address": "2616 Olive St Dallas, TX 75201 United States",
            "venue_dwell_time_max": 150,
            "venue_dwell_time_min": 45,
            "venue_id": "ven_415149775a732d724c774b52596f545a717a51754e66624a496843",
            "venue_lat": 32.791142,
            "venue_lng": -96.806687,
            "venue_name": "Happiest Hour",
            "venue_type": "BAR"
        },
        {
            "day_info": {
                "day_int": 3,
                "day_max": 57,
                "day_mean": 35,
                "day_rank_max": 4,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day.",
                "venue_closed": 0,
                "venue_open": 11,
                "venue_open_close_v2": {
                    "12h": [
                        "11am–12am"
                    ],
                    "24h": [
                        {
                            "closes": 0,
                            "opens": 11
                        }
                    ]
                }
            },
            "day_int": 3,
            "day_raw": [
                0,
                0,
                0,
                0,
                0,
                15,
                20,
                25,
                30,
                35,
                40,
                45,
                50,
                55,
                50,
                40,
                25,
                15,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "price_level": 2,
            "rating": 4.5,
            "reviews": 3140,
            "venue_address": "678 75th Ave St Pete Beach, FL 33706 United States",
            "venue_dwell_time_max": 0,
            "venue_dwell_time_min": 0,
            "venue_id": "ven_4d43346d6c56553869504952673477436371333146617a4a496843",
            "venue_lat": 27.740851,
            "venue_lng": -82.7538416,
            "venue_name": "The Toasted Monkey",
            "venue_type": "BAR"
        }
    ],
    "venues_n": 5,
    "window": {
        "day_window": "Thursday 6AM until Friday 5AM",
        "day_window_end_int": 4,
        "day_window_end_txt": "Friday",
        "day_window_start_int": 3,
        "day_window_start_txt": "Thursday",
        "time_local": 4,
        "time_local_12": "4AM",
        "time_local_index": 22,
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_end_ix": 23,
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "time_window_start_ix": 0
    }
}
===
</details>

# Conclusion

The collections API is a powerful tool to curate venues. You can create a list of all your venues, but also create collections for specific niche venues like Cocktail bars and Sports bars. On other words you can 'tag' venues with specific names, by adding them to custom collections.

# Use-cases

## Revolutionizing City Tours: Leveraging Foot Traffic Data for Optimal Exploration Experience

Foot traffic data is an innovative way to gauge the relative busyness of public venues like museums, parks, restaurants, and more. BestTime.app, a leading foot traffic data API Saas, provides this data on an hourly basis. With a percentage ranging from 0 to 100%—where 100% denotes the peak hour of the week—you can get a clear snapshot of when a venue is bustling or calm.

When it comes to city tours, integrating BestTime's foot traffic data can be a game-changer. Instead of guessing the best times to visit attractions, you can plan your itinerary based on data-driven insights. Here's how it works.
First, you can use the data to avoid peak hours. By visiting attractions when they're less busy, you can enjoy them without the usual crowds. This can significantly enhance your sightseeing experience, allowing you to fully absorb the rich culture and history of each site.
Second, you can optimize your city tour schedule. By knowing when each attraction is least busy, you can craft a plan that allows you to visit multiple places in one day without feeling rushed or overwhelmed. You'll be able to navigate the city more efficiently and make the most of your time.

Third, you can integrate these insights into your own travel app or business. If you're a tour operator or a travel app developer, BestTime's API allows you to enrich your services by providing your customers with the optimal time to visit each attraction. This way, you're not just offering a tour - you're offering a tailored, crowd-free experience.
In a bustling city like New York, the possibilities are endless. With foot traffic data, you can transform a typical sightseeing tour into an optimized exploration that balances enjoyment and efficiency.

## Leverage Foot Traffic Data to Discover Lively Social Spots in a New Area

Moving to a new city or just visiting an unfamiliar area can sometimes make it challenging to find places that offer a vibrant social scene, particularly on off-peak days like Monday evenings. Foot traffic data, such as what BestTime.app offers, can be a game-changer in these situations, giving you the ability to find busy places to socialize or explore the local nightlife based on real-time and predicted crowd density.
Why Use Foot Traffic Data?
Foot traffic data refers to the quantity of people present in a specific location at a given time. BestTime.app provides relative foot traffic data, indicating the crowd density as a percentage from 0 to 100% for each hour of the week. In this context, 100% represents the peak hour of the week for that specific venue.
While this data doesn’t provide absolute visitor numbers or seasonal changes, it does provide a relative understanding of how busy a location like a bar, restaurant, park, beach, or museum can be at different times. This allows you to determine when a place is bustling with people or when it’s more quiet and serene.

How to Use Foot Traffic Data
Imagine you're new to Los Angeles and you're looking for a lively bar or restaurant on a Monday evening. Using BestTime.app, you can filter businesses based on how busy they are predicted to be at specific hours and days of the week.
With a few clicks, you can discover which venues in your chosen neighborhood are likely to have a bustling crowd, making your decision process much simpler and your socializing experience much better.

The Benefits of Using BestTime.app
BestTime.app not only allows you to find busy places to socialize, but also helps you avoid crowded times if you prefer a more laid-back environment. This can be particularly useful when planning visits to popular attractions like museums or parks, where a lower crowd density might enhance your experience.
Moreover, businesses can also leverage this data to adjust their operating hours or plan events based on predicted foot traffic, ensuring they can serve their customers better.

## Search & filter venue foot-traffic around the world

There are plenty of ways to find what you’re looking for in a city, but not all of them work as well as they should. This article discusses how you can use foot-traffic data to be the smartest in the room. The used tool lets you search and filter worldwide venue foot-traffic data in order to find the best venues for whatever your needs may be. Whether it’s finding where to go out Friday night, visiting a grocery store when it’s less busy, improve digital outdoor ads efficiency, or researching mobility trends, this might be the tool for you.
Using the BestTime.app Venue Search in the Radar tool you will be able to filter the foot-traffic data on visitor peak, day/time, geographic area, and business type, reviews, rating and price level. For example “Busy bars in San Francisco Friday evening”, “Quiet supermarkets Sydney Australia on Sunday from 8 AM until 11 AM”, or “Things to do in New York City”. The data is also available through the BestTime.app software API.
In this tutorial, we will describe how the Venue Search and Radar tools work in general without any use-case in mind. In future tutorials, we will describe how to use this tool using the API and use-case-specific versions. For this tutorial, you need a free BestTime.app account to get started, but a paid subscription to analyze higher volumes of foot-traffic data.  You can also use the free demo without registering, but not all functionality is included and includes and limited to only several searches per day.
A quick intro to BestTime. BestTime.app is a data analytics company providing instant foot-traffic data for venues in 150+ countries.
Forecast at what time of the week most visitors come to a venue (e.g. a store, bar, attraction, gym, or restaurant).
Live updates if a venue is more or less busy than normal (real-time).
Search venues foot-traffic based on category (e.g. supermarkets in London) or name (e.g. McDonalds in San Francisco).
Filter venues in a whole area based on visitor peaks, day, time, and business type.
Integrate all data directly into your applications/ research using the developer REST-API.
You could compare it with a supercharged FourSquare/ Google Popular Times API with more footfall data analytic functionality.

Adding new data
We start by opening the BestTime.app Radar Tool. The Radar tool is used to filter venues that are already added to BestTime by the user itself. You can get venue foot-traffic data one-by-one using the venue name and address (using the forecast tool/ API),  or using multiple venues using the Venue Search tool/API - which we will discuss now.
Add new venue foot-traffic by using the Venue Search bar in the top-left of the screen. For example "Things to do in New York City", or "Bars in San Francisco". Alternatively, you can find venues nearby by clicking "Nearby my location" in combination with a search query, e.g. "bars". Your browser might show a share location permission popup. The Venue Search tool will then use the estimated location (geographic coordinates) supplied by your browser to find places nearby you.
By clicking on the 'options' button more search options will appear.

NumberChange the ‘maximum number of venues’ to increase the number of search results. The higher the number the longer it takes before the search is complete. The venue search tool will analyze each found venue on foot-traffic directly using the internal ‘Forecast’ tool/API. Besides the Venue Search credits used for this search it also uses credits for each internal Forecast. So the more venues the longer and more credits it will cost.
OpenedBy default venues with all types of opening hours are searched (option ‘all’). Using the option ‘24H’ the only venues that are open 24H are returned. By selecting ‘now’ only venues that are open at this moment are returned.
Fast SearchThe Venue Search tool has two-speed options. ‘Fast’ and ‘Normal’. The results for both options are 99% similar, but by selecting the ‘fast’ option the search process is faster. However, the ‘fast’ option is using more credits. The ‘fast’ option can only be used to search for a maximum of 60 venues per search. The ‘normal’ search speed supports up to 200 venues per search (in the future this number might increase). If you select the ‘fast’ option and a number higher than 60 it will automatically use the ‘normal’ speed.
Combine with current resultsNormally, each new Venue Search result will only show the data of venues from the most recent search request. By selecting “combine with current results” the new results will be combined with the data already shown in the Radar tool. This way you can e.g. combine the search results for restaurants and supermarkets together. Internally this is done by adding the venues from the new result to an existing collection of venues. Later more on venue collections.
More search optionsThe Venue Search bar in the Radar tool only shows a few search options. For more search options you can use the dedicated Venue Search page, or the Venue Search API endpoint. Later more advanced search requests will be discussed in this tutorial.
Search resultsClick on the search icon to start the search. The search could take a while, depending on your search speed, number of venues, and if a similar search has been performed recently. When the search is complete the page will be reloaded with the new search results.
The Radar tool will show the venue foot-traffic data in the middle as a heatmap. On the left side of the Radar tool a list of venues is displayed including venue information and foot-traffic data for today. You can hover over the foot-traffic data to use the corresponding hours. Scroll down to see all venues shown in the Radar map.

Foot-traffic detailsSee more venue foot-traffic details, by clicking on a venue on the left-side or on the heatmap.
On top, the foot-traffic forecast for today is shown (indicated as a percentage from 0 to 100%). Sometimes live data is available and displayed in Pink (from 0 to 200%). Beneath that is a week foot-traffic forecast chart shown. The color represents how busy it is predicted to be. Hover with your mouse over an hour to see the corresponding percentage (also from 0 to 100%). Click on the button 'details' to open this venue in the BestTime Forecast tool. This tool will show more in-depth foot-traffic analyses.
Heatmap
The heatmap in the center of the Radar tool will show the foot-traffic data of all loaded venues together on a map with a color representing how busy it will be according to the forecast for a given hour or real-time using the Live data. By default, the heatmap shows the foot-traffic data for current hour and day in the local timezone of the map. Green indicates a percentage of foot-traffic forecast of 0% and red 100% (similar to the day and week forecasts). When zoomed in far enough, each colored dot represents an individual venue. When zoomed out the dots and colors blend together. The resulting color is based on the average of multiple venues together. However over the heatmap for the venue names. Click on a venue dot for more information.
Timeline

A timeline on top of the heatmap indicates by default the current hour in the local timezone of the map. Without active filters, the hours in the timeline range from 6 AM until 5 AM the next day (following the default BestTime day window). By clicking on another hour of the timeline foot-traffic for the selected hour will be displayed. Click on the ‘Play’ button to automatically loop over each hour of the day, resulting in an animated heatmap.

Map buttonsIn the top-left on the map are additional buttons displayed. From top to bottom: Zoom in and out using the + and — buttons. Show the heatmap fullscreen using the square fullscreen icon. Click the map pin to show your own location on the map. The chart icon will open show a popup to export currently loaded venues into the Compare dashboard tool (see today’s foot-traffic side by side). Click the question mark icon for more Help info.
In the middle right of the screen is the purple ‘filters’ button located. By default, the filter panel is shown, but it can be hidden/displayed using this button.

Filters
Filter options are shown on the right side of the screen. Using these filter we can filter currently loaded venues based on predicted foot traffic, live foot traffic, geographic location, day of the week, time of the day, venue type, rating, reviews, price level, collections, or a combination of the previous mentioned filters. This tool uses the Venue Filter API under the hood. Each time the filter is changed the API is called and charges API credits (depending on the number of venues filtered).

Reset/ View allClick this button to remove all filters and collections. A venue search result is automatically loaded in a new collection. By clicking this button it will basically show all venues that the user has loaded before into BestTime in this location on the map. When the filters are too restrictive a popup will be shown that no venues were meeting the filter criteria. Deselect the last chosen filter or use this button to remove all filters.
Update mapThe update map button is useful after dragging/ zooming the map. This will load all venues meeting the filters in the new map area.
Busy Min & Max & ConfigurationFilter venues based on foot-traffic forecasts or live data using a minimum or/and maximum percentage. By default, the filter will return venues that have at least one hour of the selected day and hours that meet the min and/ or max busy filter. Change the configuration from ‘any’ to ‘all’ to let the filter only return venues that meet the min and/or max on all selected hours and selected day.
Day & TimeFilter foot-traffic data on a day by selecting the day of the week, or today for automatically showing the foot-traffic for the current day in the local time. A day can be narrowed down by adjusting the minimum and maximum hours (using the BestTime day window).
Whole day & Now & LiveBy default, the ‘whole day’ is selected. After adjusting the minimum and maximum hours you can click on ‘whole day’ again to reset the hour filters.Click on ‘Now’ toggle to filter the foot-traffic ‘forecast’ to today’s current hour in the local timezone of the venues on the map.Using the ‘live’ toggle will show a similar result as the ‘now’ toggle, but shows how busy it is at this moment in real-time (opposed to the other settings that show a foot-traffic prediction based on historical visits in the past weeks). When the ‘now’ or ‘live’ mode is selected a foot-traffic gauge is displayed on the left side instead of a foot-traffic chart of today.

By default to save API credits, it will load live data of venues without refreshing the data. Check the ‘Refresh Live data’ button to refresh the live data for each individual venue. The filter result will take longer and will charge Live credits for each individual venue loaded in the Radar tool. It is recommended to only refresh the live data once per hour. Not all venues with forecast foot-traffic data have live data. Some not at all and some venues only during certain times of the day. So when selecting ‘live’ data it is normal that fewer or no venues will be displayed in the Radar tool.
TypesFilter down the venue results on venue type (category). See the Venue Filter APIdocumentation for all types. One or multiple types can be selected. Deselect all types to remove the type filter.
Rating & Reviews & PriceFilter the loaded venues on user rating, user reviews, and price level. Not all venues have a rating, reviews, and a price level. When one of these filters is selected, venues without that data will not be displayed.
AnimateConfigure the animation speed of the heatmap after pressing ‘play’ on the heatmap (this is not a filter).
LocationFilter venues based on a point on the map with a radius in meters. The point on the map can be defined using the ‘latitude’ and ‘longitude’. In the Venue Filter API venues can also be filtered on a bounding box.
API keyThe Radar tool/ Venue filter API show by default all venues in the BestTime database that meet the filter criteria. A user can optionally configure the Venue Filter API to only return venues that have been forecasted with a specific user private API key.
CollectionA collection is a group of venues and each collection has a unique ‘collection_id’. For every Venue Search, a new collection is automatically made and the venues from the search results are added to this collection (except when a search result is combined with current results). The collection_id is automatically displayed in the filter panel. By removing the collection_id the radar tool will show all previously loaded venues on that map (meeting the filter criteria). You can also fill in a previous collection_id from a manually curated collection or a previous venue search result. As discussed before, by selecting ‘Combine with current results’ in the Venue Search options the new search results will be added to the current loaded collection. You can find your existing collection on the Collection page. Collections that are automatically generated by a Venue Search are named after the search query. By clicking on a collection_id you will find links to open the collection in the Radar Tool or show a list of all containing venues.
No results meeting the filter criteria. Add more venues using the Venue Search tool/API , or individually per venue using the venue name and address (tool/ API).Depending on your account each venue foot-traffic forecast is only stored on the server for a predefined amount of days (see ‘days stored’ on the pricing page). We recommend refreshing venue foot-traffic forecasts every month. This can be done in bulk using the New forecast API endpoint, or manually for each venue using the New forecast website tool.
Advanced Venue Search filters
The filters in the Radar tool (Venue Filter API) can also be applied directly on the Venue Search tool/ API. If we for example want to find busy bars in San Francisco we can use the Venue Search tool to search for “bars in San Francisco” and subsequently add the filters “busy minimum = 50%”, Day = Friday, Hour minimum = 6 PM, maximum = 12 AM.Besides the inputs as discussed in the ‘Filter’ section, the Venue Search also understands several textual filter inputs (see for more information Natural language filters in the search query as filters). These textual filters will be translated into normal filter parameters. When directly searched for “Busy bars in San Francisco Friday night” using the Venue Search the same result will be displayed as the “Bars in San Francisco” search query in combination with the earlier mentioned filters. You will also see that the textual filters activate the same filters on the right side of the Radar Search. Other textual filter examples are:
“Busy bars in Sydney Australia Saturday from 8 PM until 11 PM” results in a search for “Bars in Sydney Australia” with filters set to: day = Saturday, hour min = 8 PM, hour max = 11 PM, busy min = 50%
“Quiet supermarkets” + ‘Nearby me’ checkbox checked, results in “Supermarkets” in a radius of 5 kilometers nearby you (using the latitude and longitude provided by your device) with the filters set to: ‘busy max’ = 50%
The filters do not directly influence the venues search result from the Venue Search itself (except ‘opened’ and ‘live’), but will apply the filters on the linked Radar tool/ Venue Filter API results. So when searching for “bars in San Francisco”
Other use-case examples
Save time by avoiding the crowd and reducing risks by finding quiet supermarkets, shops, and shopping malls.
Find out when and where the hippest bars using user ratings, reviews, foot-traffic, day, and time filters)
Save money by optimizing outdoor advertising by tracking foot-traffic in neighborhoods.
Analyze demand for specific venues or neighborhoods, like potential cab customers, or flex contractors in hospitality.
Analyze if a venue promotion or event resulted in more visitors using the live data.
Understand human behavior by for example when most people go to the beach or gym.
Find venues that are more or less crowded than normal using live data
If you are a marketer or publicist, you can now find out which venues have the most foot traffic on your target day and time. If you’re an event planner, venue owner, or advertiser
When you’re looking for a venue, it’s hard to find out what time of day or day of the week is best. This data can help answer that question so you can make better decisions on where to go.
Avoid waiting lines of popular hotspots like museums, and theme parks
With BestTime.app you can find the best time to visit venues and get your product in front of a lot more potential customers.
Optimize agenda meeting locations by suggesting the best time to go or avoid a venue.

## Find the best time to visit popular bars & night club using foot traffic data

Most people rely on websites and social connections to discover to which bar or nightclub they should go. However, most sources don't tell you what is the best day and time to visit that actual venue. In this BestTime.app tutorial we explain how you can use BestTime to find the most popular venues and on which day of the week and time you should go to find the crowd. With this method we can for example see all busy and popular bars on Thursday evening in your desired neighborhood/city.

Adding new data
 There are different methods to get venue foot-traffic data:
single venue using the name and addressIf you have a list of bars in you can add them by name and address (e.g. 'Alchemist Bar & Lounge - 679 3rd St, San Francisco, CA' . This can either be done using the website forecast tool or with the software API. Adding a big list of venues through the website can be tedious, and therefore we recommend using the software API to automate this.
multiple venues using the 'Venue Search' toolIf you don't have specific bar names in mind but are looking for the most popular bars in a neighborhood or city you can use the Venue Search tool. This can either be done using the website tool or software API. The Venue Search result returns only 20 (default) to 200 (max) venues (this number includes venues that do not have foot-traffic data). So this tool only returns a limited amount of venues with each result. You can cover bigger areas by searching multiple times in different areas. You could for example search for bars in each individual neighborhood.
BestTime only adds a venue to your account if a venue had enough foot-traffic data in the past weeks. It doesn't really matter which method you choose to add venues to your account, and you can even combine methods Once venues are added to your account we can use the Radar tool (or Venue Filter for the software API) to filter bars in a whole area for example on foot-traffic intensity, day of the week, time, etc.

Website tools
In the sections below we first demonstrate how to analyze bars using the website tools. In the later sections, we describe how to accomplish the same using the software API.
Adding venues by name and address
Click in the left main menu on 'New Foot-traffic data', and click then on 'Single Venue Search' to go to the Single venue forecasting tool. We type in "Novela" and select "Novela - 662 Mission Street, San Francisco, CA" from the dropdown list. The address will be filled in automatically in the 'Venue Address' field. Click on the button 'Forecast' to continue.

If BestTime has enough foot traffic data for this venue it will load the next page with foot traffic data details for the bar. The bar is now also added to your user account.

The blue bar charts show today’s foot traffic forecast per hour. The foot traffic data is expressed as a percentage from 0 to 100%, wherein 100% is the foot traffic peak of the week. If live data is available it will be displayed on the current hour in pink. The live percentage could go well above 100%. This means it is busier than the normal (forecasted) peak of the week. Click in the top right on 'Week' to get a week overview of the forecasted foot traffic.
If you add a new venue it could happen that an error will be displayed on top of the screen in red.  It could mean 1) that BestTime has not enough foot-traffic data for this venue (at this moment), 2) the venue might be currently closed or closed the whole day, 3) it could not find the venue.
In the tutorial below, the foot-traffic data details will be discussed.

We go now back to the previous page and add another bar - Alchemist Bar & Lounge, 3rd street, San Francisco - for demonstration purposes.
Foot-traffic overview
Click in the menu on 'My foot traffic' to get an overview of all the foot traffic data in your account. So far there are only two venues listed. Click on the name of the bar to go again to the foot-traffic data details of the specific bar.

Adding multiple venues using the 'Venue Search' tool
Let's say we don't know exactly the names of the bars, but we want to add some bars in the Mission District of San Francisco to our account.  Click in the left main menu on 'New Foot-traffic data', and click then on 'Search multiple venues' to go to the Venue Search Tool.

In the Search Query, we type 'bars in Mission District San Francisco'. We uncheck the 'Fast Search' checkbox -  after clicking on the Advanced button. For now, we select 20 as the maximum number of venues since the free account only includes a limited amount of credits (credits on a free account do not renew). Alternatively, you can check 'Nearby my location' and only type 'bars' in the Search query to avoid having to specify the location. Check the technical Venue Search documentation for more options and information. Click the 'Search' button at the bottom to start the search.

The Venue Search result will be automatically added to your user account and opened in the Radar Tool. The Radar tool is used to visualize and filter foot-traffic data of multiple venues at the same time. Not all bars matching your search result have foot-traffic data, so it could happen that you see less than 20 results.
On the left, you see the venue names and by default a chart with the foot-traffic prediction for today. Hover over the chart to see the predicted foot traffic percentages per hour. Click on the name of a venue to see more details.

In the middle of the screen, you will see a (heat)map with colored dots. When zoomed in enough, each dot represents a venue that is currently loaded in the Radar tool. The color represents the foot traffic intensity for the current hour, ranging from green (0%) to red (100%).  You can also click on the heatmap to open foot traffic details of the corresponding venue.
Later we discuss the radar tool in more detail but first, we are going to add some more bars. The tutorial below also explains the Radar tool in more detail.

As you can see, the previously added bars (Novela and Alchemist Bar & Lounge) are not visible on the map or in the list on the left. When we perform a new Venue Search the search results are added to a 'Collection'. A collection is a group of venues. By default, the Radar Tool only displays the venues within that collection.
If we would perform a new Venue search query for bars in a different neighborhood the Radar tools would again only show venues from the last search result. If we want to display bars from multiple neighborhoods/ searches together we can do two things. The first option is to add the results from a new venue search to the existing loaded collection. The second option is to remove or reset the active filters.
For option one, we add new venues again through a new Venue Search. However, this time we do this directly from within the Radar tool. In the top left of the screen, we type 'Bars in Marina District San Francisco'. After that, we click on the 'options' button. We check the 'Combine with current results' checkbox and click on the purple search icon.

After loading the new search results will be displayed again in the Radar tool. The map is centered on the new results, but if you zoom them map out you will see the previous bars from the Mission District are also still visible.

Now we will discuss the second option to display more venues in the Radar tool. On the right side of the Radar tool you see a panel full of buttons and filters. Using the filters you can narrow down the currently loaded venues on e.g. day, time, foot-traffic intensity, type, location, etc.  Again, the tutorial below also explains the Radar tool and the filters in more detail.

If you scroll to the bottom of the filter panel you will see that the Collection field is filled with a collection id. That means the Radar tool will only display venues on the map that are currently part of the given collection. You can press enter after removing the id from the field, or you can press the 'Update Map' button in the top right of the screen.

Now the previously added bars 'Novela' and 'Alchemist Bar & Lounge' should also be visible in the Radar Tool. While writing this tutorial we added more venues already so that's why the image displayed below shows more data.

As an alternative to manually removing the collection id, you can press the 'Reset/ View all' button on the top-right of the Radar Tool. This will remove/reset all active filters in the Radar tool at the same time (useful when we later use more filters in the Radar tool).
If we only want to show the venues from the previous collection again, you can do so by filling in the collection id in the Collection field. Alternatively, you can check all your collections on the Collection page. Collections can also be created, named, and managed (add/remove venues) through the API, but collections automatically created using the Venue Search tool will be named after the search query. By clicking on the collection id you can see a list of venues in the collection, or you can immediately open the collection in the Radar Tool.

Findings the right bar using filters
In previous sections, we discussed how to add new bars to your user account. Now discuss how to filter and display previously added bars that meet certain criteria.  For example, we want to show only the bars that are busy on Friday from 9 PM until 11 PM in a 1-kilometer radius around you (or any desired location).
We start with the Radar Tool zoomed and centered in San Francisco without any filters or loaded collections. You should see all previously added bars loaded.

On the right side of the screen, you can see the Filter panel. By adding filters we narrow down the currently loaded bars that meet the filter criteria.
Note: Each time a filter is applied, new data is loaded and credits will be charged (see venue Filter credits).
Filter on day of the week
By default, the Radar view shows the foot traffic data for the current time of the day (in the timezone of the map). First, we change the day to 'Friday'. The list and map data will now automatically show the foot traffic data for Friday.
Filter on foot traffic intensity
Now we would like to only display bars that will be at least 60% busy on Friday. We therefore set the 'Busy min' value to 60%. Now all bars will be displayed that will be at least 60% busy somewhere during the day (from 6 AM until 5AM the next day).  
Filter on time of day
The resulting bars could in theory also be only busy at 11 AM and quiet during the remainder of the day. Therefore we, filter also on time by setting the 'hour min' to '9 PM', and the 'hour max' to '11 PM'. Now all bars that are at least 60% busy anywhere from 9 Pm until 11 PM on Friday in San Francisco are displayed.  If you want to only show bars where ALL hours are at least 60% busy, then you can click the 'all' radio button below the minimum busyness filter. On the left side in the venue list you will see that the charts only show the foot traffic forecast for the filtered hours. The timeline on top of the map will also only indicate the selected hours.

Filter on location
The next step is to narrow down to bars in a specific location. Previously we added new venues in the Martina and Mission district using the Venue Search tool. This automatically created a collection id for that search request. So we could fill in the collection ID in the filter panel to filter the current set of bars only to bars previously found in e.g. the Mission district.
As an alternative to using a collection, we can filter down on geographical coordinates with a radius (using the API you can also filter on a bounding box instead of a radius).
We fill 37.759904 Deg latitude and -122.42562 Deg longitude in the location filter fields as the center of Mission District. We set the radius to 1000 meters, to only show bars in a 1 kilometer around the center of Mission District. If you move the map these values automatically update, so it's better to move to map to your desired view before filling in the coordinates and the radius.
Optionally, you could filter further on the rating, price level, and amount of reviews of the bar. Not all venues have a price level, therefore applying the price level filter removed all venues without that data from the results.

Showing data for the current hour
By selecting the 'Now' radio button in the Day & Time filter panel only foot-traffic data is loaded for today's current hour. The current hour is depending on the time zone of the map location. The charts in the left venue list view are now also replaced by gauges indicating the foot traffic intensity for the current hour. We now set the 'Busy' minimum value to 60% again to only show venues that are predicted to be at least 60% busy at this moment.

Real-time foot traffic data (live data)
So far we only applied filters on foot traffic forecast (prediction) data. This hourly forecast is made by analyzing visits to a venue in the past weeks. BestTime also provides live data for some venues. Click in the 'Day & Time' filter panel section on 'Live' to only show venues that have live data.
 Live data is based on the number of visits in the current hour of a venue. Live foot traffic data is also displayed as a relative percentage and is most useful to determine if it's currently much more or less busy than usual (compared to the foot traffic forecast). If the forecast indicates 70% and the Live foot traffic data indicates 40% as foot traffic prediction, it means that it is now approximately 30% less busy than usual for the current hour.  A forecasted value of 100% indicates the predicted foot traffic peak of the week. However, live data could go well above 100% in some cases. Then the live data indicates for example 140% it means that it is currently 40% more busy compared to the forecasted peak of the week.
Unfortunately, not all venues, that have foot traffic forecast data, have live data available. In general, the bigger or more popular venues have live data.  Live data is only available when a venue is open (in contrast to forecast data).
To save resources & API credits and increase the response speed, the Radar tool will load Live data without refreshing it. Click the 'Refresh Live data' checkbox to refresh the live data for all currently displayed venues. When you've added the bars in the past hour the data is fresh enough. You will notice this takes significantly longer to load the data.  We recommend refreshing the data only once per hour.

## BestTime beginners guide - Part 2 Software API

In Part 1 of this tutorial, we wrote how we can use the different BestTime.app website tools to add and analyze foot traffic data. In part 1 we first added bars to our user account. We used the Radar tool to filter the bars based on the amount of foot traffic on a specific day, time, and location. For example, we showed how to only show all the bars that are busy on Friday from 9 PM until 11 PM in the Mission District in San Francisco. In Part 2 we are going to take the same steps but now using the software API.

Add a single venue using the name and address
The New Foot Traffic Forecast API endpoint is used to add venues to your account using the name and address of the venue.

If BestTime was able to generate foot traffic data for the given venue it will look like the JSON response below. The JSON response is shortened since the whole response is too long to display here. Only limited data for Friday is shown, but normally it includes data for all days of the week. Click here for a full JSON response example. Check the API documentation for more explanation about the response data. Notice that besides foot traffic data and analyses the response also includes the venue_id. The venue_id can be used to get data from an existing forecast, without refreshing the foot traffic forecast (more discussed in Query foot traffic data).

If BestTime cannot provide foot traffic data for the requested address you will get an error message. The error message could contain that the venue is found but there is not enough data to provide foot traffic data. The error response could also indicate that the venue itself could not be found. Please check the address again. It could also respond that the venue could not be found if the address is not specific enough; e.g. there are multiple venues with the same name in a city. Later in the 'Venue Search' section we discuss how to add multiple venues at the same time to our account.
If you have a list of bars by name and address we can also simply create a loop to add multiple bars to your account (Python code only)

Query existing foot traffic data
Each time we use one of the API endpoints to get New foot-traffic data the generated foot traffic data is stored for a certain amount of days on your account. We can refresh the foot traffic by calling the same new foot traffic API endpoint. If we just need the same foot traffic data without generating fresh foot traffic predictions we could use the 'Query' API endpoints. These endpoints are cheaper (1 API credit vs 2 for new fresh foot traffic data) and respond much faster. Most query endpoints will be called using the HTTP 'GET' method as opposed to the 'New' foot traffic endpoints that require a HTTP 'POST' method'.
To query data from a venue you can use the venue_id from the 'New foot traffic data' response, or we can get a list of all the venue_id's in our account using the Venues API endpoint.

Using the Query endpoints you can get specific information like when the peak of the day starts, or which hours on Wednesday are quiet. Click here to see a list of all the Query endpoints.
The query endpoints not only return existing foot traffic data from your account but also provide additional analyses based on this data. The 'New foot traffic data API endpoint provides only static forecast data for the whole week. Most of the Query endpoints also include dynamic data in the API response. When you are for example interested to know which hour is predicted to be most busy you could use the Query Peaks endpoint. This endpoint does not only tell you at what time the peak hour is but will also dynamically tell you the time left until this moment: e.g. '2 Hours and 40 Minutes' until the peak of the day. It will also tell you if the peak is still coming or did already pass.
A new foot traffic data request provides the analyses for a whole week in one response. If you, for example, would like to quickly know how busy it is predicted to be at this moment you could use the 'Now' or 'Now Raw' endpoint. The 'Raw' endpoints return foot traffic data as a percentage from 0 to 100%, while the non-raw version of the endpoint returns textual information (e.g. 'above average' foot traffic as prediction).
Remember the query endpoints do not refresh the forecast foot traffic data itself. However, as you can see in the API documentation, it is possible to get data in the format of a specific query endpoint (e.g. Query Peaks) and refresh the forecast in one API call. This can be done by calling the API endpoint using the HTTP 'POST method instead of the 'GET' method. Remember this costs more API credits and takes longer to respond.
Live data
The previous API call returned foot traffic data based on foot traffic forecasts. BestTime has also live (real-time) data for a select number of venues (i.e. not all venues with foot traffic forecast data have live data). Additionally, live data is only available during the opening hours, whereas forecasts and query data can be retrieved regardless of the opening hours. Using the Live foot traffic data API endpoint we can get real-time foot traffic information:

The venue_live_busyness value contains a percentage indicating the foot traffic intensity for this hour. The forecast foot traffic percentages only go from 0% up to 100%, while the live data ranges from 0% to well above 100%. As mentioned before, 100% is the busiest peak of the week for a venue based on venue visits from the past weeks (for a bar this could be e.g. Friday 10 PM).
If a venue has for example an event and is much more busy than normal (compared to the busiest hours from the past week), the live value indicates a value above 100%. If there are now for example 50% MORE people than the busiest hour from last week the venue_live_forecasted_delta will indicate 50% and the venue_live_busyness will indicate 150%.  
In the response above the live data venue_live_busyness indicates that it is only 20% busy at this moment (Friday 3 PM).  The forecast for Friday 3 PM indicates venue_forecasted_busyness is it is normally 60% busy. The venue_live_forecasted_delta , therefore, indicates it is 40% LESS busy than normal (60% - 20%).
When the venue is closed or does not have live data at all the API call will return with an error message that there is no live data available at this moment. BestTime cannot tell you in advance which venues do have live data. The data is generated by comparing foot traffic data from the current hour at the venue with foot traffic data from the past weeks. This automated calculation depends on traffic volumes from the past week and current hour to determine if there is enough statistical power to display foot traffic data.  You might have more luck when trying it another time or day when there is no data at this moment.
Adding multiple venues using the 'Venue Search' tool
Let's say we don't know exactly the names of the bars, but we want to add some bars in the Mission District of San Francisco to our account.  We will use the 'Venue Search' API endpoint for this. This endpoint will accept text inputs (q parameter) like 'bars in Mission District San Francisco' or 'Whole Foods Market San Francisco'. As you can see from the example text inputs, you can add multiple venues by either specifying a type of venue (e.g. bar) or a name of a chain (e.g. Whole Foods Market, or McDonald's).
Text input parameter q also needs a location in combination with the type or name. This could be anything ranging from a country, or a city, to a neighborhood. So in hour bar example, we set q to bars in Mission District San Francisco. A location in q is always required unless a coordinate lat , lng and a radius is provided in the request. Otherwise, BestTime doesn't know where to search for your desired venues. You could for example use the coordinates of the Mission District (or the user's coordinates as input) in combination with q=bars to search for bars in that neighborhood without typing Mission District in q.
Multiple API endpoints are involved from entering a venue search input until returning foot-traffic data for the found venues. The Venue Search model will look up venues in the background and will forecast them subsequently (using the New Foot Traffic Forecast endpoint). Remember that this will therefore also result in additional forecast API credit usage. The endpoint will reply with a background task URL, job_id, and a collection_id (see Collections). You can poll the Venue Search Progress endpoint to poll to background job progress. We will now search for a maximum of 20 bars in the Mission District of San Francisco.
The higher the number of requested venues num the longer it takes for the search to complete. By default, the search speed method is set to fast=true.  To save free API credits we set the fast=fasle. Searching with the fast method is charged with more API credits (5x more at the time of writing). The fast method is limited to a maximum num of 60. Selecting a higher number will automatically use the normal speed method. Select false to save on API credits or to search for more than 60 venues at the same time. See API Credits for more info.

By repeatedly checking the Venue Search progress API endpoint get information on the progress of the background venue search job. You can do that using a normal API call or for now, just open the link from the previous response in your browser.

Once the background job is complete the same Venue Search Progress endpoint will give a JSON response like this:

 The response includes the found venue names, how many venues were found, how many venues have foot traffic data, etc. The response also includes the coordinates of the area the venues are located in. This is useful when showing the venues on a map. Both bounding box coordinates and the center of the map coordinate are provided.
The response does not include foot traffic data itself, but it provides two different links to get the foot traffic data: the venue_filter_api and radar_tool links. As the name suggests, when you open the radar_tool link in your web browser you will see the search results in the BestTime Radar tool (we discussed the Radar tool in Part 1 of this tutorial). The venue_filter_api link requests the foot traffic data through the Venue Filter API endpoint.
<http://besttime.app/api/v1/venues/filter?lat_min=37.7504268&lat_max=37.770023&lng_min=-122.424317&lng_max=-122.4083202&collection_id=col_5c546908473645c1b9bad36b7fef7765&api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&live_refresh=False>
In the next section, we discuss the Venue Filter itself. The Radar Tool makes also use if this API under the hood. When requesting foot traffic data through the Venue Filter you will see a response similar to this:

In the above example, the foot traffic data is displayed under the day_raw array. The day_raw consists out of 24 hours. By default, the Venue Filter tool responds with data for the current day of the week with the BestTime day window (6 AM until 5 AM next day.
Filter venues on foot traffic data, day, location & more
In the previous section, we searched for bars and got the foot traffic data through the Venue Filter API Endpoint. The Venue Filter API endpoint basically returns the foot traffic data of all venues in a specified geographic location, but makes it possible to filter the venues on e.g. foot traffic intensity, day of the week, time of the day, venue type, personal collections, ratings, number of reviews, and price levels. Due to these filter capabilities, it is a very powerful tool to only find venues that meet your criteria.
We can use this API endpoint to find within e.g. the busy bars on Friday from 9 PM until 11 PM on. How do we define 'busy'? As discussed before, BestTime indicates foot traffic intensity per hour as a percentage from 0 to 100%, wherein 100% is the hour with foot traffic peak of the week for a specific venue. For our bar use-case we tell the Venue filter to only show bars that are at least 70% busy compared to the peak of the week. As you can see from the Venue Filter API documentation we need to set the busy_min parameter to 70 to achieve this.
By default, the Venue Filter API will return with foot-traffic data for the current day of the week.  We set the day_int to 4 (Monday 0 to Sunday 6). We set the hour_min to 21 and the hour_max to 23  to only receive foot traffic data from 9 PM until 11 PM. Note that the API inputs are in 24-hour format.
It depends on your free/subscription plan how many API credits are charged for your Venue Filter API call. At the time of writing, the Free and Basic metered plans charge 1 API credit per 10 found Venues, and the Pro charges 1 API credit per 100 found Venues.
The Venue Filter endpoint requires geographical location parameters or a collection_id. When using the location parameters either a combination of a coordinate lat, lng, with a radius or  the bounding box parameters lat_min, lng_min, lat_max, and lng_max are required. If you just want to get all venues you could set the values to cover the whole world you could set the bounding box values to the maximum possible values lat_min=-90, lat_max=90, lng_min=-180, and lng_max=180 degrees. In the example API call below we use the coordinates of San Francisco in combination with a radius of 20000 meters (approx 65617 feet).

The Venue Filter will return a response like the JSON structure below. As you can see the raw_data array only includes foot traffic data for the hours from 9 PM until and including 11 PM. To be more precise, when we talk about foot traffic for 9 PM it means from 9:00 PM until 9:59 PM. So in this case the three values from the raw_data array (e.g. 75, 60, 40) are an indication of the foot traffic intensity from 9:00 PM until 11:59 PM.

By adding the now=true value to the Venue Filter API call the endpoint will return foot traffic data for the current hour of the venue. Also, all the filters (like minimum foot traffic intensity) are applied at this hour.
Sorting and paging
By default the Venue Filter API orders venues by number of reviews (descending from high to low) to place the more established venues on top of the list. This can be changed by setting order_by to one of the following values: reviews, rating, price_level, live, now, name, day_rank_max, day_rank_mean, day_max, day_mean, date,  dwell_time_min, dwell_time_max, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23.   Some values are self-explaining or can be searched in the API documentation. By default the order will be descending (from high to low). Using the order parameter the order can be set to desc (descending - from high to low) or asc (ascending - from low to high)(not to be confused with order_by).
 The live , now , and numbers from 0 to 23 will order the venues based on foot traffic intensity. So when e.g. using now the venues with the highest forecasted foot traffic at this hour (local time of the geographic filter area) will be shown on top. The numbers represent the 24 hours in a day in 24 hour format, and can be used to show venues with a foot traffic at a specific hour of the day. This is for example useful to e.g. find and show venues on top that are busy late at night.
See the response attributes of week overview API documentation for information regarding the day_rank_max,day_rank_mean,day_max,day_mean order values. The dwell time values order the venues based on how long visitors stay on average at a venue.
It is also possible to order venues by two values using the comma as seperator (without space) e.g. order_by=22,reviews. This will show venues with the highest foot traffic at 22:00 hour (10 PM) on top, and uses reviews as secondary order. The order parameter accepts also two comma seperated values - e.g. order=asc,desc - in case two order_by values are given.
By default the number of returned venues by the Venue Filter endpoint is set to 5000. In a lot of application use-case you might only want to show e.g. the top 20 venues, and include some sort of paging. This can be done by setting limit=20 and set page to the desired page number. The maximum limit per page is 10.000 venues. Note: The higher the number, the slower the response and the more API credits are used.
Filter live foot traffic data
The venue filter API endpoint also supports filtering on live foot traffic data using the live=true parameter in the API call.  Instead of calling the Live foot traffic endpoint for each individual venue, you can use the venue filter endpoint to get live data of multiple venues in one API call. When filtering on e.g. the live data in combination with the busy_min value we can easily find all bars that have actually foot traffic at this moment instead of depending on a forecast based on foot traffic data from the past weeks.
By default, this live data is not refreshed in order to save API credits and increase speed significantly. It is up to the user to decide how often this data is refreshed. The live data can be updated individually for each venue using the Live foot traffic endpoint. You can also pass  live_refresh=true as an additional parameter in the Venue Filter API call to get fresh live data of multiple venues.
Only venues that meet the venue filter criteria without the live parameter will be refreshed (e.g. filtered on location, collection, rating, reviews and price level). This only does not apply to the foot traffic intensity filters ( busy_min and busy_max). So if you e.g. filter on venues in a specific neighborhood with at least 1000 reviews,  with the minimum foot traffic intensity set to 50% ( busy_min=50), then all venues found in that neighborhood with that amount of reviews will be refreshed in the background, regardless of the forecasted foot traffic data values.
Once the live data is refreshed in the background the foot traffic intensity filters busy_min and busy_max are applied on the LIVE foot traffic values.  We are planning to add additional functionality in the future to filter based on the live_delta value. This way you can e.g. filter e.g. only display bars that are 40% more busy than usual. Please send us a message if you want this feature.
Adding filters to the Venue Search tool
As you can see in the Documentation the Venue Search endpoint also accepts most filter parameters similar to the Venue Filter API endpoint (e.g. busy_min and hour_min). It must be clarified that the Venue Search itself does not filter venues based on these filter parameters. The Venue Search endpoint searches venues and will create a link to the Venue Filter API endpoint including those filters!
When you use the Venue Search endpoint to search for q=Bars in Mission District in San Francisco in combination with busy_min=70, the will return all found bars in the mission district and add the ones with foot traffic data to your account. It will include a link to the Venue Filter API endpoint including the busy_min=70 filter.  
Besides the filter parameters, the Venue Search endpoint tries to understand textual filters from the text input q. When searching for example q=Busy bars in Mission District San Francisco on Friday from 9 PM until 11 PM, it will search for bars in Mission Disctrict San Francisco and converts the rest of the text into venue filters: busy_min=50 (at least 50% busy), day_int=4 (Friday), hour_min=21 (9PM), hour_max=23 (11 PM).
For more advanced options and info check Natural language in the search query as filters. As mentioned before the Venue Search tool is not extremely fast, but is useful when you don't know in advance which venues are desired. For use-cases that require faster performance, we recommend initially adding all desired venues once to your account. After that, you should only use the faster Venue Filter API endpoint to quickly filter your desired venues. We also recommend updating the foot traffic forecasts every 2 to 4 four weeks, since the Venue Filter API endpoint doesn't do this (it only filters existing foot traffic data added to your account).

</EMAIL TEMPLATES and tutorials>
