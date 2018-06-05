# A python web app template - Flask + MongoDB
This is a highly configurable python web application boilerplate.<br>
It uses Flask, MongoDB, custom logging and environmental configurations for easy, robust development.<br>


### Steps:
1. Search for 'TODO' in the project to fill the configuration.<br>
2. python ui/server.py

### Architecture:
```bash
python-boilerplate/ # root directory
    core/ # configurations, models and abstractions.
    data/ # MongoDB access layer and a factory
    ui/ # Contains a Flask application that uses the db
    tests/ # Any tests you want to implement
    bll/ # Any custom logic you want to use between the UI and the DATA layers.
```

### Configurations
The directory core/configurations contains a lot of configurations.<br>
The most important one is env.py,<br>
DEVELOP_MODE will control the selected db and the logging levels.