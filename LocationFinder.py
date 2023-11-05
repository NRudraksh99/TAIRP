from geopy.geocoders import Nominatim as nm
from tkinter import Tk,Label,Entry,Button

f=nm(user_agent="LocationFinder")
    
def getLocation():
    address=""
    lat=float(lat_input.get())
    lon=float(lon_input.get())
    if lat<(-90) or lat>90 or lon<(-180) or lon>180:
        l.config(text="Invalid Co-ordinate(s) entered.... Please try again!!")
    else:
        try:
            location=f.reverse((lat,lon),timeout=20)
            location=location.raw["address"]
            for i in location.keys():
                address+=f"{location[i]}\n"
            l.config(text=f"Location Obtained: {address}")
        except:
            l.config(text="Unfortunately, we couldn't locate the entered Coordinates...")


r=Tk()
r.title("LocationFinder Pro!")
Label(r,text="GUI Program for Finding Location based on Latitude and Longitude!",font=100).grid(row=0)

Label(r, text='Enter the Latitude:',font=72).grid(row=1)
Label(r,text="Enter the Longitude: ",font=72).grid(row=2)
lat_input=Entry(r)
lat_input.grid(row=1,column=1)
lon_input=Entry(r)
lon_input.grid(row=2,column=1)

l=Label(r,text="",font=72)
l.grid(row=5)

btn=Button(r,text="Check!",font=72,fg="white",bg="black",command=getLocation).grid(row=6)

r.mainloop()