# import libraries
from rotary import Rotary
from imu import MPU6050
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import micropython

# define UART communication
uart = machine.UART(0, 9600)


# I2C for MPU6050 and OLED display
# define i2c pin
i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)
# define imu comunicated with i2c
imu = MPU6050(i2c)
# addresses look-up
addr=[]
for i in range(len(i2c.scan())):
    addr.append(i2c.scan()[i])
    print("addr[", i, "]:", hex(addr[i]), sep="")
# define oled(Width, height, i2c, address)
oled = SSD1306_I2C(128, 32, i2c, addr[0])

# Encoders
# define GPIO for encoders
rotary_right = Rotary(2,3)
rotary_left = Rotary(6,7)
# define counting number for encoders
cnt_right=0
cnt_left=0
right_UART_info=0
left_UART_info=0
# counter
def rotary_changed_right(change):
    global cnt_right,right_UART_info
    if change == 1:
        cnt_right = cnt_right +1
    elif change == 2:
        cnt_right = cnt_right - 1
    print("cnt_right", cnt_right)
    right_UART_info="cnt_right:"+str(cnt_right)
    uart.write(str(right_UART_info))
    
# counter    
def rotary_changed_left(change):
    global cnt_left,left_UART_info
    if change == 1:
        cnt_left = cnt_left +1
    elif change == 2:
        cnt_left = cnt_left - 1
    print("cnt_left", cnt_left)
    left_UART_info="cnt_left:"+str(cnt_left)
    uart.write(str(left_UART_info))
    
    
# call back while encorders changing    
rotary_right.add_handler(rotary_changed_right)
rotary_left.add_handler(rotary_changed_left)



while True:
    # print IMU data
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,2)
#     print("ax",ax)
#     print("ay",ay)
#     print("az",az)
#     print("gx",gx)
#     print("gy",gy)
#     print("gz",gz)
#     print("tem",tem,type(tem))

    oled.fill(0)
    oled.text("ax:",0,1,1)
    oled.text("{:.2f}".format(ax),25,1,1)
    oled.text("ay:",0,10,1)
    oled.text("{:.2f}".format(ay),25,10,1)
    oled.text("az:",0,20,1)
    oled.text("{:.2f}".format(az),25,20,1)
    oled.text("gx:",65,1,1)
    oled.text("{:.2f}".format(gx),90,1,1)
    oled.text("gy:",65,10,1)
    oled.text("{:.2f}".format(gy),90,10,1)    
    oled.text("gz:",65,20,1)
    oled.text("{:.2f}".format(gz),90,20,1)    
    oled.show()
    
#     which_motor = input('Enter right or left:')
#     uart.write(str(which_motor))
#     step = input('Enter number of steps:')
#     uart.write(str(step))
    
    
    time.sleep(1)
    
    
    
    
    
    