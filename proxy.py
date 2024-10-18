class proxy:

    def __init__(self, id, name, online, battery_level):
        self.id = id
        self.online = online
        self.btr = battery_level
        self.region, self.name = self.getRegionName(name)

    def getRegionName(self, name):
        lst = name.split(" ")
        return lst[0], lst[1]
    
    def printInfos(self):
        print(f'Device ID: {self.id}')
        print(f'Device: {self.region} {self.name}')
        print(f'Online: {self.online}')
        print(f'battery: {self.btr}%')
