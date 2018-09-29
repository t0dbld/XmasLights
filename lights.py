import socket
import time

UDP_IP = "192.168.1.1"
UDP_PORT = 1281

MESSAGE = "kleCMD2afe00030f(&'+2"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

amPM = time.strftime('%p')
currentTime = time.strftime('%H%p')
print currentTime

while True:
	
	if currentTime == "18PM":
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		print "Color Wave"
		time.sleep(3600)
	elif currentTime == "19PM":
		sock.sendto("kleCMD05000000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050100FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05020000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050300FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05040000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050500FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05060000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050700FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05080000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050900FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050A0000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050B00FF00(&'+3", (UDP_IP, UDP_PORT))
		print "set red and green"
		time.sleep(300)
		sock.sendto("kleCMD38fe0000FF(&'+", (UDP_IP, UDP_PORT))
		print "set red with white trails"
		time.sleep(300)
		sock.sendto("kleCMD38fe00FF00(&'+", (UDP_IP, UDP_PORT))
		print "set gren with white trails"
		time.sleep(300)
		sock.sendto("kleCMD25fe0000FF(&'+", (UDP_IP, UDP_PORT))
		print "set red white sparkle"
		time.sleep(300)
		sock.sendto("kleCMD25fe00FF00(&'+", (UDP_IP, UDP_PORT))
		print "set to green and white sparkle"
		time.sleep(300)
		sock.sendto("kleCMD05000000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050100FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05020000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050300FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05040000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050500FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05060000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050700FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05080000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050900FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050A0000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050B00FF00(&'+3", (UDP_IP, UDP_PORT))
		print "set red and green"
		time.sleep(300)
		sock.sendto("kleCMD38fe0000FF(&'+", (UDP_IP, UDP_PORT))
		print "set red with white trails"
		time.sleep(300)
		sock.sendto("kleCMD38fe00FF00(&'+", (UDP_IP, UDP_PORT))
		print "set green with white trails"
		time.sleep(300)
		sock.sendto("kleCMD25fe0000FF(&'+", (UDP_IP, UDP_PORT))
		print "set red white sparkle"
		time.sleep(300)
		sock.sendto("kleCMD25fe00FF00(&'+", (UDP_IP, UDP_PORT))
		print "set to green and white sparkle"
		time.sleep(1200)

	elif currentTime == "20PM":
		sock.sendto("kleCMD22FF0000FF(&'+", (UDP_IP, UDP_PORT))
		print "set cascading"
		time.sleep(3600)
	elif currentTime == "21PM":
		sock.sendto("kleCMD21fe0000FF(&'+", (UDP_IP, UDP_PORT))
		print "set fade in and out"
		time.sleep(3600)
	elif currentTime == "22PM":
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		print "set Color Wave"
		time.sleep(3600)
	elif currentTime == "23PM":
		sock.sendto("kleCMD05000000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050100FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05020000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050300FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05040000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050500FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05060000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050700FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD05080000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050900FF00(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050A0000FF(&'+3", (UDP_IP, UDP_PORT))
		time.sleep(1)
		sock.sendto("kleCMD050B00FF00(&'+3", (UDP_IP, UDP_PORT))
		print "set red and green"
		time.sleep(3600)

	else:
		sock.sendto("kleCMD2800000000(&'+\00\003", (UDP_IP, UDP_PORT))
		print "Turning lights off"
		time.sleep(64800)
