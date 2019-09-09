class Vehicle:
    def __init__(self):
        # add parkingspot
        self.parkingSpots = []
        self.licensePlate = None
        self.spotsNeeded = None
        self.size = None
    def getSpotsNeeded(self):
        return self.spotsNeeded

    def getSize(self):
        return self.size
    def parkInSpot(self,spot):
        #self.parkingSpot.append(spot)
        pass
    def clearSpot(self):
        for i in range(len(self.parkingSpots)):
            tmp = self.parkingSpots[i]
            self.parkingSpots.remove(tmp)
    #canFitInSpot
    #print()
