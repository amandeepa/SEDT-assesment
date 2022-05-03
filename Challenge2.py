# Python program to return the maximum occurring character in the input string
ASCII_SIZE = 256

def ReturnMaxOccurringChar(str):

	count = [0] * ASCII_SIZE
	max = -1
	c = ''
	for i in str:
		count[ord(i)]+=1;

	for i in str:
		if max < count[ord(i)]:
			max = count[ord(i)]
			c = i

	return c
print("Please enter the string")
str = input()

print("Max occurring character is: ",ReturnMaxOccurringChar(str))
