#This is version 3 of the RCCG(Random Ceasar Cypher Generator). Ment to simplify the creation of "encrypted" messages allong with decoding them.
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

#turning the binary code, 1's and 0's, into different numbers, ex; 0 -> 8 and 10 -> 6
	str_oz = rev.replace('10', '6')
	str_zo = str_oz.replace('01', '3')
	str_z = str_zo.replace('0', '8')
	str_o = str_z.replace('1', '5')

#redefining the numbers for the shift code output, shift of 3 letters is re-written as 73227 for output
	cyph_dict = {
    '3':'73|227',
    '4':'434|89',
    '5':'262|76',
    '6':'76|947',
    '7':'133|645',
    '8':'262|75',
    '9':'56|07',
    '10':'407|29',
    '11':'80|743',
    '12':'148|510',
    '13':'72|985',
    '14':'3|7128',
    '15':'868|63',
    '16':'32|542',
    '17':'17441|5',
    '18':'78|835',
    '19':'6469|3',
    '20':'6|3429',
    '21':'17|313',
    '22':'818|64',
    '23':'39|286',
	}
	hex = (cyph_dict[str(cyph)])#naming the dict output
	a, b = hex .split("|")

	print("Encoded Message: "+a+"01"+str_o[::-1]+"10"+b)#printing the encoded message with the re-mapped shift code

if mode == "decode":
	a, b = input("Coded Message:") .split("01")#one line input for both the code and shift ammount
	x, c = b .split("10")#x is the actual message, c is the 2nd part of the shift code

#making the shift ammount back into a redable for for the program
	hex_dict = {
    '73227':'3',
    '43489':'4',
    '26276':'5',
    '76947':'6',
    '133645':'7',
    '26275':'8',
    '5607':'9',
    '40729':'10',
    '80743':'11',
    '148510':'12',
    '72985':'13',
    '37128':'14',
    '86863':'15',
    '32542':'16',
    '174415':'17',
    '78835':'18',
    '64693':'19',
    '63429':'20',
    '17313':'21',
    '81864':'22',
    '39286':'23',
	}
	#transforming y(hex) from string to integer
	h = hex_dict[a+c]
	int_h = (-int(h))

	fwrd = x[::-1]#reversing the binary string in correct order ex; 1011 -> 1101

#replacing the numbers of the encoded message back into Binary, 1's and 0's
	str_o = fwrd.replace('5', '1')
	str_z = str_o.replace('8', '0')
	str_zo = str_z.replace('3', '01')
	str_oz = str_zo.replace('6', '10')

#binary back into letters
	def BinaryToDecimal(binary):
		decimal, i, n = 0, 0, 0
		while(binary != 0):  
			dec = binary % 10
			decimal = decimal + dec * pow(2, i)  
			binary = binary//10
			i += 1
		return (decimal)
	
	bin_data = str_oz
	str_data =''

	for i in range(0, len(bin_data), 7):
		temp_data = int(bin_data[i:i + 7])
		decimal_data = BinaryToDecimal(temp_data)
		str_data = str_data + chr(decimal_data)
	

	code = caesar_shift(str_data,int_h)#shifting the alphabet back into their original position
	
	print("Original Message:",code)#printing the original message

input("press enter to finish: ")

 #RCCG-V3.01 18/04/2023 Created by; Artus aka. AlmondMan
 #(MM/DD/YYY)