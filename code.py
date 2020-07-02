import speech_recognition 
import pyttsx3
from datetime import date
from datetime import datetime



robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)

	print("Robot:...")
	
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)

	# hieu.py
	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:	
		robot_brain	= "hello Dinh Tung"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "president" in you:
		robot_brain = "Donald Trump"

	elif "bye" in you:
		robot_brain = "bye Dinh Tung"
		print("Robot: " + robot_brain )
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else :
		robot_brain ="I'm fine thank you"
	
	print("Robot: " + robot_brain )
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()