class CellPhone:
  def __init__(self, brand, model, color):
    self.brand = brand
    self.model = model
    self.color = color
    self.power_on = False
    self.ringing = False

  def __str__(self):
    return "Brand: {}\nModel: {}\nColor: {}".format(self.brand, self.model, self.color)

  def turn_on(self):
    self.power_on = True
    print("Phone is turning on...")

  def turn_off(self):
    self.power_on = False
    print("Phone is turning off...")

  def start_ringing(self):
    self.ringing = True
    print("Ringing...")

  def stop_ringing(self):
    self.ringing = False
    print("Stopped ringing.")

# Example usage:
phone1 = CellPhone("Apple", "iPhone 12", "black")
phone2 = CellPhone("Samsung", "Galaxy S20", "gray")

print(phone1)
print(phone2)

phone1.turn_on()
phone1.start_ringing()
phone1.stop_ringing()
phone1.turn_off()

phone2.turn_on()
phone2.start_ringing()
phone2.stop_ringing()
phone2.turn_off()
