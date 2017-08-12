from django.shortcuts import render
import serial
import time
# Create your views here.


# time.sleep(0.1)
# print ser.portstr
# print ser
# time.sleep(0.1)
# ser.close()


def info():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    # ser = serial.Serial('COM4', 9600)  # 注意选择串口号， 从 0 开始计数， 我的是 COM3 ，所以参数是 2
    # line = ser.readline()
    line = ser.readline().decode()
    if line.startswith('humidity'):
        d = line.split(':')
        f = (1024-int(d[1]))/10.24
        data = "当前土壤湿度：{:.2f}%".format(f)
    return data
    # print(time.strftime("%Y-%m-%d %X\t") + line.strip())
    # time.sleep(1)
    
    # 每 10 秒向窗口写当前计算机时间
    # a = int(time.strftime("%S"))
    # sep = a % 10
    # # print a, sep
    # if sep == 0:
    #     # ser.write("hello, I am hick, the time is : " + time.strftime("%Y-%m-%d %X\n"))  # write a string
    #     ser.writelines('open')
    # if sep == 5:
    #     ser.writelines('close')
    # if sep == 8:
    #     ser.writelines('sensor')


def index(request):
    i = info()
    return render(request, 'index.html', {'data': i})




