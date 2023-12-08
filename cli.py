import RCCG
import tkinter as tk
from tkinter import filedialog


invalid = True

while invalid:

    mode = input("Would you like to ENCODE or DECODE? ")

    if not mode in ['encode', 'ENCODE', 'e', 'E', 'Encode', 'decode', 'DECODE', 'd', 'D', 'Decode']:
        
        print('Invalid input')

    else:
        if mode in ['encode', 'ENCODE', 'e', 'E', 'Encode']:

            invalid = False


            msg = input("Your Message: ")

            encoded = RCCG.encode(msg)

            print(encoded)

            file = input("Would you like to save to a file? y/n: ")
            
            if file == 'y':
                with open('RCCG-output.txt', 'w') as f:
                    f.write(encoded)
                    print("saved to 'output.txt'")
            


        elif mode in ['decode', 'DECODE', 'd', 'D', 'Decode']:

            invalid = False


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



        