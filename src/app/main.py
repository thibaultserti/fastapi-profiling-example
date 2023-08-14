import os
import pyroscope
from fastapi import FastAPI
from bike.bike import order_bike
from car.car import order_car
from scooter.scooter import order_scooter

import constants

pyroscope.configure(
	application_name = constants.APP_NAME,
	server_address   = constants.PYROSCOPE_ENDPOINT,
	tags             = {
        "region":   f'{os.getenv("REGION")}',
	}
)


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bike")
def bike():
    order_bike(0.2)
    return "<p>Bike ordered</p>"


@app.get("/scooter")
def scooter():
    order_scooter(0.3)
    return "<p>Scooter ordered</p>"


@app.get("/car")
def car():
    order_car(0.4)
    return "<p>Car ordered</p>"


@app.get("/")
def environment():
    result = "<h1>environment vars:</h1>"
    for key, value in os.environ.items():
        result +=f"<p>{key}={value}</p>"
    return result