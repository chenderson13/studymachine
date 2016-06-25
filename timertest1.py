def main():
	print ("\nThis timer is a great way to get started."
		"It's a way to dip your toe in knowing that you've only committed to working for a small amount of time and are 'allowed' to stop afterward.",
		"\n\nSet the timer for the shortest amount of time you *know* you can work continuously. Even three minutes is fine for a start!")
	import time
	customtime = int(raw_input("How many minutes would you like to set the timer for? :" ))
	#customtime = customtime * 60	
	run =  raw_input("Type '1' when you're ready to start: ")
# Only run if the user types in "1"
	if run == "1":
		print ("The timer has been set for %i minutes." % (customtime))
		print "A sound will play when the time is up."
		import threading as _threading
		t = _threading.Timer(customtime, TimerEnd)
		t.start()
	else:
		pass	
		
# def timer():
# 	import threading as _threading
# 	t = _threading.Timer(customtime, TimerEnd)
# 	t.start()
		

def TimerEnd():
 	print "Time's Up!"

	
# def sound():
# 	import pygame
# 	import time     
# 	pygame.init()
# 	song = pygame.mixer.Sound('Chime.wav')
# 	clock = pygame.time.Clock()
# 	song.play()
# 	while True:
# 		clock.tick(60)
# 		time.sleep(2)
#   		break
# 	pygame.quit()
if __name__ == '__main__':
	main()