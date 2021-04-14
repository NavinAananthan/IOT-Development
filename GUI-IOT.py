from tkinter import *
from tkinter.ttk import *
import tkinter
import cv2 

#**********************setting the gui window***************************#

window=tkinter.Tk()                     #setting up the window
window.title("Home IOT")                #adding title to the GUI window
window.geometry("500x500")              #giving size for the GUI window
window.configure(background="black")    #setting the background color
window.resizable(0,0)
#bg=PhotoImage(file="fire.jpg")

#*************************setting up the labels**************************#

label1=tkinter.Label(window,bg="black",foreground="white",text="IOT with Python",font=("DS-Digital",35,"bold"))      #label 1
label1.place(x=80,y=30)

label2=tkinter.Label(window,bg="black",foreground="white",text="Temperature: ",font=("DS-Digital",30,"bold"))        #label2
label2.place(x=5,y=130)

#label1.grid(row=0,column=0,pady=3)
#label1.place(anchor=NW)
#label1.place(anchor='nw')

label3=tkinter.Label(window,bg="black",foreground="white",text="Humidity: ",font=("DS-Digital",30,"bold"))           #label3
label3.place(x=10,y=200)

#label2.grid(row=3,column=0,pady=3)
#label2.place(relx = 1, x =1, y = 1, anchor = NW)
#label2.place(relx=1.0,rely=0.0,anchor='nw')
label4=tkinter.Label(window,bg="black",foreground="white",text="developed by navin",font=("DS-Digital",15,"bold"))   #label4
label4.place(x=300,y=460)     
#label1.pack()
#label2.pack()


# ************* setting the exit button ***************************#

exit_button=tkinter.Button(window,bg="black",foreground="white",borderwidth=.5,text="Exit",width=10,command=window.destroy)   #button
exit_button.config(font=("DS-Digital",15))
exit_button.place(x=200,y=350)

#exit_button.grid(row=10,column=4,pady=10)
#exit_button.pack()

#**************End of the program**********************************#

window.mainloop()               #running the window in a main loop