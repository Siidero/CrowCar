#import all of files
from threading import Thread
import BaseFunctions
import time

#use functions of BaseFunctions
class Streaming(Thread):		# Classe qui servira a lancer le stream en parallèle
	def __init__(self):
		Thread.__init__(self)
	
	def run(self):
		import streaming


thread_stream = Streaming()
thread_stream.start()
time.sleep(15)
BaseFunctions.turn_left(50,1)
BaseFunctions.turn_right(50,1)
BaseFunctions.forward(50,1)
BaseFunctions.backward(50,1)
thread_stream.join()