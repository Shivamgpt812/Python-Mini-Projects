from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Blue')

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg="Blue")
lab_txt.place(x=50, y=10, height=50, width=400)

lab_src_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg="blue")
lab_src_txt.place(x=10, y=70, height=20, width=200)

Sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD, bg="lightgray")
Sor_txt.place(x=10, y=100, height=150, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=260, height=40, width=200)
comb_sor.set("English")

button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=220, y=260, height=40, width=100)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=330, y=260, height=40, width=200)
comb_dest.set("Hindi")

lab_dest_txt = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), bg="blue")
lab_dest_txt.place(x=10, y=310, height=20, width=200)

dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD, bg="lightgray")
dest_txt.place(x=10, y=340, height=150, width=480)

root.mainloop()
