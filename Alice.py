from PIL import Image
# Ascii dictionary to change the letters to binary numbers
ascii_dict = {
'a' : '01100001',
'b' : '01100010',
'c' : '01100011',
'd' : '01100100',
'e' : '01100101',
'f' : '01100110',
'g' : '01100111',
'h' : '01101000',
'i' : '01101001',
'j' : '01101010',
'k' : '01101011',
'l' : '01101100',
'm' : '01101101',
'n' : '01101110',
'o' : '01101111',
'p' : '01110000',
'q' : '01110001',
'r' : '01110010',
's' : '01110011',
't' : '01110100',
'u' : '01110101',
'v' : '01110110',
'w' : '01110111',
'x' : '01111000',
'y' : '01111001',
'z' : '01111010',
' ' : '00100000'
}

# reversing the Ascii dictionary: Swapping the meaning and the definition
rev_ascii = {}
for k, v in ascii_dict.items():
	rev_ascii[v] = k

# function: is_even() #
# This function tests whether a number is even 
# parameter: num   - any positive integer       
# returns:   True  - if num is even
#            False - otherwise
def is_even(num):
	if (num%2) == 0:
		return True
	else:
		return False

# function:  decode() #
# turns ASCII strings into characters via lookup in rev_ascii dictionary
# parameter: enc_list - list of binary strings, 
#            each representing a character
# returns:   dec_text - list of characters
def decode(enc_list):
	dec_text = []
	# For each binary string in the list: 
	#     Find the binary string in the dictionary and put its 
	#     letter part in the list
	for bits in one_d_arr:
		dec_text.append(rev_ascii[bits])
	return dec_text

# function:   read_bits()
# reads least significant bits of pixel values in the image
# parameters: num_bits  - number of bits to be read from image file
#             img - The image as 2D array of pixel values in memory
# returns:    one_d_arr - list of ASCII strings representing the
#             message hidden in image
def read_bits(num_bits, img):
	one_d_arr = []
	bits_so_far = 0
	letter_num = 0
	bit_str = ''
	for x in range(img.width):
		for y in range(img.height):
			pixel = img.getpixel((x, y))
			if is_even(pixel): # least significant bit is 0
				bit_str += "0"
			else:			   # least significant bit is 1
				bit_str += "1"
			bits_so_far +=1

			if len(bit_str) == 8: # whole character's ASCII code
				one_d_arr.append(bit_str)
				bit_str = ''

			if bits_so_far == num_bits: # all bits have been read
				return one_d_arr

num_characters = int(input("How many characters are there to decode? "))
num_bits = 8*num_characters

fname = input("What is the name of the image file you want to use? ")
img = Image.open(fname)
# Finding Message
one_d_arr = read_bits(num_bits, img)

# The message will be the decoded version of the one dimensional array list however it will be a list itself so the join is used to make it into a string instead of a list
mess = decode(one_d_arr)
mess = ''.join(mess)
print(mess)
