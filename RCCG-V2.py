#This is version 2 of the RCCG(Random Ceasar Cypher Generator). Ment to simplify the creation of "encrypted" messages allong with decoding them.
#V1 simply takes the user's message and randomly applies an alphabet shift then displays the encoded(shifted) message long with the amount shifted.
#While decoding it uses the encoded message given along with the shift amount to display the original message.
#The next versions are meant to simplify the user experience along with making the encoded messages increasingly difficult to decode without the use of the original program

alphabet = "abcdefghijklmnopqrstuvwxyz"

# convert between letters and numbers up to 26
def number_to_letter(i):
	return alphabet[i%26] # %26 does the wrap-around

def letter_to_number(l):
	return alphabet.find(l)# index in the alphabet

# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
	i = letter_to_number(l)
	if i == -1:# character not found in alphabet
		return ""# remove it, it's space or punctuation
	else:
		return number_to_letter(i + amount)# Caesar shift

#full text encode
def caesar_shift(text, amount):
	shifted_text = ""
	for char in text.lower():# converting uppercase to lowercase
		shifted_text += caesar_shift_single_character(char, amount)
	return shifted_text

### MAIN PROGRAM/ENCRYPTION MODES ###

mode = input("Would you like to ENCODE or DECODE?")
if mode == "encode":
	msg = input("Your Message:")

	import random
	cyph = random.randint(3, 23)#randomly choosing the shift amount, between 3 and 23 shifts
	code = caesar_shift(msg,cyph)#shifting the input string
	
	bini = ''.join(format(i, 'b') for i in bytearray(code, encoding ='utf-8'))#converting string to binary
	rev = bini#reversing the binary string ex; 1101 -> 1011

#redefining the numbers for the shift code output, shift of 3 letters is re-written as 73227 for output
	cyph_dict = {
    '3':'73227',
    '4':'43489',
    '5':'26276',
    '6':'76947',
    '7':'133645',
    '8':'26275',
    '9':'5607',
    '10':'40729',
    '11':'80743',
    '12':'148510',
    '13':'72985',
    '14':'37128',
    '15':'86863',
    '16':'32542',
    '17':'174415',
    '18':'78835',
    '19':'64693',
    '20':'63429',
    '21':'17313',
    '22':'81864',
    '23':'39286',
	}
	hex = (cyph_dict[str(cyph)])#naming the dict output

	print(rev[::-1]+",-"+hex)#printing the encoded message with the re-mapped shift code

if mode == "decode":
	x, y = input("Coded Message:") .split(",")#one line input for both the code and shift ammount

#making the shift ammount back into a redable for for the program
	hex_dict = {
    '-73227':'-3',
    '-43489':'-4',
    '-26276':'-5',
    '-76947':'-6',
    '-133645':'-7',
    '-26275':'-8',
    '-5607':'-9',
    '-40729':'-10',
    '-80743':'-11',
    '-148510':'-12',
    '-72985':'-13',
    '-37128':'-14',
    '-86863':'-15',
    '-32542':'-16',
    '-174415':'-17',
    '-78835':'-18',
    '-64693':'-19',
    '-63429':'-20',
    '-17313':'-21',
    '-81864':'-22',
    '-39286':'-23',
	}
	#transforming y(hex) from string to integer
	h = hex_dict[y]
	int_h = int(h)

	fwrd = x[::-1]#reversing the binary string in correct order ex; 1011 -> 1101

#binary back into letters
	def BinaryToDecimal(binary):  
		binary1 = binary
		decimal, i, n = 0, 0, 0
		while(binary != 0):  
			dec = binary % 10
			decimal = decimal + dec * pow(2, i)  
			binary = binary//10
			i += 1
		return (decimal)
	
	bin_data = fwrd
	str_data =''

	for i in range(0, len(bin_data), 7):
		temp_data = int(bin_data[i:i + 7])
		decimal_data = BinaryToDecimal(temp_data)
		str_data = str_data + chr(decimal_data)
	

	code = caesar_shift(str_data,int_h)#shifting the alphabet back into their original position
	
	print("Original Message:",code)#printing the original message

input("press enter to finish: ")

 #RCCG-V2 12/02/2021 Created by; Artus aka. AlmondMan