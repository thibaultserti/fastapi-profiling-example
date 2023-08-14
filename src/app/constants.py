import os

APP_NAME = os.environ.get("APP_NAME", "fastapi-profiling-example")
PYROSCOPE_ENDPOINT = os.environ.get("PYROSCOPE_ENDPOINT", "http://pyroscope.ayanides.cloud")