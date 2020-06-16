import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from glob import glob
from tkinter.ttk import *

root=tk.Tk()
root.title("Login")

listbox=tk.Listbox(root)
label_login1=tk.Label(root, text=' Welcome to The Shopping Mart ')
label_login2=tk.Label(root, text='UserName')
label_login3=tk.Label(root, text='Password') 
e1 = Entry(root) 
e2 = Entry(root)        
total=0


def Checkout():
        r = tk.Tk() 
        r.title('Checkout')
        
        global listbox
        label1=tk.Label(r,text="Your Cart",width=50)
        listbox=tk.Listbox(r)
        
        button1 = tk.Button(r, text = "Delete", command = lambda listbox=listbox: listbox.delete(tk.ANCHOR))  
        label1.pack()
        listbox.pack()
        button1.pack()
        listbox.insert('end','Total = 0')
        button2 = tk.Button(r,text = "Grand Total",command=Grand_total)
        button2.pack()
        r.mainloop()

def end():
        r=tk.Tk()
        r.title("Thank You")
        messageVar = Message(r, text = "Thank You For Shopping with Us!") 
        messageVar.config(bg='lightyellow')
        button = tk.Button(r,text ="Exit",command=r.destroy)
        messageVar.pack()
        button.pack()

def Grand_total():
        r=Tk()
        label_1=tk.Label(r,text=("Your Grand Total :",total),width=50,bg='lightblue')
        
        label_1.pack()
        button3 = tk.Button(r,text ="Proceed",command=end)
        label_2=Label(r,text="Choose your Payment option",width=50)
        label_2.pack()
        v = IntVar() 
        Radiobutton(r, text='Cash', variable=v, value=1).pack(anchor=W) 
        Radiobutton(r, text='Card', variable=v, value=2).pack(anchor=W)
        button3.pack()


def Electronics():
        r = tk.Tk() 
        r.title('Electronics')
        button1 = tk.Button(r, text='Mobiles', width=25, command=mobile_variant)
        button2 = tk.Button(r, text='Laptops', width=25, command=laptop_variant)
        button3 = tk.Button(r, text='Cameras', width=25, command=camera_variant)
        button4 = tk.Button(r, text='Back', width=25, command=r.destroy) 
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        r.mainloop()

def mobile_variant():
 r=tk.Tk()
 r.title(" Mobile Variants")
 photo5=  tk.PhotoImage(file= r"C:\\Project\\IPhone 11 Pro.gif",master=r)
 photo6 = tk.PhotoImage(file= r"C:\\Project\\Realme 6.gif",master=r)
 photo7 = tk.PhotoImage(file= r"C:\\Project\\Lenovo Zuk.gif",master=r)
 photo8 = tk.PhotoImage(file= r"C:\\Project\\Asus Zenfone.gif",master=r)
 photo9 = tk.PhotoImage(file= r"C:\\Project\\OnePlus 7T.gif",master=r)
 foto5= photo5.subsample(20,20)
 foto6= photo6.subsample(3,3)
 foto7= photo7.subsample(10,10)
 foto8= photo8.subsample(10,10)
 foto9= photo9.subsample(3,3)
 button1 = tk.Button(r, text="IPhone 11 Pro ", image=foto5, compound=  LEFT,command=lambda:add("IPhone 11 Pro",70000))
 button2 = tk.Button(r, text="Realme 6 ", image=foto6, compound=  LEFT,command=lambda:add("Realme 6      ",12000))
 button3 = tk.Button(r, text="Lenovo Zuk", image=foto7, compound=  LEFT, command=lambda:add("Lenovo Zuk   ",8500))
 button4 = tk.Button(r, text="Asus Zenfone ", image=foto8, compound=  LEFT,command=lambda:add("Asus Zenfone ",10000))
 button5 = tk.Button(r, text="OnePlus 7T ", image=foto9, compound=  LEFT,command=lambda:add("OnePlus 7T   ",40000))
 button1.pack()
 button2.pack()
 button3.pack()
 button4.pack()
 button5.pack()
 r.mainloop()
def camera_variant():
 r=tk.Tk()
 r.title("Camera Variants")
 photo10 = tk.PhotoImage(file= r"C:\\Project\\Canon EOS.gif",master=r)
 photo11 = tk.PhotoImage(file= r"C:\\Project\\Sony Coolpix.gif",master=r)
 photo12 = tk.PhotoImage(file= r"C:\\Project\\Kodak Easyshare.gif",master=r)
 foto10= photo10.subsample(3,3)
 foto11= photo11.subsample(3,3)
 foto12= photo12.subsample(7,7)
 button1 = tk.Button(r, text="Canon EOS", image=foto10, compound=  LEFT,command=lambda:add("Canon EOS",12500))
 button2 = tk.Button(r, text="Sony Coolpix", image=foto11, compound=  LEFT,command=lambda:add("Sony Coolpix",8500))
 button3 = tk.Button(r, text="Kodak Easyshare", image=foto12, compound=  LEFT,command=lambda:add("Kodak Easyshare",7900))
 button1.pack()
 button2.pack()
 button3.pack()
 r.mainloop()

