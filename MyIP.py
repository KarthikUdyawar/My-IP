import requests
from tkinter import *

try:
    url = "https://ipinfo.io/json"
    x = requests.get(url)
    data = (x.json())

except:
    print("Error")
    
coor = data['loc'].split('.')
lat = coor[0]
lon = coor[1]
coor1 = (lat,lon)

root = Tk()
root.title("My IP")

for i,recs in enumerate (data):
    button1 = Button(root,text=recs)
    button1.grid(row=i,column=0,sticky=N,pady=5)
    entry1=Label(root,text=data[recs])
    entry1.grid(row=i,column=1,sticky=N,pady=2)
    
root.mainloop()
