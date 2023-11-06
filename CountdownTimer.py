from tkinter import StringVar, Tk,messagebox,Label,Entry,Button
from time import sleep as sl

r=Tk()
r.title("PyTimer")
r.resizable(False, False)
r.configure(background="#8772f2")

h_d=StringVar()
m_d=StringVar()
s_d=StringVar()

def timer():
    try:
        h=int(h_d.get())
        m=int(m_d.get())
        s=int(s_d.get())
        if h>2 or m>59 or s>59:
            raise TypeError
        t=h*3600+m*60+s
        while(t > -1):
            m, s = divmod(t, 60)
            h = 0
            if(m > 60):
                h, m = divmod(m, 60)
            h_d.set("{0:2d}".format(h))
            m_d.set("{0:2d}".format(m))
            s_d.set("{0:2d}".format(s))
            r.update()
            sl(1)
            if(t == 0):
                messagebox.showinfo("PyTimer", "Time's Up!!")
            t -= 1
    except:
        messagebox.showinfo("PyTimer","Either invalid values were entered or the time entered is too long....")

Label(r,text="GUI Program for a Basic Countdown timer!",font=100,bg="#8772f2").grid(row=0,column=0)

x=Label(r,text="Hours:\t",font=72,bg="#8772f2")
x.grid(row=2,column=0)
y=Label(r,text="Minutes:\t",font=72,bg="#8772f2")
y.grid(row=4,column=0)
z=Label(r,text="Seconds:\t",font=72,bg="#8772f2")
z.grid(row=6,column=0)

h_input=Entry(r,textvariable=h_d,width=3, font=("Calibri", 20, ""))
h_input.insert(0,"0")
h_input.grid(row=3,column=0)
m_input=Entry(r,textvariable=m_d,width=3, font=("Calibri", 20, ""))
m_input.grid(row=5,column=0)
m_input.insert(0,"0")
s_input=Entry(r,textvariable=s_d,width=3, font=("Calibri", 20, ""))
s_input.grid(row=7,column=0)
s_input.insert(0,"0")

btn=Button(r,text="Start!",font=72,fg="white",bg="black",command=timer).grid(row=12)

r.mainloop()