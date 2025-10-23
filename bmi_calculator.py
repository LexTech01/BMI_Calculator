import tkinter as tk
from PIL import Image , ImageTk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x600")
name = root.title("BMI CALCULATOR")
root.resizable(False, False)
root.config(bg="#f0f1f5")

#Icon
img_icon =ImageTk.PhotoImage(file ="images/bmilogo.png")
root.iconphoto(False,img_icon)

#top image

img = Image.open("images/background.jpeg")
img = img.resize((548, 100))
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo,bg="#f0f1f5")
label.place(x=-10,y=-10)


#box
img1 = Image.open("images/box.png")
photo1 = ImageTk.PhotoImage(img1)
label = tk.Label(root, image=photo1)
label.place(x=20,y=100)

img_box2 = Image.open("images/box.png")
photo2 = ImageTk.PhotoImage(img_box2)
tk.Label(root, image=photo2).place(x=250,y=100)

#EntryBox
Height=tk.StringVar()
Weight=tk.StringVar()
height=tk.Entry(textvariable=Height,width=5,font="arial 50",bg="white",fg="black",bd=0,justify="center")
height.place(x=40,y=160)
#Height.set(get_current_value())

weight=tk.Entry(textvariable=Weight,width=5,font="arial 50",bg="white",fg="black",bd=0,justify="center")
weight.place(x=262,y=160)
#Weight.set(get_current_value2())


#bottom section
bottom = tk.Label(root, width= 90,height=19,bg="#EEBF25")
bottom.pack(side="bottom")


#Scale
img_scale = Image.open("images/scale.png")
scale = ImageTk.PhotoImage(img_scale)
tk.Label(root, image=scale,bg="#EEBF25").place(x=20,y=320)



##############Slider##############
current_value =tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_change(event):
    Height.set(get_current_value())

    #Person Image

    size=int(float(get_current_value()))
    img_man = (Image.open("images/man_standing2.png"))
    resized_img =img_man.resize((45,30+size))
    man= ImageTk.PhotoImage(resized_img)
    sec_img.config(image=man, bg='#EEBF25')
    sec_img.place(x=65, y=542-size)
    sec_img.image=man



style =ttk.Style()
style.configure('TScale')

slider = ttk.Scale(root,from_=0, to=220,orient='horizontal',style="TScale",command=slider_change,variable=current_value)
slider.place(x=80,y=240)

sec_img = tk.Label(root)
sec_img.place(x=70,y=530)


#BMI calculation
def BMI():
    h=float(Height.get())
    w=float(weight.get())

    #converting height to mater
    m=h/100
    bmi=round(w/m**2,1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="UNDER\nWEIGHT")
        label3.config(text="You’re below\nthe healthy weight\n range. Try adding more\n nutritious meals\nand stay consistent\nyour health matters!")

    elif bmi>=18.5 and bmi<=24.9:
        label2.config(text="NORMAL\nWEIGHT")
        label3.config(text="Great job!\nYou’re in a\nhealthy weight range.\nKeep up your balanced\n diet and active lifestyle!")

    elif bmi>=25 and bmi<=29.9:
        label2.config(text="OVERWEIGHT")
        label3.config(text="You’re slightly\n above the healthy range.\n A bit more physical \nactivity and mindful eating\n can make a\nbig difference!")
    
    else:
        label2.config(text="OBESE")
        label3.config(text="Your BMI is higher\n than normal.\nConsider consulting \na healthcare professional\nand adopting small,\n steady lifestyle \nchange")

##################################




##@@@@@@@@@@@@@@Slider2@@@@@@@@@@@@@@


current_value2 =tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_change2(event):
    Weight.set(get_current_value2())

style2 =ttk.Style()
style2.configure('TScale')

slider2 = ttk.Scale(root,from_=0, to=200,orient='horizontal',style="TScale",command=slider_change2,variable=current_value2)
slider2.place(x=300,y=240)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


tk.Button(root,text="Health Report",font="arial 11 bold",bg="#0073EE",fg="#000000",command=BMI).place(x=200,y=300)



img4 = Image.open("images/bmi_result.png")
newimg=img4.resize((320,97))
result = ImageTk.PhotoImage(newimg)
label = tk.Label(root, image=result,bg='#EEBF25')
label.place(x=170,y=485)

label1=tk.Label(root,font="arial 40 bold",bg="#E9C200",fg="#E5E1E1",width="6")
label1.place(x=100,y=340)

label2=tk.Label(root,font="arial 25 bold",bg="#EEBF25",fg="#000000",justify="left")
label2.place(x=130,y=415)

label3=tk.Label(root,font="arial 11 bold",bg="#EEBF25",fg="#000000",justify="center",height="7")
label3.place(x=310,y=350)



root.mainloop()