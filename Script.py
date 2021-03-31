from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def find():
    s=e1.get()
    l=Nominatim(user_agent="geoapiExcercise")
    x=l.geocode(s)
    tz=TimezoneFinder()
    lat=x.latitude
    long=x.longitude
    s1=tz.timezone_at(lng=long, lat=lat)
    t=pytz.timezone(s1)
    dt=datetime.now(t)
    if dt.hour<12:
        time=str(dt.hour)+":"+str(dt.minute)+":"+str(dt.second)+" AM"
    elif dt.hour>12:
        w=dt.hour-12
        time=str(w)+":"+str(dt.minute)+":"+str(dt.second)+" PM"
    else:
        time=str(dt.hour)+":"+str(dt.minute)+":"+str(dt.second)+" PM"
    
    e2.delete(first=0,last=len(e2.get()))
    e2.insert(END,str(s1))
    e3.delete(first=0,last=len(e3.get()))
    e3.insert(END,str(time))
    


window=Tk()
window.title("Know Your Time")
window.resizable(0,0)

l1=Label(window,text="Know Your Time",font=("Arial",25))
l1.grid(row=0,column=0,columnspan=3)

l2=Label(window,text="Enter the Place ",font=("Arial",18))
l2.grid(row=1,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val,font=("Arial",18))
e1.grid(row=1,column=1)

b=Button(window,text="Go",font=("Arial",14),command=find)
b.grid(row=1,column=2)

l_blank=Label(window,text="",font=5)
l_blank.grid(row=2,column=0,columnspan=3)

l3=Label(window,text="Time Zone",font=("Arial",18))
l3.grid(row=3,column=0)

e2_val=StringVar()
e2=Entry(window,textvariable=e2_val,font=("Arial",18),width=24)
e2.grid(row=3,column=1,columnspan=2)

l4=Label(window,text="Time",font=("Arial",18))
l4.grid(row=4,column=0)

e3_val=StringVar()
e3=Entry(window,textvariable=e3_val,font=("Arial",18),width=24)
e3.grid(row=4,column=1,columnspan=2)

window.mainloop()
