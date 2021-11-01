class Car():#parent class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
            
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
        
    def read_odometer(self):
         print('This car has '+str(self.odometer_reading)+' miles on it.')
    
    def update_odometer(self,milage):#new method\n,
            #Set the odometer reading to the given value.
             #Reject the change if it attempts to roll the odometer back.
            
        if milage>=self.odometer_reading:
            self.odometer_reading=milage
        else:
            print('You cannot roll back an odometer!!')
                
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self,battery_size=70):
        """Initialize the battery's attribite"""
        self.battery_size=battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print('This car has a '+str(self.battery_size)+'-kWh battery')
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range=240
        elif self.battery_size == 85:
            range=270
            
        message="This car can go approximately "+str(range)
        message+=" miles on full charge!"
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85
    
class ElectricCar(Car):#child class
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery=Battery()

