from random import randint

from ..sensor import Sensor


class VoltageSensor(Sensor):
    def __init__(self, name: str) -> None:
        super().__init__(name, "voltage", "volt")

    def read(self) -> float:
        return randint(0, 1000)