def laptop_variant():
 r=tk.Tk()
 r.title("Laptop Variants")
 photo13 = tk.PhotoImage(file= r"C:\\Project\\Lenovo Ideapad.gif",master=r)
 photo14 = tk.PhotoImage(file= r"C:\\Project\\HP Pavillion.gif",master=r)
 photo15 = tk.PhotoImage(file= r"C:\\Project\\Dell Inspiron.gif",master=r)
 foto13= photo13.subsample(6,6)
 foto14= photo14.subsample(3,3)
 foto15= photo15.subsample(20,20)
 button1 = tk.Button(r, text="Lenovo Ideapad", image=foto13, compound=  LEFT,command=lambda:add("Lenovo Ideapad",45000))
 button2 = tk.Button(r, text="HP Pavillion", image=foto14, compound=  LEFT,command=lambda:add("HP Pavillion",55000))
 button3 = tk.Button(r, text="Dell Inspiron", image=foto15, compound=  LEFT,command=lambda:add("Dell Inspiron",73000))
 button1.pack()
 button2.pack()
 button3.pack()
 r.mainloop()

def Fashion():
        r = tk.Tk() 
        r.title('Fashion')
        button1 = tk.Button(r, text='Men\'s', width=25, command=mens_clothes)
        button2 = tk.Button(r, text='Women\'s', width=25, command=womens_clothes)
        button3 = tk.Button(r, text='Kid\'s', width=25, command=kids_clothes) 
        button4 = tk.Button(r, text='Back', width=25, command=r.destroy)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        r.mainloop() 

def mens_clothes():
    r=tk.Tk()
    r.title("Mens wear")

    photo5 = tk.PhotoImage(file=r"C:\\Project\\Men Shirt.gif", master=r)
    photo6 = tk.PhotoImage(file=r"C:\\Project\\Men Tshirt.gif", master=r)
    photo7 = tk.PhotoImage(file=r"C:\\Project\\Men Jeans.gif", master=r)

    foto5 = photo5.subsample(6,6)
    foto6 = photo6.subsample(5,5)
    foto7 = photo7.subsample(2,2)

    tk.Button(r, text="Men Shirt", image=foto5, compound=LEFT, command=lambda: add("Men Shirt",700)).pack()
    tk.Button(r, text="Men Tshirt", image=foto6, compound=LEFT, command=lambda: add("Men Tshirt",800)).pack()
    tk.Button(r, text="Men Jeans", image=foto7, compound=LEFT, command=lambda: add("Men Jeans",800)).pack()

    r.mainloop()



       


def womens_clothes():
    r=tk.Tk()
    r.title("Womens wear")

    photo5 = tk.PhotoImage(file=r"C:\\Project\\Saree.gif", master=r)
    photo6 = tk.PhotoImage(file=r"C:\\Project\\Salwar.gif", master=r)
    photo7 = tk.PhotoImage(file=r"C:\\Project\\Churidar.gif", master=r)

    foto5 = photo5.subsample(10,10)
    foto6 = photo6.subsample(10,10)
    foto7 = photo7.subsample(12,12)

    tk.Button(r, text="Saree", image=foto5, compound=LEFT, command=lambda: add("Saree", 700)).pack()
    tk.Button(r, text="Salwar", image=foto6, compound=LEFT, command=lambda: add("Salwar", 800)).pack()
    tk.Button(r, text="Churidar", image=foto7, compound=LEFT, command=lambda: add("Churidar", 800)).pack()

    r.mainloop()




def kids_clothes():
    r=tk.Tk()
    r.title("kids wear")

    photo5 = tk.PhotoImage(file=r"C:\\Project\\Kid Shirt.gif", master=r)
    photo6 = tk.PhotoImage(file=r"C:\\Project\\Kid Tshirt.gif", master=r)
    photo7 = tk.PhotoImage(file=r"C:\\Project\\Kid Jeans.gif", master=r)

    foto5 = photo5.subsample(7,8)
    foto6 = photo6.subsample(2,2)
    foto7 = photo7.subsample(5,4)

    tk.Button(r, text="Kid Shirt", image=foto5, compound=LEFT, command=lambda: add("Kid Shirt", 700)).pack()
    tk.Button(r, text="Kid Tshirt", image=foto6, compound=LEFT, command=lambda: add("Kid Tshirt", 800)).pack()
    tk.Button(r, text="Kid Jeans", image=foto7, compound=LEFT, command=lambda: add("Kid Jeans", 800)).pack()

    r.mainloop()


       

