import tkinter as tk
from tkinter import END, Toplevel, filedialog
import RCCG

#note: All functions with 'def' are only ran when the corresponding button has been clicked

#takes whatever is in the input text box and sends it to RCCG to be encoded then outputs it in the output textbox
def encode():

    textboxOut.delete("1.0", END) #clearing the input textbox
    inp = textboxIn.get(1.0, "end-1c")
    contents = RCCG.encode(inp) #call the endcoding function
    textboxOut.insert("1.0", contents)

#takes whatever is in the input textbox and sends it to RCCG to be decoded then outputs it in the output textbox
def decode():

    textboxOut.delete("1.0", END)#clearing the output textbox
    inp = textboxIn.get(1.0, "end-1c").strip()
    contents = RCCG.decode(inp)#call the decoding function
    textboxOut.insert("1.0", contents)

#creates popup window using file explorer specifically for importing a text file, the file contents will be stored in the input textbox
def open_file():

    textboxIn.delete("1.0", END)
    file_dialog = filedialog.askopenfilename(parent=root, title='Open file to encrypt')
    contents = open(file_dialog, 'r').read()
    textboxIn.insert("1.0", contents)

#saves whatever text is currently in the output textbox to text file 'RCCG-output.txt'
def save_file():

    inp = textboxOut.get(1.0, "end-1c")
    with open('RCCG-output.txt', 'w') as f:
        f.write(inp)

#clears both the input and output textboxes
def clear():

    textboxIn.delete("1.0", END)
    textboxOut.delete("1.0", END)

#create popup window as a child of the main (or root) window to warn that the current build is an alpha 
def open_popup():

    popup = Toplevel(root)
    popup.title("Release Information")
    popup.geometry('500x75')
    popup.wm_attributes('-topmost', True)
    popup.transient(root) #make the popup stay on top of the main window
    popup.grab_set() #make the popup modal

    #calculate the position to center the popup
    root.update_idletasks()
    popup_width = 500
    popup_height = 75
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    popup_x = root_x + (root_width // 2) - (popup_width // 2)
    popup_y = root_y + (root_height // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{popup_x}+{popup_y}")

    label = tk.Label(popup, text="This is an alpha build, functions may not work as intended.")
    label.pack()
    kill = tk.Button(popup, text="Ok", command=popup.destroy) #create a "kill" button that reads "Ok"  to kill the popup window
    kill.pack()
    kill.config(width=10, height=2)

#create root window with title "RCCG GUI"
root = tk.Tk()
root.geometry("800x450") #define default launch box size
root.title("RCCG GUI") #might change title, idk maybe "RCCG"

#create a label, or text, with the name of the applcation 
label = tk.Label(root, text="Random Caesar Cypher Generator", font=('Arial', 18))
label.pack(padx=20, pady=20, expand=True, fill='both')

#create the input textbox
textboxIn = tk.Text(root, height=3, font=('Arial', 16))
textboxIn.pack(padx=125, pady=10, expand=True, fill='both')

button_frame = tk.Frame(root)
button_frame.pack(pady=10, expand=True, fill='both')

#create encode button that calls to the 'encode' function
encodeButton = tk.Button(button_frame, text="Encode", command=encode)
encodeButton.pack(side='left', padx=5, pady=5, expand=True, fill='both')

#create decode button that calls to the 'decode' function
decodeButton = tk.Button(button_frame, text="Decode", command=decode)
decodeButton.pack(side='left', padx=5, pady=5, expand=True, fill='both')

#create open button that calls to the 'open_file' function
openButton = tk.Button(button_frame, text="Open File", command=open_file)
openButton.pack(side='left', padx=5, pady=5, expand=True, fill='both')

#create save button that calls to the 'save_file' function
saveButton = tk.Button(button_frame, text="Save to File", command=save_file)
saveButton.pack(side='left', padx=5, pady=5, expand=True, fill='both')

#create the clear button that calls to the 'clear' function
clearButton = tk.Button(button_frame, text="Clear", command=clear)
clearButton.pack(side='left', padx=5, pady=5, expand=True, fill='both')

#create the output textbox
textboxOut = tk.Text(root, height=3, font=('Arial', 16))
textboxOut.pack(padx=125, pady=10, expand=True, fill='both')

open_popup()

root.mainloop()