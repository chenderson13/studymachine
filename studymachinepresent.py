#study habits machine

def Start():
	print("\n_________________________________Study Machine__________________________________\n")
	print ("\nWelcome to the Study Machine! Study Machine will guide you through exercises to help you complete projects," 
		"study for exams, and memorize your notes. If you don't know where to start, start with Study Machine!\n")

def main_problem(): 
	print "What's the biggest issue for you right now?\nIf you have more than one of these problems don't worry, just pick one to start with.\n\n"

timer_rep = 0


def main_menu(resp):
	if resp == "m":
		problem_choice()
	else:
		pass		

def problem_choice():
	main_problem()
	problem_input = raw_input("A. I don't feel ready to start\nB. I'm having a hard time staying on track\n>" )
	problem_input = input_clean(problem_input)
	if problem_input == "a":
	 	gettin_started()
	elif problem_input == "b":
		starting_strategy()
	else:
		print "\nPlease enter the letter for the issue you want to start with:\n"
		problem_choice()

def input_clean(var):
	var = var.lower()
	var = var.replace(".", "")
	return var		

def gettin_started():
	print "\nLet's get you started!\nPress 'M' at any time to return to the main menu.\n"
	started_selfcare = raw_input("\nAre you feeling ready to start laying our your material? Are you in a head space where you can start working?\n"
		"A. As ready as I'll ever be!\nB.To be honest, I'm freaking out.\n")
	started_selfcare = input_clean(started_selfcare)
	if started_selfcare == "a":
		started_ready()
	if started_selfcare == 'b':
		print ("\nThat's okay, we've all been there! It's important to get to a calmer head space before you start working.\n\t-You will work faster and more effectively"
		"\n\t-You will be able to learn complex material much more easily\n\t-You will retain material much better if you aren't as stressed\n\n")
		selfcare_choice()
	else:
		gettin_started()	

def selfcare_choice():
	stressed_selfcare = raw_input("There are fast, proven methods for quickly powering down your stress response and getting back on track. Would you like to:\n"
			"A. Run through a basic self-care checklist\nB. Try some simple breathing and mindfulness techniques\nC. Turn on some word-free study music\nD. I feel okay, let's move on\n")
	stressed_selfcare = input_clean(stressed_selfcare)
	main_menu(stressed_selfcare)
	if stressed_selfcare == "a":
		selfcare_checklist()
	elif stressed_selfcare == "b":
		deepbreathe()
	elif stressed_selfcare == "c":
		music()
	elif stressed_selfcare == "d":
		started_ready()		
	elif stressed_selfcare == "m":
		problem_choice()	
	else:
		selfcare_choice
			
			
def selfcare_checklist():
	print("Each of these items addresses a basic need. If your body isn't taken care of it will be much harder to work effectively.")
	print ("It's worth the few minutes to go through the list and take care of any unaddressed needs. Press 'M' at any time to quit to main menu.\n")
	self_one = raw_input("Have you had something to eat and drink in the last few hours? You aren't hungry or thirsty?\nY/N\n\n")
	self_one = input_clean(self_one)
	main_menu(self_one)
	if self_one == "y":
		print ("\n")
		print u'\u2713'
	elif self_one == "n":
		print("\nTake a minute to grab a snack or make some tea. Being hungry or thirsty adds extra stress.\n") 
	else:
		print ("\n")
	self_two = raw_input("Have you gotten enough sleep in the past day?\nY/N\n")
	self_two =	input_clean(self_two)
	main_menu(self_two)
	if self_two == "y":
		print ("\n")
		print u'\u2713'
	elif self_two == "n":
		print ("Even if you have a lot to get done, sleep is extremely important for performance. Even taking a nap can help.")
	else:
		print ("\n")
	self_three = raw_input("Are you physically comfortable? Not too cold or dealing with too much noise?\nY/N\n\n")
	self_three = input_clean(self_three)
	if self_three == "y":
		print ("\n")
		print u'\u2713'
	elif self_three == "n":
		print ("Take care of yourself - find a sweater, a fan, a comfy couch, or a quiet spot at a library.")
	else:
		print ("\n")
	print "Know it's important to take care of yourself before you try to get to work. Meet your basic needs before trying to push yourself!\n\n"
	selfcare_choice()			

			# self_2 = sleep
			# self_3 = comfort
			# self_4 = move
			# self_5 = self-talk
			# self_6 = environment
def deepbreathe():
	video_yn = raw_input ("Enter 'Y' to be taken to a five minute, online deep breathing exercise. Enter 'N' to be taken back to the self care checlist.\n> ")
	video_yn = input_clean(video_yn)
	if video_yn == "y":
		import webbrowser
		webbrowser.open('https://www.youtube.com/watch?v=awc8MLSpjlQ', new=0, autoraise=True)
		selfcare_choice()
	if video_yn == "n":
		selfcare_choice()
	else:
		selfcare_choice()	

	

def music():
	music_yn = raw_input("Enter 'Y' to be taken to an online selection of study playlists with no words. Enter 'N' to be taken back to the self care checlist.\n> ")
	music_yn = input_clean(music_yn)
	if music_yn == "y":
		import webbrowser
		webbrowser.open('https://play.google.com/music/listen?authuser&u=0#/wbs/JZC20/JZC387', new=0, autoraise=True)
		selfcare_choice()
	if music_yn == "n":
		selfcare_choice()
	else:
		selfcare_choice()	

		
#to print checkmark for self care checklist
#print u'\u2713'

