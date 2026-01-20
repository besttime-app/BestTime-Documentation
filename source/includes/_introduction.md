Here is a rewritten, polished version of the introduction. I have kept the original structure and sections but improved the clarity, flow, and formatting to make it more developer-friendly and professional.

***

# Introduction

Welcome to the BestTime.app documentation. This guide covers everything you need to know to integrate foot traffic data into your applications.

* **What is BestTime.app?** (See below)
* **[API Reference](#api-reference)** (Authentication, Endpoints, and Parameters)

## What is BestTime.app?

BestTime.app is a foot traffic data API service that forecasts how busy public venues (e.g., restaurants, gyms, parks, retail stores) will be at any given hour of the week.

The data covers 150+ countries and is derived from anonymized mobile signals.

**Key concepts:**

* **Forecasts:** Predictions based on historical visitor trends from recent weeks.
* **Relative Busyness:** Data is expressed as a percentage (0% to 100%), relative to that specific venue's peak traffic of the week.
* **Granularity:** Data is provided for every hour of the week.

> **Recommended Tutorials:**
>
> * [BestTime Tools: Beginners Tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
> * [Software API: Beginners Guide](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)

### Core Functionality

* **Live Updates:** Check if a venue is currently busier or quieter than usual (available for select high-traffic venues).
* **Advanced Analysis:** Access data on peak hours, quiet hours, dwell time, and surge hours (when people arrive/leave).
* **Venue Search:** Find venues by category (e.g., "Supermarkets in London") or specific name (e.g., "McDonald's in San Francisco").
* **Venue Filtering:** Sort and filter venues in a geographic area based on foot traffic, popularity, time of day, and more.
* **Integration:** Full REST-API access for seamless integration into your software or research.

## Use Cases

Here are a few ways developers and businesses utilize BestTime data:

* **Consumer Apps:** Show users the best time to visit museums, gyms, or theme parks to avoid queues.
* **Nightlife Discovery:** Find the most popular bars nearby right now, ensuring users don't end up in an empty venue.
* **Health & Wellness:** Compare local gyms to find the quietest one for a workout.
* **Operational Dashboards:** Inform staff (e.g., kitchen or reception) about current real-time traffic and predicted peaks for the coming hours.
* **Competitive Intelligence:** Compare your foot traffic against competitors to optimize marketing campaigns.
* **Behavioral Research:** Analyze macro-trends, such as standard peak hours for different industries (e.g., gyms often peak at 7 AM and 7 PM).

## Forecasts

To create a forecast, you simply provide the name and approximate address of a venue. BestTime analyzes available data to generate a foot traffic prediction.

### Supported Venues

BestTime works for public "Points of Interest" (POIs). Examples include:

* Restaurants, Bars, and Nightclubs
* Gyms and Sports Centers
* Shops, Malls, and Supermarkets
* Museums, Theaters, and Theme Parks
* Public Offices and Tourist Attractions

### Forecast Results

Generating a forecast takes a few seconds. The result is stored on the server for fast retrieval later. The data includes:

* **Weekly Overview:** Foot traffic intensity (0-100%) for every hour of the week.
* **Daily Analysis:** Peak busyness, average volume, and a comparative ranking of days (e.g., "Monday is the quietest day").
* **Hour Analysis:** A descriptive rating for each hour (rated on a scale from -2 to +2).
* **Peak Data:** Start time, end time, maximum intensity, and duration of peaks.
* **Surge Analysis:** The specific times when most visitors arrive or leave.
* **Lists:** Quick access lists for "Busy Hours" and "Quiet Hours."

### Relative Numbers vs. Absolute Numbers

BestTime provides **relative** foot traffic data, not absolute visitor counts.

* **0% to 100% Scale:** 100% represents the busiest hour of the week for that specific venue.
* **Intensity Score:** Hours are also rated on a 5-point scale (Low, Below Average, Average, Above Average, High).

### Coverage

We cover **150+ countries**.

* **Requirement:** A venue generally needs to be a public business with at least 100 visitors per week to generate statistically significant data.

### Updating Data

* **Forecasts:** Represents a "typical week" based on recent history. We recommend updating/refreshing forecasts once every 2–4 weeks using the *New Foot Traffic Forecast* endpoint.
* **Live Data:** Represents real-time activity. This must be refreshed every clock hour using the *Live Data* endpoint.
* **Venue Filter:** Returns cached data (never older than a month). For strictly fresh data, use the *New Foot Traffic Forecast* endpoint.

## Queries

There is a difference between **Generating** a forecast and **Querying** one.

1. **New Forecast:** Analyzes raw data to create a prediction. Takes a few seconds; costs more credits.
2. **Query:** Retrieves a previously generated forecast from the database. Instant response; costs fewer credits.

### Recommended Usage

To optimize performance and credit usage:

* Generate a **New Forecast** for a venue once every few weeks.
* Use **Queries** to retrieve that data as often as needed in between updates.
* Use the **Venue Filter** to retrieve data for multiple venues efficiently.

### Smart Attributes

Some query endpoints provide dynamic calculations on top of static data. For example, peak/surge analysis endpoints will calculate the "Time remaining until the next busy hour" (e.g., *"2.5 hours until peak"*).

### Query Endpoints

* **Venue Details:** Retrieve metadata for specific venues or lists of venues.
* **Full Forecast:** Retrieve the complete analysis for a venue.
* **Specific Analysis:** Query specific data points to reduce payload size:
  * Day or Week overview
  * Specific Hour or "Current Hour" (adjusted for venue timezone)
  * Lists of Busy, Quiet, Peak, or Surge hours

## Forecast Day Window (The "BestTime Day")

It is crucial to understand how BestTime handles the "day."

* **Standard Notation:** Hours are displayed from `0` (Midnight) to `23` (11 PM).
* **The Day Window:** A "BestTime Day" runs from **6 AM to 5 AM the next morning**, rather than Midnight to Midnight.

**Why?** This prevents data for nightlife venues (bars/clubs) from being split across two different days. A forecast for "Friday" includes the late-night hours of Friday night leading into Saturday morning (up to 5 AM).

### Data Array Example

The array index `0` corresponds to 6 AM, and index `23` corresponds to 5 AM the next day.

*Example: A restaurant that opens at 9 AM, has a lunch peak at 1 PM, a dinner peak at 9 PM, and closes at 3 AM.*

| Hour    | Array Index | Foot Traffic % | Note               |
|:--------|:----------:|:--------------:|:-------------------|
| 6 AM    | 0          | 0%             | Closed             |
| 7 AM    | 1          | 0%             |                    |
| 8 AM    | 2          | 0%             |                    |
| **9 AM**| **3**      | **10%**        | **Opens**          |
| 10 AM   | 4          | 15%            |                    |
| 11 AM   | 5          | 35%            |                    |
| 12 PM   | 6          | 50%            |                    |
| **1 PM**| **7**      | **65%**        | **Lunch Peak**     |
| 2 PM    | 8          | 45%            |                    |
| 3 PM    | 9          | 30%            |                    |
| 4 PM    | 10         | 25%            |                    |
| 5 PM    | 11         | 30%            |                    |
| 6 PM    | 12         | 40%            |                    |
| 7 PM    | 13         | 60%            |                    |
| 8 PM    | 14         | 80%            |                    |
| **9 PM**| **15**     | **90%**        | **Dinner Peak**    |
| 10 PM   | 16         | 80%            |                    |
| 11 PM   | 17         | 55%            |                    |
| 12 AM   | 18         | 40%            |                    |
| 1 AM    | 19         | 30%            |                    |
| 2 AM    | 20         | 20%            |                    |
| **3 AM**| **21**     | **0%**         | **Closes**         |
| 4 AM    | 22         | 0%             |                    |
| 5 AM    | 23         | 0%             | End of Day Window  |
