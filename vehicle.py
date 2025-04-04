import csv
class Vehicle:
    tax=0.16
    all=[]
    def __init__(self,type:str,company:str,color:str,price:int):
        self.type=type
        self.company=company
        self.color=color
        self.price=price
        Vehicle.all.append(self)
    
    def final_price(self):
        return self.price-(self.price*self.tax)

    @classmethod
    def from_csv(cls):
        with open("vehicle.csv","r") as f:
            read=csv.DictReader(f)
            vehicles=list(read)
        for vehicle in vehicles:
            Vehicle(
                type=vehicle.get('type'),
                company=vehicle.get('company'),
                color=vehicle.get('color'),
                price=vehicle.get('price')
            )
    @staticmethod
    def isinteger():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''
    @staticmethod
    def is_expensive():
        if Vehicle.price>=20000:
            return f"{Vehicle.type} is expensive as fuck!!"
        else:
            return "not bad!!"

    def __repr__(self):
        return f"Type: {self.type}\nCompany: {self.company}\nColor: {self.color}\nPrice: {self.price}\n"

Vehicle.from_csv()

        

        
    