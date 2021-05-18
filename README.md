# Intrusion Detection using Deepstream 5.1 #

## Folder Structure ##

```bash
├── deepstream_app
│   ├── common
│   │   ├── __pycache__
│   │   │   ├── FPS.cpython-36.pyc
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── bus_call.cpython-36.pyc
│   │   │   ├── is_aarch_64.cpython-36.pyc
│   │   ├── FPS.py
│   │   ├── __init__.py
│   │   ├── bus_call.py
│   │   ├── is_aarch_64.py
│   │   ├── utils.py
│   ├── deepstream-intrusion-detection-analytics
│   │   ├── config_nvdsanalytics.txt
│   │   ├── deepstream_intrusion_analytics.py
│   │   ├── dsnvanalytics_pgie_config.txt
│   │   ├── dsnvanalytics_tracker_config.txt
├── flask_app
│   ├── static
│   │   ├── cover.css
│   │   ├── dashboard.css
│   │   ├── styles.css
│   ├── templates
│   │   ├── both.html
│   │   ├── home.html
│   │   ├── live_chart.html
│   │   ├── live_streaming.html
│   ├── database.csv
│   ├── flask_app.py
│   ├── nginx.conf
│   ├── uwsgi.ini
├── README.md
```

## Prerequisites ##

- DeepStreamSDK 5.1
- Python 3.6
- Gst-python
- flask_socketio
- flask
- pandas
- OpenCV
- redis

## How To Use ##

* Run the flask_app.py file with 
```bash 
python3 flask_app.py
```
* Run the deepstream_intrusion_analytics.py file with
```bash 
python3 deepstream_intrusion_analytics.py <uri1> [uri2] ... [uriN]

Eg:	python3 deepstream_intrusion_analytics.py file:///home/ubuntu/video1.mp4
	python3 deepstream_intrusion_analytics.py rtsp://127.0.0.1/video1
```