import tkinter as tk


m = tk.Tk()
m.title("Recipe Calculator")

def retrieve_input():
    inputValue=textbox3.get("1.0","end-1c")
    return(inputValue)

test = retrieve_input()
print(test)

#Recipe Info
label2 = tk.Label(m, text = "Recipe name: ")
label2.pack()
textbox3 = tk.Text(m, width= 25, height = 1)
textbox3.pack()

#Ingredient Info
label = tk.Label(m, text = "Ingredient Name: ")
label.pack()
textbox = tk.Text(m, width= 25, height = 1)
textbox.pack()

label4 = tk.Label(m, text = "Ingredient Weight: ")
label4.pack()
textbox4 = tk.Text(m, width= 25, height = 1)
textbox4.pack()

label5 = tk.Label(m, text = "Ingredient Calories: ")
label5.pack()
textbox5 = tk.Text(m, width= 25, height = 1)
textbox5.pack()

button5 = tk.Button(m, text = "Add Ingredient", width = 25)
button5.pack()
button3 = tk.Button(m, text = "Add Recipe", width = 25, command=lambda: retrieve_input())
button3.pack()

#Display Ingredient
label2 = tk.Label(m, text = "Recipe Info: ")
label2.pack()
textbox2 = tk.Text(m, width= 45, height = 15)
textbox2.pack()

#close application
button1 = tk.Button(m, text = "close", width = 25, command = m.destroy)
button1.pack()



m.mainloop()