def started_ready():
	supplies_ready = raw_input("Do you have your supplies and work area ready? Your notes, pen, calculator, etc.? This is often the easiest part!\nY/N?\n")
	supplies_ready = input_clean(supplies_ready)
	if supplies_ready == "y":
		print ("\nGreat, let's try to actually do some work!\n")
		starting_strategy()
	elif supplies_ready == "n":
		prepping_supplies = raw_input("\nFind a good spot to work and get everything together. When you're done, enter 'ok' to move on and start working.\n")
		prepping_supplies = input_clean(prepping_supplies)	
		if prepping_supplies == "ok" or prepping_supplies == "okay":
			starting_strategy()
	else:
		print ("\nAnswer with 'Y' or 'N'.\n")
		started_ready()		

def starting_strategy():
	print ("\nLet's choose a strategy to get started.\n"
	"(A.) Will be most helpful if you are ready to start but having trouble taking the first step.\n(B.) Will be most helpful if you're ready to dive in but are a little intimidated by the amount of work.\n")
	start_choice = raw_input("\t-A. Start Small and Work Up- Set Short Time Goals\n\t-B. Get Going - Set a Longer Timer with Planned Breaks\n")
	start_choice = input_clean(start_choice)
	if start_choice == "a":
		short_timer()
	elif start_choice == "b":
		pomodoro()
	elif start_choice == "m":
		problem_choice()	
	else:
		print ("Choose 'A' or 'B' to choose a starting strategy or 'M' to return to main menu.")		



def short_timer():
	print ("\nThis timer is a great way to get started."
		"It's a way to dip your toe in knowing that you've only committed to working for a small amount of time and are 'allowed' to stop afterward.\n\nSet the timer for the shortest amount of time you *know* you can work continuously. Even three minutes is fine for a start!\n>")
	import time
	customtime = int(raw_input("How many minutes would you like to set the timer for? :" ))
	customtime = customtime * 60	
	run =  raw_input("Type '1' when you're ready to start: ")
# Only run if the user types in "1"
	if run == "1":
		global customtime
		print ("The timer has been set for %i minutes." % ((customtime/60)))
		print "A sound will play when the time is up."
		sound()
		timer_rstrt()
		#timer()
	else:
		pass	
		
# def timer():
# 	import threading as _threading
# 	t = _threading.Timer(customtime, TimerEnd)
# 	t.start()
# 	pass
		

def TimerEnd():
	print "Time's Up!"
	sound()
	timerend_rstrt
	
def sound():
	import pygame
	import time     
	pygame.init()
	song = pygame.mixer.Sound('Chime.wav')
	clock = pygame.time.Clock()
	song.play()
	while True:
		clock.tick(60)
		time.sleep(2)
  		break
	pygame.quit()



	
def timer_rstrt():	
	restrt = raw_input("Would you like to try going a little longer this time?\nEnter '1' to reset the timer\nEnter '2' to try a longer, more structured timer\nEnter '3' to return to the main menu\n>")
	if restrt == "1":
		short_timer()
	elif restrt == "2": 
		pomodoro()
	elif restrt == "3":
		starting_strategy()
	else:
		short_timer() 	
					

# t = Timer(customtime, hello)
# t.start()  # after 30 seconds, "hello, world" will be printed


def pomodoro():
	print ("\nThe Pomodoro method encourages you to stay on task by allowing for a built-in 10-minute break after a work session. This builds in breaks so that you can work longer without burning out.\n")
	import time
	pomodoroselect = (raw_input("Would you like to try (A) 50/10 work sessions or (B) 20/10 work sessions?\n>" ))
	if pomodoroselect == "a":
		fifty_ten()
	elif pomodoroselect == "b":
		twenty_ten()
	elif pomodoroselect == "m":
		problem_choice()	
	else:
		pomodoro()

def fifty_ten():
	run =  raw_input("Type '1' when you're ready to start:\n ")
	if run == "1":
		print ("The timer has been set for 50 minutes. Work the whole time!")
		print ("A sound will play when the time is up.")
		#timer50()
		sound()
		timer10()
	else:
		pass					

def twenty_ten():	 
	run = raw_input("Type '1' when you're ready to start:\n ")
	if run == "1":
		print ("The timer has been set for twenty minutes.")
		print ("A sound will play when the time is up.")
		#timer20()
		sound()
		timer10()
	else:
		pass	

def timer50():
	import time
	import threading as _threading
	t = _threading.Timer(3000, timer10)
	t.start()

def timer20():
	import time
	import threading as _threading
	t = _threading.Timer(1200, timer10)
	t.start()


def timer10():
	run = raw_input("Type '1' when you're ready to start your 10 minute break!:\n> ")
	if run == "1":
		print ("The timer has been set for ten minutes.")
		print ("A sound will play when the time is up.")
	import time
	import threading as _threading
	t = _threading.Timer(600, timer10end)
	t.start()		

def timer10end():
	sound()
	print ("Choose another study period!")
	pomodoro()			

# 50/10s

# starting_small

# study_techniques
# 	what is the problem?
# 		can't get started on work
# 			get ready
#				-headspace
					# -self-care
					# 	-physical
					# 	-breathing
					# 	-music
		
#			-checklist (can be a dictionary with \n on each line???)
# 			-starting small w/timer
# 			-50/10s or 20/10s	


# 		don't understand material
# 			reviewing at your own pace
# 			secondary sources
# 			reorganizing notes

# 		can't remember material
# 			reorganizing notes
# 			flash cards
# 			explain
# idea- make *all* response options tabbed in?
	
def main():
	Start()
	problem_choice()

if __name__ == '__main__':
		main()	
