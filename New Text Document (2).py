from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import cv2

window=Tk()
window.geometry("600x600")
window.title("Welcome")

label1 =Label(window,text="RGB Image to Gray Scale Image",fg="Black",bg="White",relief="solid",font=("arial",16,"bold"))
label1.pack()


def browser():
    x = filedialog.askopenfilename()
    print(x)


def second_win():
    print("Inserting picture")
    window=Tk()
    window.title("Browser")
    window.geometry("300x300")
    label_2=Label(window,text='Inserting image',relief="solid",font=('new time roman',16,'bold')).place(x=30,y=70)
    button4 = Button(window, text="InsertingImage", fg="black", bg="White", relief="solid", font=("arial", 20, "bold"),command=browser)
    button4.place(x=0, y=110)


def app():
    image = cv2.imread(browser(x))

    cv2.imshow('Original', image)

    cv2.waitKey()

    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("newphoto", gray_img)
    cv2.imshow("grayscale", gray_img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


def printt():
    print("Converting")


def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("Welcome to RGB IMAGE TO GRAY SCALE IMAGE SOFTWARE", "Hey here we use Opencv Library")

imge=Image.open('C:/Users/Hussaini/Desktop/rgb to grayscale-011.jpg')
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo,width=300,height=77)
lab.pack()

menu=Menu(window)
window.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=exit1)

subm2=Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=abt)




button1=Button(window,text="Gerenate",fg="black",bg="White",relief="solid",font=("arial",20,"bold"),command=app)
button1.place(x=0,y=210)


button2=Button(window,text="Cancel",width=20,command=exit1)
button2.place(x=0,y=410)


button3=Button(window,text="Browers",fg="black",bg="White",relief="solid",font=("arial",20,"bold"),command=second_win)
button3.place(x=0,y=110)




window.mainloop()