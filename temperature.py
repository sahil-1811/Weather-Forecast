import tkinter as tk
from tkinter import ttk
from types import CoroutineType
import bs4
from bs4 import BeautifulSoup
import requests,threading


# headers={'''User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like  Gecko) Chrome/58.0.3029.110 Safari/537.3'''}
root=tk.Tk()
root.geometry("500x300")
root.title("Weather Prediction")
root.resizable(False,False)

frame1=tk.Frame(root,bg='#fff',width=500, height=200)
frame1.place(x=0,y=0)

frame2=tk.Frame(root,bg='#2E2E2E',width=300, height=100)
frame2.place(x=0,y=200)

frame3=tk.Frame(root,bg='#33FFDD',width=200, height=100)
frame3.place(x=300,y=200)




def Weather(*args):
    global city
    city1=city.get()
    city1=city1.replace(" ","+")

    search_label['text']="Searching For "+city.get()

    res=requests.get("https://www.google.com/search?q="+"weather"+city1)
    # res=requests.get(f'''https://www.google.com/search?q={city1}+temperature&rlz=1C1RXQR_enIN928IN928&sxsrf=ALiCzsZCymkpk0x2plf_VGYDZl5fFRMhfw%3A1652763074089&ei=wimDYqGSBYuAmAXA0a_4CQ&ved=0ahUKEwih-7af3uX3AhULAKYKHcDoC58Q4dUDCA4&uact=5&oq={city1}+temperature&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCAAjIOCAAQgAQQsQMQgwEQyQMyBQgAEIAEMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoLCAAQgAQQsQMQgwE6BQgAEJIDOgcIIxDqAhAnOgcILhDqAhAnOgQIIxAnOgUIABCRAjoRCC4QgAQQsQMQgwEQxwEQ0QM6BAgAEEM6BwgAELEDEEM6BAguEEM6DQguEIAEEIcCELEDEBQ6CgguELEDEIMBEEM6CggAELEDEIMBEEM6DQgAELEDEIMBEMkDEEM6BwguELEDEEM6CAgAELEDEIMBOg0IABCABBCHAhCxAxAUOggILhCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6CwguEIAEEMcBEKMCOgoIABCABBCHAhAUOhMIABCABBCHAhCxAxCDARDJAxAUOgsILhCABBCxAxCDAToICC4QgAQQsQM6FQgAEIAEEIcCELEDEIMBEBQQRhCAAkoECEEYAEoECEYYAFCbBFiWPGDaPWgIcAF4BIABwgGIAdsdkgEEMC4yN5gBAKABAbABCsgBCsABAQ&sclient=gws-wiz ''')
    soup=BeautifulSoup(res.text,'html.parser')
    
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    # print(str)

    # formatting data
    data = str.split('\n')
    time=data[0].split(" ")
    time1 = time[0]
    time2 =time[1]
    sky = data[1]

    tk.Label(root,text=city1.upper(),font='Caveat 12 bold',bg='#2E2E2E',fg='#fff').place(x=130,y=250)
    tk.Label(root,text=sky,font='ROBOTO 15 bold',bg='#2E2E2E',fg='#fff').place(x=130,y=220)
    tk.Label(root,text=temp,font='ROBOTO 35 bold',bg='#2E2E2E',fg='#fff').place(x=5,y=220)
    tk.Label(root,text=time1,font='Caveat 20 bold',bg='#33FFDD',fg='#2E2E2E').place(x=320,y=210)
    tk.Label(root,text=time2,font='Caveat 20 bold',bg='#33FFDD',fg='#2E2E2E').place(x=325,y=240)
    entry.delete('0',tk.END)
    





def call_function(*args):
    T=threading.Thread(target=Weather,daemon=True)
    T.start()












global city
city=tk.StringVar()

tk.Label(root,text='Enter City Name',font=('Arial Rounded Mt Bold',12),bg='#fff').place(x=150,y=40)
entry=tk.Entry(root,textvariable=city,font=('Arial',13),bd=2,justify=tk.CENTER,relief=tk.GROOVE,width=18,bg="#D0FFBC")
entry.bind("<Return>",call_function)
entry.place(x=130,y=85)


tk.Button(root,text="Check",font=('Arial Rounded MT Bold',10),bd=2,relief=tk.GROOVE,bg="#D0FFBC",command=call_function).place(x=300,y=85)

search_label=tk.Label(root,text="",font=("Sitka Small",12),bg="#fff",fg="#24292F")
search_label.place(x=140,y=130)


root.mainloop()




