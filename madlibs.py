def main():
	time = input("Enter a number from 1 to 12 :")
	items = str(input("Enter a noun (plural) :"))
	name= str(input("Enter a name :")).capitalize()
	scream = str(input("Enter any sentence :")).upper()
	action = str(input("Enter a verb :"))

	print("It was "+ str(time) + " o'clock when I heard a knock at the door."
	"I opened the door and there was a box full of " + items + " with a note saying From "+ name +
	" Just as I closed the door I heard a scream "+ scream +" I froze in place and all I could do was "+ action +".")

if __name__ == '__main__':
	main()
