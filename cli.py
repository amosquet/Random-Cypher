import RCCG
import tkinter as tk
from tkinter import filedialog


mode = input("Would you like to ENCODE or DECODE? ")

if mode == 'encode' or mode == 'ENCODE' or mode == 'e' or mode == "E" or mode == "Encode":

    msg = input("Your Message: ")

    encoded = RCCG.encode(msg)

    print(encoded)

    file = input("Would you like to save to a file? (Y)yes/(N)no: ")
    
    if file == 'Y':
        with open('RCCG-output.txt', 'w') as f:
            f.write(encoded)
            print("saved to 'output.txt'")
    


elif mode == 'decode' or mode == "DECODE" or mode == 'd' or mode == 'D' or mode == "Decode":

    file = input("Would you like to decode from file or copy the encoded file? file/copy? ")

    if file == "file":
        
        root = tk.Tk()
        root.withdraw()

        filename = filedialog.askopenfilename(parent=root,title='Open file to encrypt')
        contents = open(filename, 'r').read()

        msg = contents
        

    else:

        msg = input("Coded Message: ")


    decoded = RCCG.decode(msg)

    print(decoded)


input("press any key to finish: ")

        