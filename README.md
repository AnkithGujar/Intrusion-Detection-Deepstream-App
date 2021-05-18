# Intrusion Detection using Deepstream 5.1 #

## Description ##

The main focus of our project was to achieve two aspects of self-driving cars, Steering control and Obstacle avoidance. We trained our Convolutional Neural Network (CNN) with images taken from a camera mounted on the vehicle to achieve accurate steering control and we used a pre-trained network on the Common Objects in Context (COCO) dataset for Object Detection. The code in this repository focuses on testing our model in the game GTA V. We picked GTA V for its real-world simulation with traffic, pedestrians, traffic lights, and buildings.

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