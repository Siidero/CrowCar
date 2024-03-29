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
        
def backward(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.forward(speed)
        explorerhat.motor.two.backward(speed)
    
def turn_right(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.forward(speed)
        explorerhat.motor.two.forward(speed)

def turn_left(speed, temp):
    curr_time = time.time()
    final_time = curr_time + temp
    while curr_time <= final_time:
        curr_time = time.time()
        explorerhat.motor.one.backward(speed)
        explorerhat.motor.two.backward(speed)
#main
turn_right(50,1)