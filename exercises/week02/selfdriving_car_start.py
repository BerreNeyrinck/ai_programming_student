"""
Oefening 1: Self-Driving Car (Model-based Reflex Agent)
========================================================
Implementeer een agent die zijn voorligger volgt op 10m.
"""


class LidarSensorInput:
    def __init__(self, distance=0.0,):
        self.DistanceTo = distance


class Brake:
    def __str__(self):
        return "BRAKE"


class Nothing:
    def __str__(self):
        return "NOTHING"


class SelfDrivingCar:
    def __init__(self):
        # TODO: interne state — welke variabele heb je nodig?
        self.Delta_Distance = 0
        self.lastDistance = 0
        self.Delta_Time = 0
        self.snelheid = 0
        pass

    def process(self, sensor_input):
        # TODO: bereken relatieve snelheid en tijd tot botsing
        #       rem als tijd < 5 seconden
        # print(f"distance To target: {sensor_input.DistanceTo}")
        self.snelheid = self.lastDistance - sensor_input.DistanceTo
        # print(f"snelheid: {self.snelheid}")
        if(self.snelheid > 0):
            self.Delta_Time = self.lastDistance / self.snelheid
            print(f"tijd tot botsing: {round(self.Delta_Time,2)}")

            if(self.Delta_Time < 5):
                return Brake()
            else:
                return Nothing()

        self.lastDistance = sensor_input.DistanceTo
        action = Nothing()
        return action


if __name__ == "__main__":
    sensor = LidarSensorInput(10)
    agent = SelfDrivingCar()

    for afstand in [10, 15, 13, 10, 8, 6, 4, 3]:
        sensor.DistanceTo = afstand
        action = agent.process(sensor)
        print(f"Afstand: {afstand}m -> {action}")