from nicegui import Client, ui
from . import counter

def startup() -> None:
    counter.create()