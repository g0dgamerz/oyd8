import time
import random
def haha():
	a=input('enter y key to continue and other key to exit')
	if a=='y':
		i=6
		while i>0:
			print("you have %d life left"%i)

			
			n=random.randint(1,100)
			guess=int(input("enter integer from 1 to 100:"))
			while n != "guess":
				print
				if guess<n:
					i -= 1
					if i<0:
						print('game over')
						break
					else:	
						print("guess is low")
						print("you have %d life left"%i)
						guess =int(input("enter integer from 1 to 100:"))
				elif guess>n:
					i -= 1
					if i<0:
						print('game over')
						break
					else:
						print("guess is high")
						print("you have %d life left"%i)
						guess= int(input("enter an integer from 1 to 100:"))
				else:
					print("you gussed it")
					break
					

	else:
		print('so you are not game addict goto hell')
		exit()

def sleeper():
    while True:
        # Get user input
        print('welcome to game ')
        num=input("please press 2 and hit enter:")
 
        # Try to convert it to a float
        try:
            num = float(num)
            time.sleep(2)
            print("Are you ready to play?")
            haha()
        except ValueError:
            if a=='y':
            	print('ok')
            else:
            	print('fuck')
try:
    sleeper()
    
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
