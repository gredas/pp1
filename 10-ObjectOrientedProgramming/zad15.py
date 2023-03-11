import random
class thermometer():
    def use(self):
        self.temperature = round(random.uniform(34.0,42.0),1)
    def result(self):
        if self.temperature>=37:
            print(f'Temperature : {self.temperature}C (fever)')
        else:
            print(f'Temperature : {self.temperature}C (normal)')
thermometer1 = thermometer()
thermometer1.use()
thermometer1.result()

