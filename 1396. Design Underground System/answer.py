class UndergroundSystem:

    def __init__(self):
        self.route = {}
        self.cus = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cus[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cus_checkin = self.cus.get(id)
        startStation, start_t = cus_checkin[0], cus_checkin[1]
        endStation = stationName
        end_t = t
        time_diff = end_t - start_t

        if self.route.get((startStation, endStation)):
            c_route = self.route.get((startStation, endStation))
            total_count, total_time = c_route[0], c_route[1]
            self.route[(startStation, endStation)] = (1 + total_count, total_time + time_diff)
        else:
            self.route[(startStation, endStation)] = (1, time_diff)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        c_route = self.route.get((startStation, endStation))

        total_count, total_time = c_route[0], c_route[1]
        return total_time / total_count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)