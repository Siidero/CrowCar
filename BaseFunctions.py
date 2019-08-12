import time;
import explorerhat;

#functions
def forward(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.two.forward(speed)
        explorerhat.motor.one.backward(speed)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
        
def backward(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.forward(speed)
        explorerhat.motor.two.backward(speed)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
def turn_right(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.forward(speed)
        explorerhat.motor.two.forward(speed)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def turn_left(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.backward(speed)
        explorerhat.motor.two.backward(speed)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()