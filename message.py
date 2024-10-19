class Message:
    def __init__(self, proxy, battery=False):
        self.name = proxy.name
        self.region = proxy.region

        if battery:
            self.text = f'O proxy {self.region} {self.name} está com pouca bateria, cerca de {proxy.btr}%'        
        else:
            self.text = f'O proxy {self.region} {self.name} está offline!'

    def __str__(self):
        return self.text