# weatherxm-api-demos
Short demos of the WeatherXM API (https://api.weatherxm.com/api/v1/docs/)

# Installation

```bash
$ git clone https://github.com/vrypan/weatherxm-api-demos.git

$ cd weatherxm-api-demos

$ python3 -m venv venv

$ . ./venv/bin/activate

$ pip install -r requirements.txt

```

# Usage 

Next, copy `.env.sample` to `.env` and edit it with your username and password.

Run `my_stations.py`

```bash
$ python ./my_stations.py
```

This will show all your stations and the current weather conditions for each one.

For example:

```
python ./my_stations.py
========================================
Station ID: e2816f10-a9de-11ec-900c-abdec1c57354
Station Name: Macho Mango Altocumulus
Current Weather:
	timestamp	2024-06-04T17:55:22+03:00
	temperature	36.8
	humidity	19
	wind_speed	0.58
	wind_gust	1.02
	wind_direction	148
	solar_irradiance	221.80327868852459
	uv_index	2
	precipitation	0
	pressure	979.43
	dew_point	9.41081931510785
	precipitation_accumulated	0
	feels_like	35.062236267520014
	icon	partly-cloudy-day
```

`one_day_temp_hist.py` is an example on how to retrieve historic data.

Get your Station ID from the previous command and run `python ./one_day_temp_hist.py <STATION_ID>`

```
python ./one_day_temp_hist.py e2816f10-a9de-11ec-900c-abdec1c57354
# Station =  e2816f10-a9de-11ec-900c-abdec1c57354
2024-05-28T00:00:00+03:00 16.12
2024-05-28T01:00:00+03:00 15.17
2024-05-28T02:00:00+03:00 14.75
2024-05-28T03:00:00+03:00 14.23
2024-05-28T04:00:00+03:00 13.97
2024-05-28T05:00:00+03:00 13.78
...
```

If you want a nice chart, you can use a library/program like [gnuplot](http://www.gnuplot.info) or (much more limited but very easy) [termgraph](https://github.com/mkaz/termgraph)

```
pip install termgraph

python ./one_day_temp_hist.py e2816f10-a9de-11ec-900c-abdec1c57354 | termgraph


2024-06-03T00:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 21.01
2024-06-03T01:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 20.33
2024-06-03T02:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.96
2024-06-03T03:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.53
2024-06-03T04:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.30
2024-06-03T05:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.12
2024-06-03T06:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.58
2024-06-03T07:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 21.60
2024-06-03T08:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 27.66
2024-06-03T09:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 30.99
2024-06-03T10:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.56
2024-06-03T11:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.09
2024-06-03T12:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.52
2024-06-03T13:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.17
2024-06-03T14:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 31.59
2024-06-03T15:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.79
2024-06-03T16:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.59
2024-06-03T17:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.90
2024-06-03T18:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 33.21
2024-06-03T19:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 30.04
2024-06-03T20:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 27.35
2024-06-03T21:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 24.55
2024-06-03T22:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 23.19
2024-06-03T23:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 22.37
2024-06-04T00:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 21.60
2024-06-04T01:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 21.33
2024-06-04T02:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 21.21
2024-06-04T03:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 20.61
2024-06-04T04:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.94
2024-06-04T05:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.32
2024-06-04T06:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.39
2024-06-04T07:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 21.55
2024-06-04T08:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 27.45
2024-06-04T09:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 30.72
2024-06-04T10:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.83
2024-06-04T11:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 34.60
2024-06-04T12:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 35.70
2024-06-04T13:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 35.49
2024-06-04T14:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 36.61
2024-06-04T15:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 38.06
2024-06-04T16:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 37.84
2024-06-04T17:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 36.98
2024-06-04T18:00:00+03:00: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 36.60
```

# API documentation

You can find the full API documantation at https://api.weatherxm.com/api/v1/docs/

# Limitations

The API will only allow you to get historic data for your own stations or the stations you follow (you can follow up to 10 more stations).

You can use the [search endpoint](https://api.weatherxm.com/api/v1/docs/#/network/search) to find stations to follow (or do it through the mobile app).

If you are interested in using the API to get data for many stations, [WeatherXM Pro](https://weatherxm.com/weatherxm-pro/) is under development.
