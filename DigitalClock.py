from tkinter import*
import time
import datetime
import calendar

root=Tk()
root.title("Digital Clock")
root.geometry("1350x700+0+0")
root.config(bg="#081923")

def clock():


    # ==Time
    h=str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s= str(time.strftime("%S"))
    #print(h,m,s)

    #==Date
    dd = str(time.strftime("%d"))
    mm = int(time.strftime("%m"))
    mm=calendar.month_name[mm]
    yy = datetime.datetime.now()
    #print(dd,mm,yy)

    lbl_date.config(text=dd)
    lbl_month.config(text=mm)
    lbl_year.config(text=str(yy.year))


    if int(h)>12 and int(m)>0:
        lbl_noon.config(text="PM")

    if int(h)>12:
        h=str(int(h)-12)


    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)




lbl_hr=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white")
lbl_hr.place(x=350,y=200,width=150,height=150)

lbl_hr2=Label(root,text="Hour",font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
lbl_hr2.place(x=350,y=360,width=150,height=50)

lbl_date=Label(root,text="Date",font=("times new roman",20,"bold"),bg="#087587",fg="white")
lbl_date.place(x=350,y=420,width=150,height=50)

lbl_min=Label(root,text="12",font=("times new roman",50,"bold"),bg="#008EA4",fg="white")
lbl_min.place(x=520,y=200,width=150,height=150)

lbl_min2=Label(root,text="Minute",font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
lbl_min2.place(x=520,y=360,width=150,height=50)

lbl_month=Label(root,text="Month",font=("times new roman",20,"bold"),bg="#087587",fg="white")
lbl_month.place(x=520,y=420,width=150,height=50)

lbl_sec=Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
lbl_sec.place(x=690,y=200,width=150,height=150)

lbl_sec2=Label(root,text="Second",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lbl_sec2.place(x=690,y=360,width=150,height=50)

lbl_year=Label(root,text="Year",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lbl_year.place(x=690,y=420,width=150,height=50)

lbl_noon=Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
lbl_noon.place(x=860,y=200,width=150,height=150)

lbl_noon2=Label(root,text="AM",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lbl_noon2.place(x=860,y=360,width=150,height=50)

lbl_current_date=Label(root,text="Date",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lbl_current_date.place(x=860,y=420,width=150,height=50)

clock()
root.mainloop()