class Person:
    def __init__(self, name, ssn):
        self.__name = name
        self.__ssn = ssn
    
    def setName(self, new_name):
        self.__name = new_name
    def setSsn(self, new_ssn):
        self.__ssn = new_ssn

    def getName(self):
        return self.__name
    def getSsn(self):
        return self.__ssn

    def __repr__(self):
        return "Person({},  {})".format(self.getName(), self.getSsn())
    def __str__(self):
        return "Name:   {}\nSSN:    {}".format(self.getName(), self.getSsn())


class Employee(Person):
    def __init__(self, name, ssn, _id, password):
        Person.__init__(self, name, ssn)
        self.__id = _id
        self.__password = password
    
    def setId(self, new_id):
        self.__id = new_id
    def setPassword(self, password):
        self.__password = password
    
    def getId(self):
        return self.__id
    def getPassword(self):
        return self.__password

    def login(self, name, password):
        if(name == self.getName() and password == self.getPassword()):
            return True
        else:
            return False

    def __repr__(self):
        return "Employee({},    {}, {}, {})".format(
            self.getName(), self.getSsn(), self.getId(), self.getPassword()
        )
    def __str__(self):
        return "Name:   {}\nSSD:    {}\nID: {}\nPassword:   {}".format(
            self.getName(), self.getSsn(), self.getId(), self.getPassword())


class Customer(Person):
    def __init__(self, name, ssn, home_address, phone_number, country, user_history):
        Person.__init__(self, name, ssn)
        self.__home_address = home_address
        self.__phone_number = phone_number
        self.__country = country
        self.__user_history = user_history

    def setHomeAddress(self, new_home_address):
        self.__home_address = new_home_address
    def setPhone(self, new_phone_number):
        self.__phone_number = new_phone_number
    def setCountry(self, new_country):
        self.__country = new_country
    def setHistoryUser(self, new_user_history):
        self.__user_history = new_user_history

    def getHomeAddress(self):
        return self.__home_address
    def getPhone(self):
        return self.__phone_number
    def getCountry(self):
        return self.__country
    def getHistoryUser(self):
        return self.__user_history
    
    def __repr__(self):
        return "Customers({},   {}, {}, {}, {}, {})".format(
            self.getName(), self.getSsn(), self.getHomeAddress(), self.getPhone(),
            self.getCountry(), self.getHistoryUser()
        )

    def __str__(self):
        return "Name:           {}\nSSN:            {}\nHome Address:   {}\nPhone:          {}\nCountry:        {}\nUser History:   {}".format(
            self.getName(), self.getSsn(), self.getHomeAddress(), self.getPhone(),
            self.getCountry(), self.getHistoryUser()
        )

class Car:
    def __init__(self, plate_number, status, car_type, seats, fuel_type, model, price_range, manufacturer, color, car_history):
        self.__plate_number = plate_number 
        self.__status = status
        self.__car_type = car_type
        self.__seats = seats
        self.__fuel_type = fuel_type
        self.__model = model
        self.__price_range = price_range 
        self.__manufacturer = manufacturer
        self.__color = color
        self.__car_history = car_history

    def setPlateNumber(self, new_plate_number):
        self.__plate_number = new_plate_number
    def setStatus(self, new_status):
        self.__status = new_status
    def setCarType(self, new_car_type):
        self.__car_type = new_car_type
    def setSeats(self, new_seats):
        self.__seats = new_seats
    def setFuelType(self, new_fuel_type):
        self.__fuel_type = new_fuel_type
    def setModel(self, new_model):
        self.__model = new_model
    def setPriceRange(self, new_price_range):
        self.__price_range = new_price_range
    def setManufacturer(self, new_manufacturer):
        self.__manufacturer = new_manufacturer
    def setColor(self, new_color):
        self.__color = new_color
    def setCarHistory(self, new_car_history):
        self.__car_history = new_car_history

    def getPlateNumber(self):
        return self.__plate_number
    def getStatus(self):
        return self.__status
    def getCarType(self):
        return self.__car_type
    def getSeats(self):
        return self.__seats
    def getFuelType(self):
        return self.__fuel_type
    def getModel(self):
        return self.__model
    def getPriceRange(self):
        return self.__price_range
    def getManufacturer(self):
        return self.__manufacturer
    def getColor(self):
        return self.__color
    def getCarHistory(self):
        return self.__car_history
    
    def __repr__(self):
        return "Car({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(
            self.getPlateNumber(), self.getStatus(), self.getCarType(), self.getSeats(),
            self.getFuelType(), self.getModel(), self.getPriceRange(), self.getManufacturer(),
            self.getColor(), self.getCarHistory()
        )
    def __str__(self):
        return "Plate Number:   {}\nStatus: {}\nCar Type:   {}\nSeats:  {}\nFuel Type:  {}\nModel:  {}\nPrice Range:    {}\nManufacturer:   {}\nColor:  {}\nCar History:    {}".format(
            self.getPlateNumber(), self.getStatus(), self.getCarType(), self.getSeats(),
            self.getFuelType(), self.getModel(), self.getPriceRange(), self.getManufacturer(),
            self.getColor(), self.getCarHistory()
        )

class Order:
    def __init__(self, rented, returned, days, cost, car, customer, employee):
        self.__rented = rented
        self.__returned = returned
        self.__days = days
        self.__cost = cost
        self.__car = car
        self.__customer = customer
        self.__employee = employee
    
    def setRented(self, new_rented):
        self.__rented = new_rented
    def setReturned(self, new_returned):
        self.__returned = new_returned
    def setDays(self, new_days):
        self.__days = new_days
    def setCost (self, new_cost):
        self.__cost = new_cost
    def setCar(self, new_car):
        self.__car = new_car
    def setCustomer(self, new_costumer):
        self.__costumer = new_costumer
    def setEmployee(self, new_employee):
        self.__employee = new_employee
    
    def getRented(self):
        return self.__rented
    def getReturned(self):
        return self.__returned
    def getDays(self):
        return self.__days
    def getCost (self):
        return self.__cost
    def getCar(self):
        return self.__car
    def getCustomer(self):
        return self.__customer
    def getEmployee(self):
        return self.__employee
    
    def __repr__(self):
        return "Order({},   {}, {}, {}, {}, {}, {})".format(
            self.getRented(), self.getReturned(), self.getDays(), self.getCost(), self.getCar(),
            self.getCustomer(), self.getEmployee()
        )
    def __str__(self):
        return "Rented: {}\nReturned:   {}\nDays:   {}\nCost:   {}\nCar:    {}\nCustomer:   {}\nEmployee:   {}".format(
            self.getRented(), self.getReturned(), self.getDays(), self.getCost(), self.getCar(),
            self.getCustomer(), self.getEmployee()
        )
employee1 = Employee("Jerry", "2609998877", 1, "IloveCatsInWhite")
customer1 = Customer("Mrs. Kitty", "8254898489", "Privite Drive 4", "55555555", "Icelandia", "None")
car1 = Car("55-AK7", "Laus", "Jeppli", 5, "Dísel", 2015, "15'000-50'000", "Hummer", "Red", "None")

order1 = Order("12-12-2010", "1-3-2011","4","50'000", car1, customer1, employee1)
print(order1)