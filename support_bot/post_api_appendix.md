<HTML example>
Venue Day Foot Traffic with live data

===
<!DOCTYPE html>
<html>
<body>

<h1>BestTime API - Today's foot traffic chart example</h1>
<p>A demo using the <a href="https://besttime.app/?utm_source=besttime&utm_campaign=examples">BestTime</a> <a href="https://documentation.besttime.app/?javascript#new-foot-traffic-forecast?utm_source=besttime&utm_campaign=examples">New Foot Traffic Forecast</a> and <a href="https://documentation.besttime.app/?javascript#live-foot-traffic-data">Live</a> API endpoint. Vizualized using <a href="https://echarts.apache.org/en/index.html">eCharts</a></p>

<div>
    <form>
        <label for="api_key_private">Insert here your BestTime <a target="_blank" href="https://besttime.app/api/v1/api_keys_list">private API key</a></label><br>
        <input type="text" id="api_key_private" placeholder="Your private API Key" value="pri_xxxx" />
        <p>Never use your private API key on your own public website to avoid abuse. Only use it on this page for testing purposes. Get the API data through your back-end or use the public API key in combination with a <a href="https://documentation.besttime.app/#query-week-raw">query</a> API endpoint</p>
    </form>
    <form>
        <label for="api_key_private">Type a venue name and address and press the Forecast button</label><br>
        <input type="text" id="venue_name" placeholder="Venue Name" value="Central Park" />
        <input type="text" id="venue_address" placeholder="Venue Address" value="New York City Manhattan New York County" />
        <button id="btnForecast" type="submit">Foot Traffic Forecast</button>
    </form>
</div>
<br>

<!-- The div where the chart will be shown. A width and heigth is required for eCharts -->
<div id="footTrafficDay" style="width:800px; height:300px;" ></div>

<p>Check out the <a href="https://blog.besttime.app/tag/tutorials/">BestTime tutorial section</a> for more information</p>
</body>
</html>

<!-- eCharts is used to generate the graph -->
<script src="https://cdn.jsdelivr.net/npm/echarts@4.7.0/dist/echarts.min.js"
integrity="sha256-eKrx6Ly6b0Rscx/PSm52rJsvK76RJyv18Toswq+OLSs=" crossorigin="anonymous"></script>

<!-- Script to get the foot traffic from the BestTime API and vizualize the data using eCharts -->
<script>

// Graph options
var option = {
    title: {
        text: "Today's foot traffic",
    },
    tooltip: {
        show: true,
        formatter: '{c}% vs max <br> max of the week'
    },
    xAxis: {
        show: true,
        nameTextStyle: {
        color: "#b5b5b5"
        },
        axisLine: {
        show: false
        },
        axisTick: {
        show: false
        },
        axisLabel: {
        show: true,
        showMinLabel: true,
        showMaxLabel: true,
        interval: 3,
        color: "#b5b5b5",
        align: 'center'
        },
        //   nameGap: 40,
        data: ['6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM',
        '7PM', '8PM', '9PM', '10PM', '11PM', '12AM', '1AM', '2AM', '3AM', '4AM', '5AM']
    },
    yAxis: {
        show: true,
        min: 0,
        max: 100,
        interval: 100,
        // name: "Busyness",
        // nameLocation: 'middle',
        // nameTextStyle: {
        //     color: "#b5b5b5"
        // },
        axisLine: {
        show: false
        },
        axisTick: {
        show: false,
        },
        axisLabel: {
        show: true,
        interval: 100,
        showMaxLabel: true,
        showMinLabel: false,
        color: "#b5b5b5",
        // align: 'left',
        formatter: function (value) {
            return value + "%";
        }
        },
        splitline: {
        show: false
        }
    },
    grid: {
        left: 40,
        top: 30,
        right: 0,
        bottom: 20
    },
    series: [{
        type: 'bar'
    }]
};

// Preconfig chart with basic options
// Based on prepared DOM, initialize echarts instance
var chartToday = echarts.init(document.getElementById("footTrafficDay"));
chartToday.setOption(option);
chartToday.showLoading({
    text: 'Insert your private API key and press the Forecast button',
});

// let data;
// let dataToday;
// let dataLive;

// Find the current day of the week to show only today's
const d = new Date();
// Javascript getDay returns 0-6 where 0 is Sunday and 6 is Saturday
// BestTime API returns 0-6 where 0 is Monday and 6 is Sunday
let dayInt =  d.getDay() < 6 ? d.getDay() + 1 : 0;
console.log(dayInt);

