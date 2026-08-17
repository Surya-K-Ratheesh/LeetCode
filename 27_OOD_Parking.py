from enum import Enum
import time

def main():
    class SpotSize(Enum):
        motorcycle = 0
        compact = 1
        large = 2

    class vehicle:
        def __init__(self, plate, spot_size):
            self.plate = plate
            self.spot_size = spot_size

    class motorcycle(vehicle):
        def __init__(self, plate):
            super().__init__(plate, SpotSize.motorcycle)

    class car(vehicle):
        def __init__(self, plate):
            super().__init__(plate, SpotSize.compact)

    class truck(vehicle):
        def __init__(self, plate):
            super().__init__(plate, SpotSize.large)


    class ParkingSpot:
        def __init__(self, spot_id, size):
            self.id = spot_id
            self.size = size
            self.vehicle = None
            self.entry_time = None

        def is_free(self):
            return self.vehicle is None


    class level:
        def __init__(self, name, spots):
            self.name = name
            self.spots = spots

    class ParkingLot:
        hourly_rate = 5.0

        def __init__(self):
            self.levels = []

        def add_level(self, level):
            self.levels.append(level)

        def find_spot(self, vehicle):
            for level in self.levels:
                for spot in self.spots:
                    if spot.is_free() and spot.size.value >= vehicle.spot_size.value:
                        return spot

            return None

        def park(self, vehicle):
            spot = self.find_spot(vehicle)

            if spot is None:
                return None

            spot.vehicle = vehicle
            spot.entry_time = time.time()

            return spot

        def leave(self, vehicle):
            for level in self.levels:
                for spot in self.spots:
                    if spot.vehicle is vehicle:
                        hours = (time.time() - spot.entry_time) / 3600
                        bill = round(hours * self.hourly_rate, 2)
                        spot.vehicle = None
                        spot.entry_time = None
                        return bill

            return None

if __name__ == '__main__':
    main()