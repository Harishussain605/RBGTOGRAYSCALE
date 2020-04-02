from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2

window = Tk()
window.geometry("800x800")
window.title("Welcome")
# label1 = Label(window, text="RGB Image to Gray Scale Image", fg="Black", bg="White", relief="solid",
#                font=("arial", 16, "bold"))
# label1.pack()
bg_image = Image.open("G:/programming languages works/New folder/project python/Ai_FINAL.png")
img = bg_image.resize((800, 800), Image.ANTIALIAS) ## The (250, 250) is (height, width)
pic = ImageTk.PhotoImage(img)
background_label = Label(window, image=pic)
#background_label.photo=bg_image
background_label.place(x=0, y=0)
# imge = Image.open('rgb to grayscale-011.jpg')
# photo = ImageTk.PhotoImage(imge)
# lab = Label(image=photo, width=300, height=77)
# lab.pack()

#lbl1 = Frame(window, bg='SlateGray3', width=1500, height=1500)
#lbl1.pack(side=LEFT, padx=3)


x = None
def browser():
    global x
    x = filedialog.askopenfilename()


# def second_win():
#     print("Inserting picture")
#     window = Tk()
#     window.title("Browser")
#     window.geometry("300x300")
#     # label_2 = Label(window, text='Inserting image', relief="solid", font=('new time roman', 16, 'bold')).place(x=30,y=70)
#     button4 = Button(window, text="InsertingImage", fg="black", bg="White", relief="solid", font=("arial", 20, "bold"),command=browser)
#     button4.place(x=0, y=110)


def app():
    global x
    if x is not None:
        print(x)

        #image = cv2.imread(x)
        #cv2.imshow('Original', image)

        cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
        image = cv2.imread(x)                        # Read image
        imS = cv2.resize(image, (800, 900))                    # Resize image
        cv2.imshow("output", imS)                            # Show image
        #cv2.waitKey(0) 

        cv2.waitKey()
        print("Converting")
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        im=cv2.resize(gray_img, (600, 600))
        cv2.imwrite('newimage.png',gray_img)
        cv2.imshow("grayscale", im)
        cv2.waitKey(0)

        cv2.destroyAllWindows()


def printt():
    print("Converting")


def exit1():
    exit()


def abt():
    tkinter.messagebox.showinfo("Welcome to RGB IMAGE TO GRAY SCALE IMAGE SOFTWARE", "Hey here we use Opencv Library")



# button_bg_color1='#000000'
# button_bg_color2='#000000'
# button_bg_color3='#000000'
menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exit1)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)

gen = PhotoImage(file="GENBUTTON.gif")
button1 = Button(window, image=gen,borderwidth=0,bg="grey",command=app)
button1.place(x=123, y=340)

cancel = PhotoImage(file="CNL_BUTTON.gif")
button2 = Button(window,  image=cancel,borderwidth=0,bg="grey", command=window.destroy)
button2.place(x=123, y=475)

upload = PhotoImage(file="G:/programming languages works/New folder/project python/Upload_Button.gif")
button3 = Button(window, image=upload,borderwidth=0,bg="grey",command=browser)

# button3=Button(window, text = 'upload !', image =upload, command='browser' )
button3.place(x=123, y=210)

window.mainloop()
