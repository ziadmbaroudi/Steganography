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

# function: is_even() #
# This function tests whether a number is even 
# parameter: num   - any positive integer       
# returns:   True  - if num is even
#            False - otherwise
def is_even(num):
	if (num %2) == 0:
		return True
	else:
		return False

# function: encode()
# converts a string of text into a list of ascii strings
# parameter: text - a string
# returns:   enc_text - a list of ascii strings, each
#            corresponding to a character in text
def encode(text):
	enc_text = []
	# repeat for each character: find the letter in the dictionary 
	# and put its binary part in a list
	for character in message:
		enc_text.append(ascii_dict[character])
	return enc_text

# function: hide_in_pix()
# hides a message, in ascii, in the last bit of each pixel
# value of an image
# parameters: msg_length - length, in characters, of message
#             msg        - list of ascii codes representing message
#             img        - black and white PNG inside of which to hide
#                          the message
# returns:    img        - the image after altering the last bit of each
#                          pixel value to encode msg
def hide_in_pix(msg_length, msg, img):
	max_to_process = msg_length * 8 # pixels to process. Each pixel
									# contributes one bit. Each
									# character needs 8 bits.
	pixels_processed = 0
	letter_index = 0
	l = 0
	for x in range(img.width):
		for y in range(img.height):
			val = img.getpixel((x,y))
			letter = msg[letter_index]
			#### possible actions required ####
			# We need a 0 in least significant bit of pixel value
			# pixel value already ends with 0 (is even)
			# Do nothing
			if letter[l] == '0' and is_even(val):
				pass 
			# Need 0, pixel value ends with 1 (is odd)
			# change least significant bit to 0
			elif letter[l] == '0' and not is_even(val):
				pos_val = val - 1 
				img.putpixel((x,y), pos_val)
			# Need 1, pixel value ends with 1 (is odd)
			# Do nothing
			elif letter[l] == '1' and not is_even(val):
				pass 
			# Need 1, pixel value ends with 0 (is even)
			# change least significan bit to 1
			elif letter[l] == '1' and is_even(val):
				neg_val = val + 1
				img.putpixel((x,y), neg_val)
			pixels_processed += 1
			l += 1
			if l == 8: # since l needs to be 0 .. 7
				l = 0
				letter_index += 1
			if pixels_processed == max_to_process: # all characters processed
				return img


# Information for user
message = input('What message do you want to encode? (140 character limit): ')

file = input('What is the name of the image file you want to use? ')

code = encode(message)
# print(code)

# Image hiding 
img = Image.open(file)

img = hide_in_pix(len(code), code, img)
img.save("new_" + file)
