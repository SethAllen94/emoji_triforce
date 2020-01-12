from math import ceil

# unicode for smiley face emoji
smiley_face = ("\U0001f600")

#Welcome message
print("Welcome to the Emoji Triforce generator!\n"
      "Please enter the desired height (lines of emojis) of your Triforce.\n"
      "Odd heights are not possible and are automatically rounded up.\n")

run = True
while run:
	try:
		height = int(input("Please enter the desired height of your Triforce."))
		height*1

		# Single triangle height
		st_height = ceil(height/2)
		
		# Make Triforce
		for i in range(st_height):
			print(" " * (st_height) + " " * (st_height - 1- i) + smiley_face * (i+1))
		for i in range(st_height):
			print(" " * (st_height - 1- i) + smiley_face * (i+1) + " " * (st_height - i - 1) + " " * (st_height - 1- i) + smiley_face * (i+1))

		again = input("Would you like to make another? (y/n)")
		if again == 'n':
			run = False
	
	except ValueError:
		print("Please enter an integer\n")

	
