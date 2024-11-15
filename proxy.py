class Proxy:

    def __init__(self, line):
        self.id = line['id']
        self.online = line['online']
        self.btr = line['deviceMetrics']['batteryLevel']
        self.isCharging = line['deviceMetrics']['isCharging']
        self.region, self.name = self.getRegionName(line['name'])

    def getRegionName(self, name):
        lst = name.split(" ")
        if lst[-1].endswith(']'):
            lst = lst[:-1]
        return " ".join(lst[:-1]), lst[-1]
    
    def printInfos(self):
        print(f'Device ID: {self.id}')
        print(f'Device: {self.region} {self.name}')
        print(f'Online: {self.online}')
        print(f'battery: {self.btr}%')
