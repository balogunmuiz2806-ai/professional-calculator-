# Professional Calculator Lessons 31-35
import tkinter as tk
import math

window = tk.Tk()
window.title("Professional Calculator")
window.geometry("500x600")
window.resizable(False, False)

history=[]

tk.Label(window,text="Professional Calculator",font=("Arial",16,"bold")).pack(pady=10)
tk.Label(window,text="First Number").pack()
entry1=tk.Entry(window,font=("Arial",12),width=25)
entry1.pack()

tk.Label(window,text="Second Number").pack(pady=(10,0))
entry2=tk.Entry(window,font=("Arial",12),width=25)
entry2.pack()

result=tk.Label(window,text="Answer:",font=("Arial",12,"bold"))
result.pack(pady=10)

tk.Label(window,text="History",font=("Arial",12,"bold")).pack()
history_box=tk.Listbox(window,width=55,height=8)
history_box.pack()

def save_history(calc):
    history.append(calc)
    history_box.insert(tk.END,calc)

def get_numbers():
    try:
        return float(entry1.get()), float(entry2.get())
    except ValueError:
        result.config(text="Please enter valid numbers.")
        return None

def add():
    n=get_numbers()
    if n:
        a,b=n; ans=a+b
        result.config(text=f"Answer: {ans}")
        save_history(f"{a} + {b} = {ans}")

def subtract():
    n=get_numbers()
    if n:
        a,b=n; ans=a-b
        result.config(text=f"Answer: {ans}")
        save_history(f"{a} - {b} = {ans}")

def multiply():
    n=get_numbers()
    if n:
        a,b=n; ans=a*b
        result.config(text=f"Answer: {ans}")
        save_history(f"{a} × {b} = {ans}")

def divide():
    n=get_numbers()
    if n:
        a,b=n
        if b==0:
            result.config(text="Cannot divide by zero.")
        else:
            ans=a/b
            result.config(text=f"Answer: {ans}")
            save_history(f"{a} ÷ {b} = {ans}")

def modulus():
    n=get_numbers()
    if n:
        a,b=n; ans=a%b
        result.config(text=f"Answer: {ans}")
        save_history(f"{a} % {b} = {ans}")

def power():
    n=get_numbers()
    if n:
        a,b=n; ans=a**b
        result.config(text=f"Answer: {ans}")
        save_history(f"{a}^{b} = {ans}")

def square():
    try:
        a=float(entry1.get()); ans=a**2
        result.config(text=f"Answer: {ans}")
        save_history(f"{a}² = {ans}")
    except ValueError:
        result.config(text="Please enter a valid number.")

def square_root():
    try:
        a=float(entry1.get())
        if a<0:
            result.config(text="Cannot calculate square root of a negative number.")
        else:
            ans=math.sqrt(a)
            result.config(text=f"Answer: {ans}")
            save_history(f"√{a} = {ans}")
    except ValueError:
        result.config(text="Please enter a valid number.")

def clear():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    result.config(text="Answer:")
    entry1.focus()

def clear_history():
    history.clear()
    history_box.delete(0,tk.END)

frame=tk.Frame(window)
frame.pack(pady=10)

buttons=[
("+",add,0,0),("-",subtract,0,1),("×",multiply,0,2),
("÷",divide,1,0),("%",modulus,1,1),("xʸ",power,1,2),
("x²",square,2,0),("√",square_root,2,1),("Clear",clear,2,2)
]
for text,cmd,r,c in buttons:
    tk.Button(frame,text=text,width=8,height=2,command=cmd).grid(row=r,column=c,padx=5,pady=5)

tk.Button(window,text="Clear History",width=28,height=2,command=clear_history).pack(pady=5)
tk.Button(window,text="Exit",width=28,height=2,bg="red",fg="white",command=window.destroy).pack(pady=5)

window.mainloop()