function getFootTrafficData() {

    const params = new URLSearchParams({
    'api_key_private': document.getElementById("api_key_private").value,
    'venue_name': document.getElementById("venue_name").value,
    'venue_address': document.getElementById("venue_address").value
    });

    fetch(\`https://besttime.app/api/v1/forecasts?\${params}\`, {
    method: 'POST'
    }).then((response) => response.json())
    .then((data) => {
        document.getElementById("btnForecast").disabled = false;

        if (data.status == "error") {

        if ('message' in data) {
            console.log();
            if ('api_key_private' in data) {
                alert(JSON.stringify(data.message.api_key_private[0]))
            } else {
                alert(JSON.stringify(data.message))
                console.log(data.message)
            }
        }
        } else {
            dataToday = data['analysis'][dayInt.toString()]

            // Show all foot traffic forecast percentages in the console from 6AM until 5AM next morning.
            console.log(dataToday);

            chartToday.hideLoading();
            chartToday.setOption({
                title: {
                    text: "Today's foot traffic for " + data.venue_info.venue_name + " " + data.venue_info.venue_address,
                },
                series: [{
                name: "Forecasted busyness",
                clip: false,
                type: 'bar',
                itemStyle: {
                    color:"#7dabf4"
                },
                z: 0,
                data: dataToday.day_raw
                }]});

        }

    })
    .catch(console.error);

    // Add Live data to the same chart
    fetch(\`https://besttime.app/api/v1/forecasts/live?\${params}\`, {
    method: 'POST'
    }).then((response) => response.json())
    .then((dataLive) => {

        // Show all live data in the console
        console.log(dataLive);

        if (dataLive.status == "OK") {

            pct = dataLive.analysis.venue_live_busyness;

            // Scale yaxis higher if we have a live number higher than 100%
            if (pct > 100) {
                yaxisMax = pct
            } else {
                yaxisMax = 100;
            }

            if (pct > 80) {
                liveLabelOffsetHor = 30;
            } else {
                liveLabelOffsetHor = -5;
            }

            // If 5am adjust x-axis to prevent a day wide live bar
            hour_start_12 = dataLive.analysis.hour_start_12
            hour_end_12 = dataLive.analysis.hour_end_12
            if (hour_start_12 == "5AM") {
                hour_end_12 = "";
            }

            // Includes duplicate code for yAxis, this is done on purpose
            chartToday.setOption({
                yAxis: {
                    show: true,
                    min: 0,
                    max: yaxisMax,
                    axisLine: {
                    show: false
                    },
                    axisTick: {
                    show: false,
                    },
                    axisLabel: {
                    show: true,
                    interval: 100,
                    showMaxLabel: true,
                    showMinLabel: false,
                    color: "#b5b5b5",
                    // align: 'left',
                    formatter: function (value) {
                        return value + "%";
                    }
                    }
                },
                series: [{
                    "name": "Live busyness",
                    "markArea": {
                    "label": {
                        "show": true,
                        "position": [liveLabelOffsetHor, "100%"],
                        "offset": [0, -210],
                        "fontSize": 20,
                        "color": 'white',
                        "backgroundColor": "#f50057",
                        "distance": 'top'
                    },
                    "silent": false,
                    "data": [
                        [{
                        "name": "Live",
                        //"type": 'min',
                        "yAxis": 0,
                        "value": pct,  //Live value tooltip.
                        "xAxis": hour_start_12,
                        "itemStyle": {
                            "color": "#f50057",
                            "shadowBlur": 30,
                            "shadowOffsetX": 1,
                            "opacity": 0.5
                        }
                        }, {
                        "yAxis": pct,
                        "xAxis": hour_end_12,
                        }]
                    ]
                    }
                }]
                });

        }

    })
    .catch(error => {
        console.error;
        document.getElementById("btnForecast").disabled = false;
    });
}

// Load on page load
//getFootTrafficData();

// Reload the forecast data when clicking the Forecast button
document.getElementById("btnForecast").addEventListener('click', (event) => {
    event.preventDefault();

    document.getElementById("btnForecast").disabled = 'true';

    getFootTrafficData();
});

</script>
===

</HTML example>

<HTML example>
# Venue foot traffic week heatmap example
<!DOCTYPE html>
<html>
<head>
    <!-- ApexCharts CSS file -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/apexcharts/3.17.1/apexcharts.min.css"
  integrity="sha256-Z+b0591KmC0xEn2bVTikG6Ic6LzwqrV5x7IXZpTKI2o=" crossorigin="anonymous" />
</head>
<body>

<h1>BestTime API - Week foot traffic heatmap example</h1>
<p>A demo using the <a target="_blank" href="https://besttime.app/?utm_source=besttime&utm_campaign=examples">BestTime</a> <a target="_blank" href="https://documentation.besttime.app/?javascript#new-foot-traffic-forecast">New Foot Traffic Forecast</a> API endpoint. Vizualized using <a target="_blank" href="https://echarts.apache.org/en/index.html">eCharts</a></p>

<div>
    <form>
        <label for="api_key_private">Insert here your BestTime <a target="_blank" href="https://besttime.app/api/v1/api_keys_list">private API key</a></label><br>
        <input type="text" id="api_key_private" placeholder="Your private API Key" value="pri_xxxx" />
        <p>Never use your private API key on your own public website to avoid abuse. Only use it on this page for testing purposes. Get the API data through your back-end or use the public API key in combination with a <a href="https://documentation.besttime.app/#query-week-raw">query</a> API endpoint</p>
    </form>
    <br>
    <form>
        <label for="api_key_private">Type a venue name and address and press the Forecast button</label><br>
        <input type="text" id="venue_name" placeholder="Venue Name" value="Central Park" />
        <input type="text" id="venue_address" placeholder="Venue Address" value="New York City Manhattan New York County" />
        <button id="btnForecast" type="submit">Foot Traffic Forecast</button>
    </form>
</div>
<br>

<!-- The div where the chart will be shown. A width and heigth is required -->
<div id="footTrafficWeekHeatmap" style="width:800px; height:600px;" ></div>

<p>Check out the <a target="_blank"  href="https://blog.besttime.app/tag/tutorials/?utm_source=besttime&utm_campaign=examples">BestTime tutorial section</a> for more information</p>
</body>
</html>

<!-- ApexCharts is used to generate the graph -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/apexcharts/3.8.6/apexcharts.min.js"
integrity="sha256-fPasH9WrBndkSzQggD2jDhtCOJ8MapJPWFDUjLGPNPM=" crossorigin="anonymous"></script>

<!-- Script to get the foot traffic from the BestTime API and vizualize the data using eCharts -->
<script>

// Heatmap colors and categories
var busyCategories = {
    notBusy: {
        min: 1,
        max: 39,
        name: 'Not busy',
        color: '#00A100'
    },
    littleBusy: {
        min: 40,
        max: 69,
        name: 'Little busy',
        color: '#FFB200'
    },
    Busy: {
        min: 70,
        max: 500,
        name: "Busy",
        color: '#FF0000'
    }
}

var sampleData = [0, 5, 10, 10, 15, 40, 30, 20, 15, 20, 30, 50, 60, 70, 90, 70, 40, 10, 0, 0, 0, 0, 0];

// Graph options
var options = {
        series: [
            {
                name: 'Sun',
                data: sampleData
            },
            {
                name: 'Sat',
                data: sampleData
            },
            {
                name: 'Fri',
                data: sampleData
            },
            {
                name: 'Thu',
                data: sampleData
            },
            {
                name: 'Wed',
                data: sampleData
            },
            {
                name: 'Tue',
                data: sampleData
            },
            {
                name: 'Mon',
                data: sampleData
            }
        ],
        chart: {
            height: 350,
            type: 'heatmap',
        },
        plotOptions: {
            heatmap: {
                shadeIntensity: 0.5,
                //radius: 10,
                useFillColorAsStroke: true,
                colorScale: {
                    ranges: [
                        //{
                        //     from: 0,
                        //     to: 1,
                        //     name: 'Closed',
                        //     color: '#00A100'
                        // },
                        {
                            from: busyCategories.notBusy.min,
                            to: busyCategories.notBusy.max,
                            name: busyCategories.notBusy.name,
                            color: busyCategories.notBusy.color
                        },
                        {
                            from: 40,
                            to: 69,
                            name: 'Usually a little busy',
                            color: '#FFB200'
                        },
                        {
                            from: 70,
                            to: 100,
                            name: 'As busy as it gets',
                            color: '#FF0000'
                        }
                    ]
                }
            }
        },
        dataLabels: {
            enabled: false,
            formatter: function (val) {
                return val + "%";
            }
        },
        xaxis: {
            labels: {
                rotate: 90,
                rotateAlways: true,
                trim: false,
                hideOverlappingLabels: true,
                //min: 4, //clip x-axis based on category index
                //max: 10,
                offsetY: 25,
            },
            categories: ['6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM',
                '7PM', '8PM', '9PM', '10PM', '11PM', '12AM', '1AM', '2AM', '3AM', '4AM', '5AM'],
            tickPlacement: 'between' // 'on'
        },
        axisTicks: {
            show: true,
            borderType: 'solid',
            color: '#78909C',
            height: 6,
            offsetX: 0,
            offsetY: 0
        },
        stroke: {
            width: 1
        },
        title: {
            text: 'Week foot traffic forecast'
        },
        tooltip: {
            enabled: true,
            x: {
                show: false
              },
            y: {
                formatter: function(value, { series, seriesIndex, dataPointIndex, w }) {

                  return  value + "%";
                }
              },
            fixed: {
                enabled: false,
                position: 'topLeft',
                offsetX: 0,
                offsetY: 0,
            },
            // x: {
            //   format: 'HH'
            // },
        },
    };

chart = new ApexCharts(document.querySelector("#footTrafficWeekHeatmap"), options);
chart.render();

function getFootTrafficData() {

    const params = new URLSearchParams({
    'api_key_private': document.getElementById("api_key_private").value,
    'venue_name': document.getElementById("venue_name").value,
    'venue_address': document.getElementById("venue_address").value
    });

    fetch(\`https://besttime.app/api/v1/forecasts?\${params}\`, {
    method: 'POST'
    }).then((response) => response.json())
    .then((data) => {

        console.log(data)

        document.getElementById("btnForecast").disabled = false;

        if (data.status == "error") {

            if ('message' in data) {
                console.log();
                if ('api_key_private' in data) {
                    alert(JSON.stringify(data.message.api_key_private[0]))
                } else {
                    alert(JSON.stringify(data.message))
                    console.log(data.message)
                }
            }
        } else {

            // Find longest opening hours of the week
            open_ix = []
            close_ix = []

            data.analysis.forEach(function (item, index) {
                venue_open = item.day_info.venue_open;
                venue_closed = item.day_info.venue_closed;

                if (venue_open != "Closed") {
                    open_ix.push(hour2index(venue_open));
                    close_ix.push(hour2index(venue_closed));
                }
            });

            open_ix_min = Math.min(...open_ix);
            close_ix_max = Math.max(...close_ix);

            if (open_ix_min > close_ix_max || open_ix_min == close_ix_max )  {
                // Do not slice if open hour has greater index value than close (e.g. close and opens midnight)
                open_ix_min = 0;
                close_ix_max = 23;
            } else {

                // Adjust
                //open_ix_min = 0;
                close_ix_max = close_ix_max;
            }

            chart.updateOptions({
                title: {
                    text: 'Week foot traffic forecast for ' + data.venue_info.venue_name + ' ' + data.venue_info.venue_address
                },
                xaxis: {
                    // The hours for the X-axis are sliced to the range of the longest opening hours of the week
                    categories: ['6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM',
                    '7PM', '8PM', '9PM', '10PM', '11PM', '12AM', '1AM', '2AM', '3AM', '4AM', '5AM'].slice(open_ix_min, close_ix_max)
                }
            });

            chart.updateSeries([
                {
                    name: 'Sun',
                    data: data.analysis[6].day_raw.slice(open_ix_min, close_ix_max)
                },
                {
                    name: 'Sat',
                    data: data.analysis[5].day_raw.slice(open_ix_min, close_ix_max)
                },
                {
                    name: 'Fri',
                    data: data.analysis[4].day_raw.slice(open_ix_min, close_ix_max)
                },
                {
                    name: 'Thu',
                    data: data.analysis[3].day_raw.slice(open_ix_min, close_ix_max)
                },
                {
                    name: 'Wed',
                    data: data.analysis[2].day_raw.slice(open_ix_min, close_ix_max)
                },
                {
                    name: 'Tue',
                    data: data.analysis[1].day_raw.slice(open_ix_min, close_ix_max)
                },
                {
                    name: 'Mon',
                    data: data.analysis[0].day_raw.slice(open_ix_min, close_ix_max)
                }
            ])

        }

    })
    .catch(error => {
        console.error;
        document.getElementById("btnForecast").disabled = false;
    });

}

// Load on page load
//getFootTrafficData();

// Reload the forecast data when clicking the Forecast button
document.getElementById("btnForecast").addEventListener('click', (event) => {
    event.preventDefault();

    document.getElementById("btnForecast").disabled = 'true';

    getFootTrafficData();
});

// Convert the hour to the correct array index value
function hour2index(hour) {

if (hour >= 6 && hour <= 23) {
    index = hour - 6
} else {
    index = hour + 18
}

// console.log(hour, index)

return index
}

</script>

# BestTime Heatmap Venue Filter HTML example

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BestTime Venue Filter Map</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        #map { height: 70vh; } /* Main map takes up 70% of viewport height */
        .venue-list { height: 70vh; overflow-y: auto; } /* Match map height */
        .venue-item:hover { background-color: #f0f0f0; cursor: pointer; }
        .leaflet-marker-icon { border: 2px solid white; border-radius: 50%; }
        .busy-low { background-color: green; }
        .busy-medium { background-color: orange; }
        .busy-high { background-color: red; }
        .filter-panel {
            height: 15vh;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            border-top: 1px solid #dee2e6;
            padding: 1rem;
            z-index: 1000;
            overflow-y: auto;
        }
        .main-content {
            margin-bottom: 15vh; /* Match filter panel height */
        }
        /* New styles for venue details overlay */
        .venue-details-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 15vh; /* Leave space for filter panel */
            background: rgba(255, 255, 255, 0.95);
            z-index: 2000;
            padding: 20px;
            overflow-y: auto;
        }
        .venue-details-content {
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
        }
        .close-overlay {
            position: absolute;
            top: 10px;
            right: 10px;
            font-size: 24px;
            cursor: pointer;
            z-index: 2001;
        }
        #venueHeatmap {
            width: 100%;
            height: 400px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container-fluid">
    <!-- <h1>BestTime Venue Filter Map</h1> -->

    <div class="row main-content">
        <div class="col-md-4">
            <!-- <h2>Venues List</h2> -->
            <div id="venueList" class="venue-list p-3 border rounded">
                <!-- Venue list will be populated here -->
            </div>
        </div>
        <div class="col-md-8">
            <!-- <h2>Venue Map</h2> -->
            <div id="map" class="border rounded"></div>
        </div>
    </div>

    <!-- Replace overlay with Bootstrap modal -->
    <div class="modal fade" id="venueDetailsModal" tabindex="-1" aria-labelledby="venueDetailsModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-fullscreen">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="venueDetailsTitle"></h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p id="venueDetailsAddress" class="text-muted"></p>
                    <div id="venueHeatmap"></div>
                </div>
            </div>
        </div>
    </div>

    <div class="filter-panel">
        <div class="row">
            <div class="col-md-2">
                <div class="mb-2">
                    <label for="busy_min" class="form-label">Min Busyness (%)</label>
                    <input type="number" class="form-control form-control-sm" id="busy_min" placeholder="0">
                </div>
            </div>
            <div class="col-md-2">
                <div class="mb-2">
                    <label for="busy_max" class="form-label">Max Busyness (%)</label>
                    <input type="number" class="form-control form-control-sm" id="busy_max" placeholder="100">
                </div>
            </div>
            <div class="col-md-2">
                <div class="mb-2">
                    <label for="hour_min" class="form-label">Hour Min (24h)</label>
                    <input type="number" class="form-control form-control-sm" id="hour_min" placeholder="0">
                </div>
            </div>
            <div class="col-md-2">
                <div class="mb-2">
                    <label for="hour_max" class="form-label">Hour Max (24h)</label>
                    <input type="number" class="form-control form-control-sm" id="hour_max" placeholder="23">
                </div>
            </div>
            <div class="col-md-2">
                <div class="mb-2">
                    <label for="day_int" class="form-label">Day (0-6, Mon-Sun)</label>
                    <input type="number" class="form-control form-control-sm" id="day_int" placeholder="Optional">
                </div>
            </div>
            <div class="col-md-2">
                <div class="mb-2">
                    <label for="types" class="form-label">Venue Types</label>
                    <input type="text" class="form-control form-control-sm" id="types" placeholder="BAR,RESTAURANT">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12 text-center">
                <button id="applyFilters" class="btn btn-primary">Apply Filters & Update Map</button>
            </div>
        </div>
    </div>
</div>

<!-- API Key Modal -->
<div class="modal fade" id="apiKeyModal" data-bs-backdrop="static" tabindex="-1" aria-labelledby="apiKeyModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="apiKeyModalLabel">BestTime API Key Required</h5>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                    <label for="api_key_private" class="form-label">BestTime Private API Key</label>
                    <input type="text" class="form-control" id="api_key_private" placeholder="Enter your private API key">
                    <div class="form-text">Your private API key will be saved in your browser for future use.</div>
                </div>
                <div class="mb-3">
                    <label for="api_key_public" class="form-label">BestTime Public API Key</label>
                    <input type="text" class="form-control" id="api_key_public" placeholder="Enter your public API key">
                    <div class="form-text">Your public API key will be saved in your browser for future use.</div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" id="saveApiKey">Save API Key</button>
            </div>
        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<!-- Add ApexCharts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/apexcharts/3.8.6/apexcharts.min.js"></script>
<script>
    // Function to reduce coordinate decimals
    function reduceCoordinateDecimals(coord) {
        return parseFloat(coord.toFixed(2));
    }

    // Convert hour to array index (copied from radar.js)
    function hour2index(hour) {
        if (hour >= 6 && hour <= 23) {
            index = hour - 6
        } else {
            index = hour + 18
        }
        return index
    }

    // Initialize heatmap chart options
    const heatmapOptions = {
        series: [
            { name: 'Sun', data: [] },
            { name: 'Sat', data: [] },
            { name: 'Fri', data: [] },
            { name: 'Thu', data: [] },
            { name: 'Wed', data: [] },
            { name: 'Tue', data: [] },
            { name: 'Mon', data: [] }
        ],
        chart: {
            height: 350,
            type: 'heatmap',
        },
        plotOptions: {
            heatmap: {
                shadeIntensity: 0.5,
                useFillColorAsStroke: true,
                colorScale: {
                    ranges: [
                        {
                            from: 1,
                            to: 39,
                            name: 'Not busy',
                            color: '#00A100'
                        },
                        {
                            from: 40,
                            to: 69,
                            name: 'Usually a little busy',
                            color: '#FFB200'
                        },
                        {
                            from: 70,
                            to: 100,
                            name: 'As busy as it gets',
                            color: '#FF0000'
                        }
                    ]
                }
            }
        },
        dataLabels: {
            enabled: false
        },
        xaxis: {
            labels: {
                rotate: 90,
                rotateAlways: true,
                trim: false,
                hideOverlappingLabels: true,
                offsetY: 25,
            },
            categories: ['6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM',
                '7PM', '8PM', '9PM', '10PM', '11PM', '12AM', '1AM', '2AM', '3AM', '4AM', '5AM'],
            tickPlacement: 'between'
        },
        title: {
            text: 'Week foot traffic forecast'
        }
    };

    let venueHeatmapChart = null;
    let venueDetailsModal = null;

    function showVenueDetails(venue) {
        $('#venueDetailsTitle').text(venue.venue_name);
        $('#venueDetailsAddress').text(venue.venue_address);

        // Show modal while loading data
        if (!venueDetailsModal) {
            venueDetailsModal = new bootstrap.Modal(document.getElementById('venueDetailsModal'));
        }
        venueDetailsModal.show();

        // Get week data from API using public key
        const params = {
            'api_key_public': $('#api_key_public').val(),
            'venue_id': venue.venue_id
        };

        $.ajax({
            url: 'https://besttime.app/api/v1/forecasts/week/raw2',
            method: 'GET',
            data: params,
        }).fail(function(err) {
            console.error("Error fetching week data:", err);
            if (err.responseJSON && err.responseJSON.message) {
                alert(err.responseJSON.message);
            }
        }).done(function(data) {
            // Find longest opening hours of the week
            let open_ix = [];
            let close_ix = [];

            data.analysis.week_raw.forEach(function(item) {
                const venue_open = item.day_info.venue_open;
                const venue_closed = item.day_info.venue_closed;

                if (venue_open !== "Closed") {
                    open_ix.push(hour2index(venue_open));
                    close_ix.push(hour2index(venue_closed));
                }
            });

            let open_ix_min = Math.min(...open_ix);
            let close_ix_max = Math.max(...close_ix);

            if (open_ix_min > close_ix_max || open_ix_min === close_ix_max) {
                // Do not slice if open hour has greater index value than close (e.g. close and opens midnight)
                open_ix_min = 0;
                close_ix_max = 23;
            }

            // Destroy existing chart if it exists
            if (venueHeatmapChart) {
                venueHeatmapChart.destroy();
            }

            // Create new chart with venue data
            const chartOptions = {...heatmapOptions};
            chartOptions.title.text = \`Week foot traffic forecast for \${venue.venue_name}\`;

            // Update x-axis categories to only show opening hours
            chartOptions.xaxis.categories = heatmapOptions.xaxis.categories.slice(open_ix_min, close_ix_max + 1);

            // Update series data with sliced hours
            chartOptions.series = [
                { name: 'Sun', data: data.analysis.week_raw[6].day_raw.slice(open_ix_min, close_ix_max + 1) },
                { name: 'Sat', data: data.analysis.week_raw[5].day_raw.slice(open_ix_min, close_ix_max + 1) },
                { name: 'Fri', data: data.analysis.week_raw[4].day_raw.slice(open_ix_min, close_ix_max + 1) },
                { name: 'Thu', data: data.analysis.week_raw[3].day_raw.slice(open_ix_min, close_ix_max + 1) },
                { name: 'Wed', data: data.analysis.week_raw[2].day_raw.slice(open_ix_min, close_ix_max + 1) },
                { name: 'Tue', data: data.analysis.week_raw[1].day_raw.slice(open_ix_min, close_ix_max + 1) },
                { name: 'Mon', data: data.analysis.week_raw[0].day_raw.slice(open_ix_min, close_ix_max + 1) }
            ];

            venueHeatmapChart = new ApexCharts(document.querySelector("#venueHeatmap"), chartOptions);
            venueHeatmapChart.render();
        });
    }

    function closeVenueDetails() {
        if (venueDetailsModal) {
            venueDetailsModal.hide();
        }
        if (venueHeatmapChart) {
            venueHeatmapChart.destroy();
            venueHeatmapChart = null;
        }
    }

    // Add modal close event handler
    document.getElementById('venueDetailsModal').addEventListener('hidden.bs.modal', function() {
        if (venueHeatmapChart) {
            venueHeatmapChart.destroy();
            venueHeatmapChart = null;
        }
    });

    $(document).ready(function() {
        const apiKeyInput = $('#api_key_private');
        const apiKeyPublicInput = $('#api_key_public');
        let apiKeyPrivate = localStorage.getItem('besttime_api_key_private');
        let apiKeyPublic = localStorage.getItem('besttime_api_key_public');

        // Initialize map with stored position or default
        const storedLat = localStorage.getItem('map_lat') || 0;
        const storedLng = localStorage.getItem('map_lng') || 0;
        const storedZoom = localStorage.getItem('map_zoom') || 2;

        var map = L.map('map').setView([storedLat, storedLng], storedZoom);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
        }).addTo(map);

        // Save map position on moveend
        map.on('moveend', function() {
            const center = map.getCenter();
            localStorage.setItem('map_lat', reduceCoordinateDecimals(center.lat));
            localStorage.setItem('map_lng', reduceCoordinateDecimals(center.lng));
            localStorage.setItem('map_zoom', map.getZoom());
        });

        // Handle user location
        function handleUserLocation() {
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    const lat = reduceCoordinateDecimals(position.coords.latitude);
                    const lng = reduceCoordinateDecimals(position.coords.longitude);

                    // Save to localStorage
                    localStorage.setItem('user_lat', lat);
                    localStorage.setItem('user_lng', lng);

                    // Move map to user location
                    map.setView([lat, lng], 13);
                }, function(error) {
                    console.error("Error getting location:", error);
                });
            }
        }

        // Check if we have stored user location
        const storedUserLat = localStorage.getItem('user_lat');
        const storedUserLng = localStorage.getItem('user_lng');

        if (!storedUserLat || !storedUserLng) {
            handleUserLocation();
        }

        // Show modal if no API keys are stored
        if (!apiKeyPrivate || !apiKeyPublic) {
            const apiKeyModal = new bootstrap.Modal(document.getElementById('apiKeyModal'));
            apiKeyModal.show();
        } else {
            apiKeyInput.val(apiKeyPrivate);
            apiKeyPublicInput.val(apiKeyPublic);
        }

        // Handle API key save
        $('#saveApiKey').click(function() {
            apiKeyPrivate = apiKeyInput.val().trim();
            apiKeyPublic = apiKeyPublicInput.val().trim();
            if (apiKeyPrivate && apiKeyPublic) {
                localStorage.setItem('besttime_api_key_private', apiKeyPrivate);
                localStorage.setItem('besttime_api_key_public', apiKeyPublic);
                bootstrap.Modal.getInstance(document.getElementById('apiKeyModal')).hide();
                fetchVenues(); // Initial load after API keys are saved
            }
        });

        let venueMarkers = {};
        let currentVenues = [];
        let isInitialLoad = true;
        let isFilterApplied = false;

        function fetchVenues() {
            apiKeyPrivate = apiKeyInput.val();
            if (!apiKeyPrivate) {
                const apiKeyModal = new bootstrap.Modal(document.getElementById('apiKeyModal'));
                apiKeyModal.show();
                return;
            }

            localStorage.setItem('besttime_api_key_private', apiKeyPrivate);
            const bounds = map.getBounds();
            const params = {
                api_key_private: apiKeyPrivate,
                busy_min: $('#busy_min').val() === '' ? undefined : parseInt($('#busy_min').val()),
                busy_max: $('#busy_max').val() === '' ? undefined : parseInt($('#busy_max').val()),
                hour_min: $('#hour_min').val() === '' ? undefined : parseInt($('#hour_min').val()),
                hour_max: $('#hour_max').val() === '' ? undefined : parseInt($('#hour_max').val()),
                day_int: $('#day_int').val() === '' ? undefined : parseInt($('#day_int').val()),
                types: $('#types').val(),
                limit: 20,
                lat_min: bounds.getSouthWest().lat,
                lng_min: bounds.getSouthWest().lng,
                lat_max: bounds.getNorthEast().lat,
                lng_max: bounds.getNorthEast().lng
            };

            $.ajax({
                url: 'https://besttime.app/api/v1/venues/filter',
                method: 'GET',
                data: params,
                success: function(response) {
                    currentVenues = response.venues;
                    displayVenues(response.venues);
                },
                error: function(error) {
                    console.error("Error fetching venues:", error);
                    if (error.status === 401) {
                        // Invalid API key
                        localStorage.removeItem('besttime_api_key_private');
                        const apiKeyModal = new bootstrap.Modal(document.getElementById('apiKeyModal'));
                        apiKeyModal.show();
                    } else if (error.status === 404 && error.responseJSON && error.responseJSON.message) {
                        $('#venueList').html(\`<p class="text-muted p-3">\${error.responseJSON.message}</p>\`);
                    } else {
                        $('#venueList').html("<p class='text-danger p-3'>Error fetching venues. Please check filters and try again.</p>");
                    }
                }
            });
        }

        function getBusyClass(dayRaw) {
            const maxBusy = Math.max(...dayRaw);
            if (maxBusy < 40) return 'busy-low';
            if (maxBusy < 70) return 'busy-medium';
            return 'busy-high';
        }

        function displayVenues(venues) {
            $('#venueList').empty();
            if (!map) return;

            // Clear existing markers
            for (const venueId in venueMarkers) {
                map.removeLayer(venueMarkers[venueId]);
            }
            venueMarkers = {};

            if (venues && venues.length > 0) {
                let listHTML = '';
                let bounds = L.latLngBounds();

                venues.forEach(venue => {
                    listHTML += \`<div class='venue-item p-2 border-bottom' data-venue-id='\${venue.venue_id}'>
                        <strong>\${venue.venue_name}</strong><br>
                        <small class="text-muted">\${venue.venue_address}</small>
                    </div>\`;

                    const markerClass = getBusyClass(venue.day_raw);
                    const marker = L.marker([venue.venue_lat, venue.venue_lng], {
                        icon: L.divIcon({
                            className: \`leaflet-marker-icon \${markerClass}\`,
                            iconSize: [20, 20],
                            iconAnchor: [10, 10],
                            popupAnchor: [0, 0]
                        })
                    }).bindPopup(\`<strong>\${venue.venue_name}</strong><br>\${venue.venue_address}\`);

                    venueMarkers[venue.venue_id] = marker;
                    marker.addTo(map);
                    bounds.extend([venue.venue_lat, venue.venue_lng]);
                });

                $('#venueList').html(listHTML);

                // Only fit bounds on initial load or filter application
                if (isInitialLoad || isFilterApplied) {
                    map.fitBounds(bounds, { padding: [50, 50] });
                    isInitialLoad = false;
                    isFilterApplied = false;
                }

                // Venue list item hover effects
                $('.venue-item').hover(function() {
                    const venueId = $(this).data('venue-id');
                    if (venueMarkers[venueId]) {
                        venueMarkers[venueId].openPopup();
                    }
                }, function() {
                    const venueId = $(this).data('venue-id');
                    if (venueMarkers[venueId]) {
                        venueMarkers[venueId].closePopup();
                    }
                });

                // Add click handler for venue items
                $('.venue-item').click(function() {
                    const venueId = $(this).data('venue-id');
                    const venue = venues.find(v => v.venue_id === venueId);
                    if (venue) {
                        showVenueDetails(venue);
                    }
                });

            } else {
                $('#venueList').html("<p class='text-muted p-3'>No venues found matching your criteria.</p>");
            }
        }

        $('#applyFilters').click(function(e) {
            e.preventDefault();
            isFilterApplied = true;
            fetchVenues();
        });

        // Throttle map movement updates
        let mapMoveTimeout;
        map.on('moveend', function() {
            if (!isInitialLoad && !isFilterApplied) {
                clearTimeout(mapMoveTimeout);
                mapMoveTimeout = setTimeout(fetchVenues, 500);
            }
        });

        // Initial load if API key exists
        if (apiKeyPrivate) {
            fetchVenues();
        }
    });
</script>
</body>
</html>

</HTML example>

<SITEMAP>

# Demo's

## General demo

worldwide demo pages with foot traffic data per city, category (sightseeing, bar, nightclub, restaurants, cafes, shopping,nature), day and time of week.
[General demo](https://besttime.app/app/countries/)

## Venue Search

[Venue Search demo](https://besttime.app/demo/searchvenues)

## Venue Filter (Radar tool)

[Venue Filter demo](https://besttime.app/demo/radar?map_lat=20.80&map_lng=7.22&map_z=2&lat=20.80&lng=7.22&radius=18597969&limit=100)

## Find Foot Traffic Forecast for a Venue based on name and address

[Forecast demo](https://besttime.app/demoforecast)

## Compare dashboard: Compare foot traffic patterns between venues

[Compare demo](https://besttime.app/demo/compare)

# Site tools for signup users

[Start/ overview](https://besttime.app/start)

[Venue foot traffic forecast](https://besttime.app/api/v1/chooseforecast)

[Radar tool/ Venue Filter](https://besttime.app/api/v1/radar/filter)

## Venue collections

[Collections](https://besttime.app/api/v1/collection_list)

## Settings

[Settings](https://besttime.app/settings)

### Settings/ API keys

[API Keys](https://besttime.app/api/v1/api_keys_list)

### Settings/ API Usage

[API Usage](https://besttime.app/api/v1/allusage)

# Upgrade subscription

[Upgrade](https://besttime.app/subscription/pricing)
</SITEMAP>

<SUPPORTED COUNTRIES WITH FOOT TRAFFIC FORECASTS>
# Supported countries on BestTime.app with foot traffic forecasts and live data
Albania
Algeria
Andorra
Angola
Argentina
Aruba
Australia
Austria
Azerbaijan
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Botswana
Brazil
British Virgin Islands
Brunei
Bulgaria
Burkina Faso
Cambodia
Cameroon
Canada
Cayman Islands
Chile
Colombia
Costa Rica
Croatia
Cyprus
Czechia
Denmark
Dominican Republic
Ecuador
Egypt
El Salvador
Estonia
Ethiopia
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
Gabon
Georgia
Germany
Ghana
Gibraltar
Greece
Grenada
Guadeloupe
Guam
Guatemala
Guinea
Guyana
Haiti
Honduras
Hong Kong
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Isle Of Man
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Malawi
Malaysia
Mali
Malta
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Namibia
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Northern Mariana Islands
Norway
Oman
Pakistan
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Puerto Rico
Qatar
Romania
Russia
Rwanda
San Marino
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
South Africa
Spain
Sri Lanka
Suriname
Sweden
Switzerland
Taiwan
Tanzania
Thailand
Timor-Leste
Togo
Tunisia
Turkey
Uganda
United Arab Emirates
United Kingdom
United States
Uruguay
U.S. Virgin Islands
Uzbekistan
Vatican City
Venezuela
Vietnam
Zambia
Zimbabwe
</SUPPORTED COUNTRIES WITH FOOT TRAFFIC FORECASTS>

<DEBUG Errors>
Sometimes users talk about errors they get. Some errors are normal (e.g. no foot traffic forecast or live data available), but there could be bugs in the users code, or in rare cases in the BestTime API.

If the user uses Javascript and experiences errors, ask them to provide the Javascript code and the console errors. e.g. `[object Object]" error` console error is not informative enough so the actual JS code is needed to help fix the issue.

CORS:
CORS issues are usually not because of BestTime, but of the users code or browser settings. Explain them how they can fix it.
<DEBUG Errors>

<CUSTOMER SUPPORT EMAIL EXAMPLES>

<EXAMPLE 1>

### User email:
Good day,

Based on our understanding, it seems the Pro metered plan would be the most cost-effective solution for our needs. We estimate around 1,000 venues in our area that fit our criteria. We anticipate running the venue filter API once a month to identify any new venues. Following that, we would use the foot traffic by ID to get the forecast data approximately every two weeks.

We believe this approach will be the most efficient in terms of cost. Please let me know if you have any thoughts on this.

### Response from BestTime Support:

Thanks for reaching out and outlining your plan. It's helpful to understand your intended usage.

I agree with you that the Pro - Metered plan seems to be the most cost efficient with your described usage.

Let's break down the estimated costs based on your strategy using the Pro Metered plan.

**Your Estimated Usage:**

1. **Venue Filter API:** 1 call per month. Assuming this returns ~1,000 venues.
    - Credits: 1,000 venues * 0.1 credits/venue = 100 credits.
2. **Venue Foot Traffic by ID (Query):** Querying 1,000 venues twice a month (every two weeks). Querying an existing forecast costs 1 credit per venue.
    - Credits: 1,000 venues *1 credit/venue* 2 times/month = 2,000 credits.
3. **Total Estimated Monthly Credits:** 100 + 2,000 = 2,100 credits.

**Pro Metered Plan Cost:**

- Platform Fee: $99 per month.
- Credit Cost: 2,100 credits * $0.009/credit = $18.90.
- **Total Estimated Cost:** $99 + $18.90 = **$117.90 USD per month**.

**Comparison with Basic Metered Plan:**

- Credit Cost: 2,100 credits * $0.04/credit = $84 USD per month.
- The Basic Metered plan would be cheaper (**$84/month**) for this specific usage pattern *if* you only need to query existing forecasts and do not require live data access.

**Important Consideration: Querying vs. Refreshing Forecasts**

You mentioned using "foot traffic by ID to get the forecast data". It's important to distinguish between:

- **Querying (Query venue, GET request):** Retrieves the *last generated* forecast for a venue (1 credit/venue) from BestTime. Forecasts don't update automatically. BestTime aims to update all world wide venues roughly once a month. If you want to get the latest forecast data, you can use the POST request to refresh the forecast.
- **Refreshing (New foot-traffic forecast, POST request):** Generates a *new, updated* forecast based on the latest patterns (2 credits/venue).

If your plan is to get *updated* forecast data every two weeks, you would need to use the POST request to refresh the forecast. Let's recalculate based on refreshing:

1. **Venue Filter API:** 100 credits (as before).
2. **Venue Foot Traffic by ID (Refresh):** Refreshing 1,000 venues twice a month.
    - Credits: 1,000 venues *2 credits/venue* 2 times/month = 4,000 credits.
3. **Total Estimated Monthly Credits (Refreshing):** 100 + 4,000 = 4,100 credits.

**Costs if Refreshing Bi-Weekly:**

- **Pro Metered:** (4,100 credits * $0.009/credit) + $99 = $36.90 + $99 = **$135.90 USD per month**.
- **Basic Metered:** 4,100 credits * $0.04/credit = **$164 USD per month**.

In this scenario (refreshing bi-weekly), the Pro Metered plan becomes more cost-effective than the Basic Metered plan.

**Thoughts on Your Strategy:**

- Using the Venue Filter API monthly to identify new venues is in generally more efficient than Venue Search for broad area checks.
- While the Venue Filter is more efficient, it only returns venues that are already available on the BestTime platform. If venues are missing, you can either add them yourself using the New Venue Foot Traffic Forecast API, or use the Venue Search API to add multiple venues based on a query (e.g., “grocery stores in city X” or “Italian restaurants in city X, country Y”). The Venue Search API can add venues not previously seen on BestTime (e.g., new venues). However, this method is significantly slower and consumes more credits.
- We are working to improve BestTime to automatically add new venues to the platform. However, at the moment, we still partially rely on our users to help accomplish this.
- You can configure the Venue Filter to limit the amount of venues returned. When you combine this with location coordinates, venue types, etc you can reduce the amount of venues returned to a minimum to control costs.

**Conclusion:**

- If you only need to **query** stored forecasts bi-weekly (or refresh monthly) and **don't need live data**, the **Basic Metered plan** seems most cost-effective ($84/month).
- If you plan to **refresh** forecasts bi-weekly using the POST method, the **Pro Metered plan** is more cost-effective ($135.90/month vs $164/month) and also includes live data access.
- Package plans (like Pro Package 1K at $249/month or Basic Package 10K at $299/month) would be more expensive for your described usage.

I hope this helps!

Best regards,

</EXAMPLE 1>

</CUSTOMER SUPPORT EMAIL EXAMPLES>



</CONTEXT>
