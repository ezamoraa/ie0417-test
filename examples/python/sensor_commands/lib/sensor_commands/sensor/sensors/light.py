from random import randint

from ..sensor import Sensor


class LightSensor(Sensor):
    def __init__(self, name: str) -> None:
        super().__init__(name, "light", "lumen")

    def read(self) -> float:
        low = 200
        high = 1000
        return randint(low, high)
