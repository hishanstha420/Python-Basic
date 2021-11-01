class Car():#parent class\n,
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


