import time;
import explorerhat;

def motor1_forward():
    curr_time = time.time()
    final_time = curr_time + 3
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.forward(50)
    print("finished")

motor1_forward()