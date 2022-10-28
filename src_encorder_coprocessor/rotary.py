# import libraries
from imu import MPU6050
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import micropython

# class Rotary
class Rotary:
    def __init__(self, EA, EB):
#         self.cnt=0
        self.handlers = []
        self.EA_Pin = Pin(EA, Pin.IN)
        self.EB_Pin = Pin(EB, Pin.IN)
        
        self.status_pre = (self.EA_Pin.value() << 1) | self.EB_Pin.value()
        # rotary_change interupt request
        self.EA_Pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
        self.EB_Pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
        # status table
        self.status_table = {"0": "no change in reading"      , "1": "clockwise rotation",
                            "2": "counter clockwise rotation", "3": "error",
                            "4": "counter clockwise rotation", "5": "no change in reading",
                            "6": "error"                     , "7": "clockwise rotation",
                            "8": "clockwise rotation"        , "9": "error",
                            "10": "no change in reading"      , "11": "counter clockwise rotation",
                            "12": "error"                     , "13": "counter clockwise rotation",
                            "14": "clockwise rotation"        , "15": "no change in reading"}
        
    # when rotary status is changing     
    def rotary_change(self, pin):   
        status_now = self.status_pre
        self.status_pre = (self.EA_Pin.value() << 1) | self.EB_Pin.value()
        status_tab = (status_now << 2) | self.status_pre
        # status table look-up
        if status_tab == 1 or status_tab == 7 or status_tab == 8 or status_tab == 14:
#             self.cnt = self.cnt + 1
            self.call_handlers(1)
#             print("status_tab:","{0:04b}".format(status_tab),"value:",status_tab)
#             print("cnt_1",self.cnt)
        elif status_tab == 2 or status_tab == 4 or status_tab == 11 or status_tab == 13:
#             self.cnt = self.cnt - 1
            self.call_handlers(2)
#             print("status_tab:","{0:04b}".format(status_tab),"value:",status_tab)
#             print("cnt_1",self.cnt)
        print("status_table", self.status_table[str(status_tab)])
        
    # call back while status changing
    def add_handler(self, handler):
        self.handlers.append(handler)
    def call_handlers(self, s):
        for num in self.handlers:
            num(s) 




# 
# 
#     while True:
#         ax=round(imu.accel.x,2)
#         ay=round(imu.accel.y,2)
#         az=round(imu.accel.z,2)
#         gx=round(imu.gyro.x)
#         gy=round(imu.gyro.y)
#         gz=round(imu.gyro.z)
#         tem=round(imu.temperature,2)
#         #print("ax",ax)
#         #print("ay",ay)
#         #print("az",az)
#         #print("gx",gx)
#         #print("gy",gy)
#         #print("gz",gz)
#         #print("tem",tem,type(tem))
# 
#         oled.fill(0)
#         oled.text("ax:",0,1,1)
#         oled.text("{:.2f}".format(ax),25,1,1)
#         oled.text("ay:",0,10,1)
#         oled.text("{:.2f}".format(ay),25,10,1)
#         oled.text("az:",0,20,1)
#         oled.text("{:.2f}".format(az),25,20,1)
#         oled.text("gx:",65,1,1)
#         oled.text("{:.2f}".format(gx),90,1,1)
#         oled.text("gy:",65,10,1)
#         oled.text("{:.2f}".format(gx),90,10,1)    
#         oled.text("gz:",65,20,1)
#         oled.text("{:.2f}".format(gx),90,20,1)    
#         
#         oled.show()
#         time.sleep(0.1)
        
