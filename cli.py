import RCCG
import updater
import yaml
import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
import updater as up


#import owner, repo, RCCG, and CLI from config.yaml
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

#grab variables from the config file
config = load_config('config.yaml')
repow = config['owner']+'/'+config['repo']
Vrccg = config['RCCG']
Vcli = config ['CLI']
file = config['update_folder']
ufolder = file

#check if RCCG and cli are up-to-date
rc_check = updater.check(Vrccg, repow) #false = latest version
cli_check = updater.check(Vcli, repow)

# config['RCCG_status'] = rc_check
# config['CLI_status'] = cli_check

#force to string because it doesn't like bools for some reason
# rc_check = str(rc_check)
# cli_check = str(cli_check)

# #just for debugging
# print(rc_check)
# print(cli_check)

# #if the cli or RCCG is out-of-date, call the updater script
# if rc_check or cli_check == True:
#     args = [rc_check, cli_check, "False"] #status arguments, "False" is a place holder for the gui since we don't check for its version here.
#     subprocess.run(["python", "updater.py"] + args) #run the updater script
#     sys.exit() #exit the program

if rc_check or cli_check == True:

    f1 = 'RCCG.py'
    f2 = 'cli.py'

    # ufolder = config['update_folder']
    up.create_dir(ufolder)
    up.clone(repow, ufolder)

    if rc_check == True:
        print("Updating "+f1)
        up.cleanup(f1, ufolder)
    if cli_check == True:
        print("Updating "+f2)
        up.cleanup(f2, ufolder)

    subprocess.run(['python', 'cli.py'])
    sys.exit() #exit the program


# with open('config.yaml', 'w') as file:
#     yaml.safe_dump(config, file)
#     print('save complete')




#create a variable to know status of input
invalid = True

#input validation for encoding or decoding, prompting input gain if the user input is invalid
while invalid:

    mode = input("Would you like to ENCODE or DECODE? ") #printing/asking if the user wants to encode or decode text

    if not mode in ['encode', 'ENCODE', 'e', 'E', 'Encode', 'decode', 'DECODE', 'd', 'D', 'Decode']: #if the input doesn't match any valid option then we reprompt
        
        print('Invalid input')

    else:
        #if encode is true then the "invalid" variable get changed to False, text input is requested, and RCCG is called to encode the text
        if mode in ['encode', 'ENCODE', 'e', 'E', 'Encode']:
            invalid = False
            q = True


            msg = input("Your Message: ")

            encoded = RCCG.encode(msg)

            print(encoded)


            while q:
                #input validation for saving to a text file
                file = input("Would you like to save to a file? y/n: ")
                
                if not file in ['y', 'n']:
                    print('Invalid input')
                
                if file == 'y':
                    q = False

                    #saving to text file
                    with open('RCCG-output.txt', 'w') as f:
                        f.write(encoded)
                        print("saved to 'RCCG-output.txt'")
                
                elif file == 'n':
                    q = False
            

        #if encode is true then the "invalid" variable get changed to False, text input is requested, and RCCG is called to encode the text
        elif mode in ['decode', 'DECODE', 'd', 'D', 'Decode']:
            invalid = False
            q = True


            while q:
                #asking the user if they would like to import encoded text from a text file or if they want to manualy type or paste it in
                file = input("Would you like to decode from file or paste the encoded message? (f)ile/(p)aste? ")

                if not file in ['f', 'p']:
                    print('invalid input')
                    

                if file == "f":
                    q = False
                    
                    #create a file dialogue box for the user to import a a text file
                    root = tk.Tk()
                    root.withdraw()

                    filename = filedialog.askopenfilename(parent=root,title='Open file to encrypt') #opening the text file
                    contents = open(filename, 'r').read() #storing the contents of the text file

                    msg = contents #storing the contents of the text file to the "msg" variable

                    print("Decoded message: " + RCCG.decode(msg)) #dedcoding and printing the decrypted text
                    
                #used only if manual importing, through typing or pasting, is selected
                elif file == 'p':
                    q = False

                    msg = input("Coded Message: ")

                    print("Decoded message: " + RCCG.decode(msg)) #dedcoding and printing the decrypted text


        input("press any key to finish: ") #used to kill the process only when the user wants it to end instead of it automatically stopping
                                            #once the output has been printed   
