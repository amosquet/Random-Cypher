import tkinter as tk
from tkinter import END, Toplevel, filedialog
import RCCG

#note: All functions with 'def' are only ran when the corresponding button has been clicked

#takes whatever is in the input text box and sends it to RCCG to be encoded then outputs it in the output textbox
def encode():
    
    textboxOut.delete("1.0", END) #clearing the input textbox

    
    inp = textboxIn.get(1.0, "end-1c")

    contents = RCCG.encode(inp)
    
    textboxOut.insert("1.0", contents)

#takes whatever is in the input textbox and sends it to RCCG to be decoded then outputs it in the output textbox
def decode():
   
    textboxOut.delete("1.0", END) #clearing the output textbox


    inp = textboxIn.get(1.0, "end-1c")

    contents = RCCG.decode(inp)
   
    textboxOut.insert("1.0", contents)

#creates popup window using file explorer specifically for importing a text file, the file contents will be stored in the input textbox
def open_file():

  textboxIn.delete("1.0", END)


  file_dialog = filedialog.askopenfilename(parent = root, title='Open file to encrypt')

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

  label = tk.Label(popup, text = "This is an alpha build, functions may not work as intended.")
  label.pack()

  kill = tk.Button(popup, text = "Ok")
  kill.pack()
  kill.config(width = 10, height = 2)
  kill.bind("<Button-1>", lambda event: popup.destroy())


  kill = tk.Button(popup, text = "Ok") #create a "kill" button that reads "Ok"  to kill the popup window
  kill.pack()
  kill.config(width = 10, height = 2)
  kill.bind("<Button-1>", lambda event: popup.destroy())



#create root window with title "RCCG GUI"
root = tk.Tk()
root.geometry("800x450") #define default launch box size
root.title("RCCG GUI") #might change title, idk maybe "RCCG"


#create a label, or text, with the name of the applcation 
label = tk.Label(root, text = "Random Caesar Cypher Generator", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

#create the input textbox
textboxIn = tk.Text(root, height = 3, font = ('Arial', 16))
textboxIn.pack(padx = 125, pady = 10)

#create encode button that calls to the 'encode' function
encodeButton = tk.Button(root, text = "Encode", command = encode)
encodeButton.place(x = 125, y = 200)
encodeButton.config(width = 10, height = 2)

#create decode button that calls to the 'decode' function
decodeButton = tk.Button(root, text = "Decode", command = decode)
decodeButton.place(x = 230, y = 200)
decodeButton.config(width = 10, height = 2)

#create open button that calls to the 'open_file' function
openButton = tk.Button(root, text = "Open File", command = open_file)
openButton.place(x = 500, y = 200)
openButton.config(width = 10, height = 2)

#create save button that calls to the 'save_file' function
saveButton = tk.Button(root, text = "Save to File", command = save_file)
saveButton.place(x = 595, y = 200)
saveButton.config(width = 10, height = 2)

#create the output textbox
textboxOut = tk.Text(root, height = 3, font = ('Arial', 16))
textboxOut.pack(padx = 125, pady = 110)

#create the clear button that calls to the 'clear' function
clearButton = tk.Button(root, text = "Clear", command = clear)
clearButton.place(x = 365, y = 200)
clearButton.config(width = 10, height = 2)

open_popup()

root.mainloop()