def Groceries():
    r = tk.Tk()
    r.title('Groceries')
    photo5=  tk.PhotoImage(file= r"C:\\Project\\Onion.gif",master=r)
    photo6 = tk.PhotoImage(file= r"C:\\Project\\Potato.gif",master=r)
    photo7 = tk.PhotoImage(file= r"C:\\Project\\Cabbage.gif",master=r)
    photo8 = tk.PhotoImage(file= r"C:\\Project\\Poultry.gif",master=r)
    photo9 = tk.PhotoImage(file= r"C:\\Project\\Dairy.gif",master=r)

    foto5= photo5.subsample(8,10)
    foto6= photo6.subsample(4,4)
    foto7= photo7.subsample(10,10)
    foto8= photo8.subsample(3,3)
    foto9= photo9.subsample(12,12)

    tk.Button(r, text="Onion ", image=foto5, compound=  LEFT,command=lambda:add("Onion",30)).pack()
    tk.Button(r, text="Potatoe ", image=foto6, compound=  LEFT,command=lambda:add("Potatoe      ",20)).pack()
    tk.Button(r, text="Cabbage", image=foto7, compound=  LEFT, command=lambda:add("Cabbage   ",15)).pack()
    tk.Button(r, text="Poultry ", image=foto8, compound=  LEFT,command=lambda:add("Poultry ",30)).pack()
    tk.Button(r, text="Dairy ", image=foto9, compound=  LEFT,command=lambda:add("Dairy   ",15)).pack()

    r.mainloop()
        
def Others():
        r = tk.Tk() 
        r.title('Others')
        button1 = tk.Button(r, text='Music', width=25, command=musical_instruments)
        button2 = tk.Button(r, text='Books', width=25, command=books)
        button3 = tk.Button(r, text='Health Care', width=25, command=Health_care) 
        button4 = tk.Button(r, text='Back', width=25, command=r.destroy)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        r.mainloop()
def musical_instruments():
    r=tk.Tk()

    photo5 = tk.PhotoImage(file=r"C:\\Project\\Guitar.gif", master=r)
    photo6 = tk.PhotoImage(file=r"C:\\Project\\Violin.gif", master=r)

    foto5 = photo5.subsample(6,6)
    foto6 = photo6.subsample(4,4)

    tk.Button(r,text="Guitar", image=foto5,compound=LEFT, command=lambda: add("Guitar",7500)).pack()
    tk.Button(r,text="Violin", image=foto6,compound=LEFT, command=lambda: add("Violin",1500)).pack()

    r.mainloop()

        
def books():
    r=tk.Tk()

    photo5 = tk.PhotoImage(file=r"C:\\Project\\Story Book.gif", master=r)
    photo6 = tk.PhotoImage(file=r"C:\\Project\\Reference Book.gif", master=r)

    foto5 = photo5.subsample(4,4)
    foto6 = photo6.subsample(5,3)

    tk.Button(r, text="Story Book", image=foto5, compound=LEFT, command=lambda: add("Story Book",500)).pack()
    tk.Button(r, text="Reference Book", image=foto6, compound=LEFT, command=lambda: add("Reference Book",700)).pack()

    r.mainloop()



def Health_care():
    r=tk.Tk()

    photo5 = tk.PhotoImage(file=r"C:\\Project\\Medicine.gif", master=r)
    photo6 = tk.PhotoImage(file=r"C:\\Project\\Household Cleaner.gif", master=r)

    foto5 = photo5.subsample(6,6)
    foto6 = photo6.subsample(7,5)

    tk.Button(r, text="Medicine", image=foto5, compound=LEFT, command=lambda: add("Medicine",800)).pack()
    tk.Button(r, text="Household Cleaner", image=foto6, compound=LEFT, command=lambda: add("Household Cleaner",
                                                                                           200)).pack()

    r.mainloop()







  

def add(item,cost):
        global total
        total+=cost
        listbox.delete('end')
        listbox.insert('end',(item,cost))
        listbox.insert('end',('Total = ', total))


def screen():
        r = tk.Tk() 
        r.title('MainScreen')
        label1=tk.Label(r,text="Shopping Cart",width=50)
        photo1 = tk.PhotoImage(file= r"C:\\Project\\Electronics.gif",master=r)
        photo2 = tk.PhotoImage(file= r"C:\\Project\\Fashion.gif",master=r)
        photo3 = tk.PhotoImage(file= r"C:\\Project\\Groceries.gif",master=r)
        photo4 = tk.PhotoImage(file= r"C:\\Project\\Others.gif",master=r)
        foto1= photo1.subsample(28,25)
        foto2= photo2.subsample(3,3)
        foto3= photo3.subsample(3,3)
        foto4= photo4.subsample(15,25)
       
        b1 = tk.Button(r, text="Electronics", image=foto1, compound=  LEFT, command= Electronics)
        b2 = tk.Button(r, text="Fashion      ", image= foto2, compound=  LEFT, command= Fashion)
        b3 = tk.Button(r, text="Groceries  ", image= foto3, compound=  LEFT, command = Groceries)
        b4 = tk.Button(r, text="Others       ", image= foto4, compound=  LEFT, command= Others)
        b5=tk.Button(r,text="Checkout",command=Checkout)
        b6=tk.Button(r,text="Exit",command=r.destroy)
        label1.pack()
       
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
        b6.pack()
        r.mainloop()


button_login=tk.Button(root,text="Login",command=screen)
label_login1.pack()
label_login2.pack()
e1.pack()
label_login3.pack()
e2.pack()
button_login.pack()



mainloop()
