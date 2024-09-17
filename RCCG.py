#This is version 4A of the RCCG(Random Ceasar Cypher Generator). Meant to simplify the creation of "encrypted" messages allong with decoding them.
#Completely overhaulled ceasar shift and binary converstion! After 4 years this program can finally handle spaces in text, LFG!

#THIS SCRIPT IS NOT TO BE SHARED AND IS AN ALPHA BUILD NOT MEANT FOR PUBLIC RELEASE
#This is a modified script made for GUI use
import yaml

alphabet = "abcdefghijklmnopqrstuvwxyz"

# convert between letters and numbers up to 26
def number_to_letter(i):
	return alphabet[i%26] # %26 does the wrap-around

def letter_to_number(l):
	return alphabet.find(l)# index in the alphabet

# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
  if l == " ":
    return l
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

#full text decode
def caesar_shift_decrypt(text, amount):

    shifted_text = caesar_shift(text, -amount)
    return shifted_text

#converting the roman letters into binary, 1's and 0's
def words_to_binary(sentence):
    return ''.join([f'{ord(letter):08b}' for letter in sentence])

#converting binary 1's and 0's into roman letters
def binary_to_words(binary):
    characters = [binary[i:i+8] for i in range(0, len(binary), 8)]
    sentence = ''
    for character in characters:
        sentence += chr(int(character,2))
    return sentence

#redefining the numbers for the shift code output, ex; shift of 3 letters is re-written as 73227 for output
#function to load dictionary from config file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

config = load_config('config.yaml')
cyph_dict = config['cyph_dict']

### MAIN PROGRAM/ENCRYPTION MODES ###

#start of encoding
def encode(msg):

    #randomly choosing a shift amount between 3 to 23, and 27 to 35
    from random import randint, choice
    for _ in range(5):
        r = choice([(3,23),(27,35)])
        cyph = (randint(*r))
    
    
    code = caesar_shift(msg,cyph)#shifting the input string

    bini = words_to_binary(code)#converting string to binary
    rev = bini#reversing the binary string ex; 1101 -> 1011

    #turning the binary code, 1's and 0's, into different numbers, ex; 0 -> 8 and 10 -> 6
    str_oz = rev.replace('10', '6')
    str_zo = str_oz.replace('01', '3')
    str_z = str_zo.replace('0', '8')
    str_o = str_z.replace('1', '5')

    #obfuscating shift key using cyph dictionary
    hex = (cyph_dict[str(cyph)])#naming the dict output
    a, b = hex .split("|") #taking the obfuscated shift key and splitting it.

    #returning encrypted text with shift key
    return(a+"803530469412604911808100016627350902841903252146334827830598824925070206392756473556897071488234491921035262827731623431560143636674392911547862129480499413206061773770"+str_o[::-1]+"461727898511311493781391003693170643095981910343837368617180798950478072212496727634555268790775278503009288235497443181814221294871722010234444103771486479025802027848"+b)#returning the encoded message with the re-mapped shift code


#start of encoding
def decode(msg):

    #taking input 'msg' and splitting it at the split codes
    a, b = msg .split("803530469412604911808100016627350902841903252146334827830598824925070206392756473556897071488234491921035262827731623431560143636674392911547862129480499413206061773770")#one line input for both the code and shift ammount
    x, c = b .split("461727898511311493781391003693170643095981910343837368617180798950478072212496727634555268790775278503009288235497443181814221294871722010234444103771486479025802027848")#x is the actual message, c is the 2nd part of the shift code

    #converting the obfuscated shift code back into its corresponding shift amount and ensuring that it is an integer
    h = next(key for key, value in cyph_dict.items() if value == a+'|'+c)
    int_h = int(h)

    fwrd = x[::-1]#reversing the binary string in correct order ex; 1011 -> 1101

    #replacing the numbers of the encoded message back into Binary, 1's and 0's
    str_o = fwrd.replace('5', '1')
    str_z = str_o.replace('8', '0')
    str_zo = str_z.replace('3', '01')
    str_oz = str_zo.replace('6', '10')

    str_data = binary_to_words(str_oz) #converting binary back into text
    decode = caesar_shift_decrypt(str_data,int_h)#shifting the alphabet back into their original position
	
    #returning the original message
    return(decode) 






#RCCG-V4.01A 22/08/2024 Created by; Artus aka. AlmondMan