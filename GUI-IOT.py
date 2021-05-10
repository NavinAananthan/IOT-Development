from Tkinter import *
from ttk import *
import Tkinter
import seeed_dht
import time

#**********************setting the gui window***************************#
window=Tkinter.Tk()                     #setting up the window
window.title("Home IOT")                #adding title to the GUI window
window.geometry("500x500")              #giving size for the GUI window
window.configure(background="black")    #setting the background color
window.resizable(0,0)
#bg=PhotoImage(file="fire.jpg")

#*************************setting up the labels**************************#

label1=Tkinter.Label(window,bg="black",foreground="white",text="IOT with Python",font=("DS-Digital",40,"bold"))      #label 1
label1.place(x=80,y=50)

label2=Tkinter.Label(window,bg="black",foreground="white",text="Temperature: ",font=("DS-Digital",30,"bold"))        #label2
label2.place(x=5,y=160)

#label1.grid(row=0,column=0,pady=3)
#label1.place(anchor=NW)
#label1.place(anchor='nw')

label3=Tkinter.Label(window,bg="black",foreground="white",text="Humidity: ",font=("DS-Digital",30,"bold"))           #label3
label3.place(x=10,y=230)

#label2.grid(row=3,column=0,pady=3)
#label2.place(relx = 1, x =1, y = 1, anchor = NW)
#label2.place(relx=1.0,rely=0.0,anchor='nw')

label4=Tkinter.Label(window,bg="black",foreground="white",text="",font=("DS-Digital",15,"bold"))   #label4
label4.place(x=300,y=460)     

# ************* setting the exit button ***************************#

exit_button=Tkinter.Button(window,bg="black",foreground="white",borderwidth=.5,text="Exit",width=10,command=window.destroy)   #button
exit_button.config(font=("DS-Digital",15))
exit_button.place(x=180,y=370)

#exit_button.grid(row=10,column=4,pady=10)
#exit_button.pack()

#*************setting up the humidity sensor datas ****************#

sensor=seeed_dht.DHT("11",2)
def count(hum=0,temp=0):
    hum,temp=sensor.read()
    label5.config(text=str(hum))
    label6.config(text=str(temp))
    window.after(1000,count,hum,temp)

label5=Tkinter.Label(window,bg="black",foreground="white",font=("DS-Digital",30,"bold"))
label5.place(x=260,y=160)

label6=Tkinter.Label(window,bg="black",foreground="white",font=("DS-Digital",30,"bold"))
label6.place(x=260,y=230)

label7=Tkinter.Label(window,bg="black",foreground="white",text="%",font=("DS-Digital",30,"bold"))
label7.place(x=310,y=160)

label8=Tkinter.Label(window,bg="black",foreground="white",text="*c",font=("DS-Digital",30,"bold"))
label8.place(x=310,y=230)


count()

#**************End of the program**********************************#
window.mainloop()               #running the window in a main loop
 
