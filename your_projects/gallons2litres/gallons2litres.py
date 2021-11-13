from tkinter import *

def mcal():
	var2 = var1.get()

        #here you can change the operation or the mathematical process
	var3 = var2 * 3.785

	entry2.insert(0, var3)

root = Tk()
root.title("Yanis's Converter")
var1 = IntVar()
label_font = "arial",14,"bold"
Label(root,text = "Gallons", padx = 25, font=(label_font)).grid(row=0,sticky=W)
entry1 = Entry(root, width=25 , textvariable=var1)
entry1.grid(row=0,column=1)
Label(root,text="Litres", padx=25, font=(label_font)).grid(row=1,sticky=W)
entry2 = Entry(root, width=25)
entry2.grid(row=1,column=1)
Button(root,text="calculate", font=(label_font), command = mcal).grid(row=2,column=1)

root.mainloop()