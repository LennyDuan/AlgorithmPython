class ParkingSystem:
    slot = {
        1: None,
        2: None,
        3: None,
    }

    def __init__(self, big: int, medium: int, small: int):
        self.slot[1] = [0] * big
        self.slot[2] = [0] * medium
        self.slot[3] = [0] * small

    def addCar(self, carType: int) -> bool:
        try:
            free = self.slot[carType].index(0)
            self.slot[carType][free] = carType
            return True
        except Exception:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)