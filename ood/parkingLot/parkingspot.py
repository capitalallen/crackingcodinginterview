class ParkingSpot:
    """
    variable    type
    vehicle     Vehicle
    spotSize    VehicleSize
    row         int
    spotNumber  int
    level       Leve
    """
    def __init__(self,spotSize,row,spotNumber,level):
        self.vehicle = None
        self.spotSize = spotSize
        self.row = row
        self.spotNumber = spotNumber
        self.level = level
    """
    isAvalable: return vehicle
    """
    def isAvalable(self):
        return self.vehicle
    """
    check if the spot is  big enough for the vehicle
    """
    def canFitVehicle(self,v):
        # canFitInspot
        return self.isAvalable()
    """
    park vehicle in this spot
    """
    def park(self,v):
        if not self.canFitVehicle(v):
            return False
        self.vehicle = v
        #self.vehicle.parkinSpot(this)
        return True
    """
    getRow()
    """
    def getRow(self):
        return self.row
    """
    getSpotNumber
    """
    def getSpotNumber(self):
        return self.spotNumber
    """
    getsize
    """
    def getSize(self):
        return self.spotSize
    """
    removevehicle: remove vehicle and notify leve
    """
    def removevehicle(self):
        #self.leve.spotFreed()
        self.vehicle = None
    def __str__(self):
        print(self.vehicle)