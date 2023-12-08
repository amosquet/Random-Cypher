import tkinter as tk
from tkinter import END, Toplevel, filedialog
import RCCG



def encode():
    
    textboxOut.delete("1.0", END)

    
    inp = textboxIn.get(1.0, "end-1c")

    contents = RCCG.encode(inp)
    
    textboxOut.insert("1.0", contents)

def decode():
   
    textboxOut.delete("1.0", END)


    inp = textboxIn.get(1.0, "end-1c")

    contents = RCCG.decode(inp)
   
    textboxOut.insert("1.0", contents)

def open_file():

  textboxIn.delete("1.0", END)


  file_dialog = filedialog.askopenfilename(parent = root, title='Open file to encrypt')

  contents = open(file_dialog, 'r').read()

  textboxIn.insert("1.0", contents)

def save_file():
   
    inp = textboxOut.get(1.0, "end-1c")

    with open('output.txt', 'w') as f:
      f.write(inp)

def clear():
   
   textboxIn.delete("1.0", END)
   textboxOut.delete("1.0", END)


# def open_popup():

#   popup = Toplevel(root)
#   popup.title("Release Information")
#   popup.geometry('500x75')
#   popup.wm_attributes('-topmost', True)

#   label = tk.Label(popup, text = "This is an alpha build, functions may not work as intended.")
#   label.pack()

#   kill = tk.Button(popup, text = "Ok")
#   kill.pack()
#   kill.config(width = 10, height = 2)
#   kill.bind("<Button-1>", lambda event: popup.destroy())




root = tk.Tk()
root.geometry("800x450")
root.title("RCCG GUI")


label = tk.Label(root, text = "Random Caesar Cypher Generator", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

textboxIn = tk.Text(root, height = 3, font = ('Arial', 16))
textboxIn.pack(padx = 125, pady = 10)

encodeButton = tk.Button(root, text = "Encode", command = encode)
encodeButton.place(x = 125, y = 200)
encodeButton.config(width = 10, height = 2)

decodeButton = tk.Button(root, text = "Decode", command = decode)
decodeButton.place(x = 230, y = 200)
decodeButton.config(width = 10, height = 2)

openButton = tk.Button(root, text = "Open File", command = open_file)
openButton.place(x = 500, y = 200)
openButton.config(width = 10, height = 2)

saveButton = tk.Button(root, text = "Save to File", command = save_file)
saveButton.place(x = 595, y = 200)
saveButton.config(width = 10, height = 2)

textboxOut = tk.Text(root, height = 3, font = ('Arial', 16))
textboxOut.pack(padx = 125, pady = 110)

clearButton = tk.Button(root, text = "Clear", command = clear)
clearButton.place(x = 365, y = 200)
clearButton.config(width = 10, height = 2)

open_popup()

root.mainloop()
