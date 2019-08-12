import picamera
import io
import logging
import socketserver
from threading import Condition
from http import server

# Page html qui sert à afficher le stream sur l'adresse
PAGE="""\ 
<html>
<head>
<title>Eh mais ça marche</title>
</head>
<body>
<img src="stream.mjpg" width=100% height=100% />
</body>
</html>
"""

class StreamingOutput(object): # Classe qui sert à recuperer le stream de la camera
	def __init__(self): # Initialisation de la classe
		self.frame = None # Pas de frame de base
		self.buffer = io.BytesIO() # Variable qui recupere la flux a envoyer
		self.condition = Condition() # Permet de donner des conditions a la classe, ce qui permet de bloquer le flux en attendant un signal
# La fonction write dans la classe permet de dire a la fonction start_recording() que cette classe peut stocker la video
	def write(self, buf):
		if buf.startswith(b'\xff\xd8'): # Cette suite de caractère permet de signaler qu'on est au debut d'une image, donc qu'on est a une nouvelle frame
			self.buffer.truncate() # On redimentionne le flux 
			with self.condition: # Teste le lock de la classe ? Si oui, on rentre dans la suite
				self.frame = self.buffer.getvalue() # On recupere la valeur de l'image
				self.condition.notify_all() # On delock tous les threads
			self.buffer.seek(0) # On repositionne l'offset sur le buffer a 0
			return self.buffer.write(buf) # On renvoie l'image en ecriture

class StreamingHandler(server.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.send_response(301)
			self.send_header('Location', '/index.html')
			self.end_headers()
		elif self.path == '/index.html':
			content = PAGE.encode('UTF-8')
			self.send_response(200)
			self.send_header('Content-Type', 'text/html')
			self.send_header('Content-Lenght', len(content))
			self.end_headers()
			self.wfile.write(content)
		elif self.path == '/stream.mjpg':
			self.send_response(200)
			self.send_header('Age', 0)
			self.send_header('Cache_Control', 'no-cache, private')
			self.send_header('Pragma', 'no-cache')
			self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
			self.end_headers()
		try:
			while True:
				with output.condition:
					output.condition.wait()
					frame = output.frame
					self.wfile.write(b'--FRAME\r\n')
					self.send_header('Content-Type', 'image/jpeg')
					self.send_header('Content-Lenght', len(frame))
					self.end_headers()
					self.wfile.write(frame)
					self.wfile.write(b'\r\n')
			except Exception as e:
				logging.warning('Removed Streaming Client %s %s', self.client_address, str(e))
		else:
			self.send_error(404)
			self.end_headers()
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
	allow_reuse_address = True
	daemon_threads = True

def PiStreaming():
	with picamera.PiCamera(resolution='1280x720', framerate=24) as camera:
		output = StreamingOutput()
		camera.start_recording(output, format='mjpeg')
		camera.rotation = 180
		try:
			address = ('', 8000)
			server = StreamingServer(address, StreamingHandler)
			server.serve_forever()
		finally:   
			camera.stop_recording()