import requests
import time
import os
import sqlite3
from datetime import datetime, timedelta
import ujson as json  # Import json for working with JSON data in SQLite

# Configuration
# Set your API key as environment variable for security
PRIVATE_API_KEY = os.environ.get("PRIVATE_API_KEY")
PUBLIC_API_KEY = os.environ.get("PUBLIC_API_KEY")

CITIES = ["Houston, TX", "Dallas, TX", "Austin, TX", "San Antonio, TX",
          "El Paso, TX", "Albuquerque, NM", "Santa Fe, NM", "Las Cruces, NM"]
SEARCH_QUERY = "Walmart"
MAX_VENUES_PER_CITY = 20
REQUEST_DELAY = 2  # Delay in seconds between API requests to avoid rate limiting
OUTPUT_FILE = "walmart_foot_traffic_data_cached.md"
CACHE_DB_FILE = "api_cache.db"
CACHE_EXPIRY_HOURS = 1  # Cache expiry time in hours


def create_cache_table():
    """Creates the cache table in SQLite if it doesn't exist."""
    conn = sqlite3.connect(CACHE_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_cache (
            cache_key TEXT PRIMARY KEY,
            api_response TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()


def get_cached_response(cache_key):
    """Retrieves a cached API response from the database if it's valid."""
    conn = sqlite3.connect(CACHE_DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT api_response, timestamp FROM api_cache WHERE cache_key = ?", (cache_key,))
    result = cursor.fetchone()
    conn.close()

    if result:
        api_response_text, timestamp_str = result
        timestamp = datetime.fromisoformat(timestamp_str)
        if datetime.now() < timestamp + timedelta(hours=CACHE_EXPIRY_HOURS):
            return json.loads(api_response_text)  # Load JSON from cached text
    return None


def cache_api_response(cache_key, api_response):
    """Caches an API response in the database."""
    conn = sqlite3.connect(CACHE_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO api_cache (cache_key, api_response, timestamp) VALUES (?, ?, ?)",
                   (cache_key, json.dumps(api_response), datetime.now().isoformat()))  # Store JSON as text
    conn.commit()
    conn.close()


def get_venues_by_search(city, query, api_key, max_venues):
    """
    Searches for venues using the BestTime Venue Search API and returns venue details, with caching.
    """
    cache_key = f"venues_search_{city}_{query}_{max_venues}"
    cached_response = get_cached_response(cache_key)
    if cached_response:
        print(f"  [Cache Hit] Venue Search for {city}")
        return cached_response

    url = "https://besttime.app/api/v1/venues/search"
    headers = {"Content-Type": "application/json"}
    params = {
        "api_key_private": PRIVATE_API_KEY,
        "q": f"{query} in {city}",
        "num": max_venues,
        "fast": False,  # Use 'True' for faster but more expensive search
        "format": "all"
    }

    try:
        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()

        search_progress_url = response.json(
        )["_links"]["venue_search_progress"]

        while True:
            progress_response = requests.get(search_progress_url)
            progress_response.raise_for_status()
            progress_data = progress_response.json()

            if progress_data["job_finished"]:
                venues_data = [
                    venue for venue in progress_data["venues"] if venue["forecast"]]
                # Cache the venue data
                cache_api_response(cache_key, venues_data)
                return venues_data

            time.sleep(REQUEST_DELAY)

    except requests.exceptions.RequestException as e:
        print(f"Error during venue search for {city}: {e}")
        return []


def get_live_data(venue_id, api_key):
    """
    Retrieves live foot traffic data for a venue using the BestTime Live API, with caching.
    """
    cache_key = f"live_data_{venue_id}"
    cached_response = get_cached_response(cache_key)
    if cached_response:
        print(f"  [Cache Hit] Live Data for venue {venue_id}")
        return cached_response

    url = "https://besttime.app/api/v1/forecasts/live"
    params = {
        "api_key_private": PRIVATE_API_KEY,
        "venue_id": venue_id
    }

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "OK" and data["analysis"]["venue_live_busyness_available"]:
            live_data_response = {
                "name": data["venue_info"]["venue_name"],
                "address": data["venue_info"]["venue_address"],
                "venue_live_forecasted_delta": data["analysis"]["venue_live_forecasted_delta"],
                "live_percentage": data["analysis"]["venue_live_busyness"]
            }
            # Cache live data response
            cache_api_response(cache_key, live_data_response)
            return live_data_response
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching live data for venue {venue_id}: {e}")
        return None


def get_week_forecast_data(venue_id, api_key):
    """
    Retrieves the whole week's foot traffic forecast data for a venue, with caching.
    """
    cache_key = f"week_forecast_{venue_id}"
    cached_response = get_cached_response(cache_key)
    if cached_response:
        print(f"  [Cache Hit] Week Forecast Data for venue {venue_id}")
        return cached_response

    url = "https://besttime.app/api/v1/forecasts/week"
    params = {
        "api_key_public": PUBLIC_API_KEY,
        "venue_id": venue_id
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        week_forecast_response = response.json()
        # Cache week forecast data
        cache_api_response(cache_key, week_forecast_response)
        return week_forecast_response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching week forecast data for venue {venue_id}: {e}")
        return None


if __name__ == "__main__":
    if not PRIVATE_API_KEY or PRIVATE_API_KEY == "YOUR_PRIVATE_API_KEY":
        print("Error: Please set your BestTime private API key as the environment variable 'PRIVATE_API_KEY' or replace 'YOUR_PRIVATE_API_KEY' in the script.")
        exit()
    if not PUBLIC_API_KEY:
        PUBLIC_API_KEY = PRIVATE_API_KEY.replace(
            "pri_", "pub_")  # Derive public key if not set

    create_cache_table()  # Ensure cache table exists

    all_venues_data = []
    for city in CITIES:
        print(f"Searching for {SEARCH_QUERY} venues in {city}...")
        venues = get_venues_by_search(
            city, SEARCH_QUERY, PRIVATE_API_KEY, MAX_VENUES_PER_CITY)
        if venues:
            print(f"Found {len(venues)} venues in {city}.")
            all_venues_data.extend(venues)
        else:
            print(f"No venues found for {city}.")
        time.sleep(REQUEST_DELAY)

    print(
        f"\nRetrieving live data and week forecast for {len(all_venues_data)} venues... Please wait {len(all_venues_data) * REQUEST_DELAY} seconds")
    output_data = []
    for venue in all_venues_data:
        live_data = get_live_data(venue["venue_id"], PRIVATE_API_KEY)
        week_forecast_data = get_week_forecast_data(
            venue["venue_id"], PUBLIC_API_KEY)

        venue_output = {
            "name": venue["venue_name"],
            "address": venue["venue_address"],
            "venue_live_forecasted_delta": "N/A",
            "live_percentage": "N/A",
            "week_foot_traffic_json": "N/A"
        }

        if live_data:
            venue_output["venue_live_forecasted_delta"] = f"{live_data['venue_live_forecasted_delta']}%"
            venue_output["live_percentage"] = f"{live_data['live_percentage']}%"

        if week_forecast_data:
            venue_output["week_foot_traffic_json"] = week_forecast_data

        output_data.append(venue_output)
        time.sleep(REQUEST_DELAY)

    # Prepare markdown table
markdown_table = "| Name | Address | Live Delta | Current Live Data  |\n"
markdown_table += "|---|---|---|---|---|\n"
for venue_data in output_data:
    markdown_table += f"| {venue_data['name']} | {venue_data['address']} | {venue_data['venue_live_forecasted_delta']} | {venue_data['live_percentage']} | \n"

# Save to markdown file
with open(OUTPUT_FILE, "w") as f:
    f.write(markdown_table)

print(f"\nData saved to {OUTPUT_FILE}")
print("Markdown Table Output Preview:")
print(markdown_table)