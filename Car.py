class Car:

    # Properties คุณสมบัติของคลาส ส่วนนี้จำเป็นต้องมีทุกคลาส ไม่มีไม่ได้
    color = "No color"
    brand = "No brand"
    number_of_seats = 4
    number_of_wheels = 4
    maxspeed = 0
    plate_id = ""

    # =============================================================
    # Constructor ขึ้นต้นด้วย def เพราะเป็น function
    # self หมายถึงเรียกตัวมันเองโดยทันที
    def __init__(self, color, brand, number_of_seats, number_of_wheels, maxspeed, plate_id):  # รับค่าจากผู้ใช้ภายนอก
        self.color = color  # self.color ส่งค่ากลับสู่ properties
        self.brand = brand
        self.number_of_seats = number_of_seats
        self.number_of_wheels = number_of_wheels
        self.maxspeed = maxspeed
        self.plate_id = plate_id

    # =============================================================
    # Methods
    def setColor(self, x):
        self.color = x

    def setBrand(self, x):
        self.brand = x

    def setNumberOfSeats(self, x):
        self.number_of_seats = x

    def setNumberOfWheels(self, x):
        self.number_of_wheels = x

    def setMaxSpeed(self, x):
        self.maxspeed = x

    def setPlateId(self, x):
        self.plate_id = x
    # =============================================================
    # สร้าง print Data

    def printData(self):
        print("Color : ", self.color)
        print("Brand : ", self.brand)
        print("Seats : ", self.number_of_seats)
        print("Wheels : ", self.number_of_wheels)
        print("Max Speed : ", self.maxspeed)
        print("Plate ID : ", self.plate_id)
