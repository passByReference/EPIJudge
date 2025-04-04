class VehicleSize(object):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3

class Vehicle(object):
    def __init__(self, license_plate: str, vehicle_size: VehicleSize):
        self.license_plate = license_plate
        self.vehicle_size = vehicle_size

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.MOTORCYCLE)


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.COMPACT)

class Bus(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.LARGE)



class ParkingSpot(object):
    def __init__(self, level_number: int, spot_number:int, size: int):
        self.spot_number = spot_number
        self.level_number = level_number
        self.vehicle = None
        self.size = size

    def park_vehicle(self, vehicle: Vehicle):
        if self.vehicle is not None:
            raise Exception("Spot already occupied")
        if self.size < vehicle.vehicle_size:
            raise Exception("Vehicle too large for spot")
        self.vehicle = vehicle
    
    def is_available(self):
        return self.vehicle is None

    def remove_vehicle(self):
        if self.vehicle is None:
            raise Exception("Spot already empty")
        self.vehicle = None
    
    def __repr__(self):
        return f"ParkingSpot(level={self.level_number}, spot={self.spot_number}, size={self.size}, vehicle={self.vehicle.license_plate if self.vehicle else 'empty'})"

class ParkingLevel(object):
    SPOTS_PER_LEVEL = 10
    def __init__(self, level_number:int):
        self.level_number = level_number
        self.spots = [ParkingSpot(level_number, i, VehicleSize.LARGE) for i in range(self.SPOTS_PER_LEVEL)]

    
       
class ParkingLot(object):
    def __init__(self, num_levels:int):
        self.levels = [ParkingLevel(i) for i in range(num_levels)]
        self.num_levels = num_levels

    def get_number_of_available_spots(self) -> int:
        return sum(spot.is_available() for level in self.levels for spot in level.spots)
    
    def find_available_spot(self, vehicle: Vehicle) -> list[ParkingSpot]:
        if not isinstance(vehicle, Bus):
            for level in self.levels:
                for spot in level.spots:
                    if spot.is_available() and spot.size >= vehicle.vehicle_size:
                        return [spot]
        else:
            print("Finding spot for bus")
            for level in self.levels:
                for i, spot in enumerate(level.spots):
                    if spot.is_available() and spot.size == VehicleSize.LARGE:
                        end = i + 5
                        if end <= len(level.spots) and all(level.spots[j].is_available() and level.spots[j].size == VehicleSize.LARGE for j in range(i, end)):
                            return level.spots[i:end]
        raise Exception("No available spot found")

    def park_vehicle(self, vehicle: Vehicle) -> list[ParkingSpot]:
        spots = self.find_available_spot(vehicle)
        for spot in spots:
            spot.park_vehicle(vehicle)
        return spots
    
def main():
    parking_lot = ParkingLot(3)
    motorcycle = Motorcycle("1234")
    car = Car("5678")
    bus = Bus("91011")

    print(f"Available spots: {parking_lot.get_number_of_available_spots()}")

    motorcycle_spots = parking_lot.park_vehicle(motorcycle)
    print(f"Motorcycle parked in spots: {[spot for spot in motorcycle_spots]}")

    car_spots = parking_lot.park_vehicle(car)
    print(f"Car parked in spots: {[spot for spot in car_spots]}")

    bus_spots = parking_lot.park_vehicle(bus)
    print(f"Bus parked in spots: {[spot for spot in bus_spots]}")

    print(f"Available spots: {parking_lot.get_number_of_available_spots()}")


if __name__ == "__main__":
    main()
    

