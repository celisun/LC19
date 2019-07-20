# clarify
# what types of cars? motorcycle, car, bus
# how much space to take?
#   motor spot: motor
#   compact spot: motor, car
#   large spot: motor, car
#   bus can park if we have 5 consecutive large spots

# does parking lot have multiple levels? y


from abc import ABCMeta, abstractmethod
from enum import Enum

class VehicleSize(Enum):
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2

class Vehicle(metaclass=ABCMeta):
    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []

    def clear_spots(self):
        for spot in self.spots_taken:
            spot.remove_vehicle(self)
        self.spots_taken = []

    def take_spot(self, spot):

    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass


class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super(Motorcycle, self).__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True

class Car(Vehicle):
    def __init__(self, license_plate):
        super(Car, self).__init__(VehicleSize.COMPACT, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return spot.size in (VehicleSize.LARGE, VehicleSize.COMPACT)


class Bus(Vehicle):
    def __init__(self, license_plate):
        super(Bus, self).__init__(VehicleSize.LARGE, license_plate, spot_size=5)

    def can_fit_in_spot(self, spot):
        return spot.size == VehicleSize.LARGE


# ----------------------------

class ParkingLot:
    def __init__(self, num_levels=3):
        self.num_levels = num_levels
        self.levels = [Level()] * num_levels

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False


class Level:
    SPOTS_PER_ROW = 10
    def __init__(self, floor, total_spots):
        self.floor = floor
        self.num_spots = total_spots
        self.available_spots = total_spots
        self.parking_spots = []

    def park_vehicle(self, vehicle):
        """succeed, return True otherwise false"""
        spot = self._find_available_spot(vehicle)
        if spot is None:
            return None
        else:
            self._park_starting_at_spot(spot, vehicle)
            return spot

    def _find_available_spot(self, vehicle):
        """find avaiable to park, return spot, otherwise None"""
        if self.available_spots == 0: return None
        if vehicle.vehicle_size == VehicleSize.LARGE:
            i = j = 0
            while j < len(self.parking_spots):
                if not self.parking_spots[j].is_available() or vehicle.can_fit_in_spot(self.parking_spots[j]):
                    j += 1
                    i = j
                else:
                    j += 1
                    if j - i == 5:
                        return self.parking_spots[i]
        else:
            for spot in self.parking_spots:
                if spot.is_available() and vehicle.can_fit_in_spot(spot):
                    return spot
        return None

    def _park_starting_at_spot(self, spot, vehicle):
        """make parking from spot to spot + vehicle.size"""


class ParkingSpot:
    def __init__(self, level, row, spot_number, spot_size, vehicle_size):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle_size = vehicle_size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle):
        if self.vehicle is not None:
            return False
        return vehicle.can_fit_in_spot(self) # we let vehicle decide

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None


