import RCCG
import tkinter as tk
from tkinter import filedialog


#fuck comments

#create a variable to know status of input
invalid = True

#input validation for encoding or decoding, prompting input gain if the user input is invalid
while invalid:

    mode = input("Would you like to ENCODE or DECODE? ") #printing/asking if the user wants to encode or decode text

    if not mode in ['encode', 'ENCODE', 'e', 'E', 'Encode', 'decode', 'DECODE', 'd', 'D', 'Decode']: #if the input doesn't match any valid option then we reprompt
        
        print('Invalid input')

    else:

        if mode in ['encode', 'ENCODE', 'e', 'E', 'Encode']:
            invalid = False
            q = True


            msg = input("Your Message: ")

            encoded = RCCG.encode(msg)

            print(encoded)


            while q:

                file = input("Would you like to save to a file? y/n: ")
                
                if not file in ['y', 'n']:
                    print('Invalid input')
                
                if file == 'y':
                    q = False


                    with open('RCCG-output.txt', 'w') as f:
                        f.write(encoded)
                        print("saved to 'RCCG-output.txt'")
                
                elif file == 'n':
                    q = False
            


        elif mode in ['decode', 'DECODE', 'd', 'D', 'Decode']:
            invalid = False
            q = True


            while q:

                file = input("Would you like to decode from file or paste the encoded message? (f)ile/(p)aste? ")

                if not file in ['f', 'p']:
                    print('invalid input')
                    

                if file == "f":
                    q = False
                    
                    root = tk.Tk()
                    root.withdraw()

                    filename = filedialog.askopenfilename(parent=root,title='Open file to encrypt')
                    contents = open(filename, 'r').read()

                    msg = contents

                    print("Decoded message: " + RCCG.decode(msg))
                    

                elif file == 'p':
                    q = False

                    msg = input("Coded Message: ")

                    print("Decoded message: " + RCCG.decode(msg))


        input("press any key to finish: ") #used to kill the process only when the user wants it to end instead of it automatically stopping
                                            #once the output has been printed   