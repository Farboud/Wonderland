

def mainmenu():
    root = Tk()

    root.title("WonderDam")

#Logo and Title
    logo = PhotoImage(file="/Users/Farboud/Farboud/University (MS)/Term/Thesis/Python Program/sharif.gif")
    title="برنامه‌ریزی مخزن سد برای آینده"
    w = Label(root, padx=10, compound=LEFT, justify=RIGHT, image=logo).grid(row=0,column=1)
    w = Label(root, padx=10, compound=LEFT, text=title, font="Yas 16 bold", fg="red", justify=RIGHT).grid(row=0,column=2)

#Initial Conditions
    w = Label(root, padx=10, compound=RIGHT, text="شرایط اوّلیه:", font="Yas 14 bold", justify=RIGHT).grid(row=19,column=2)

    years=StringVar()
    year = Label(root, text="= تعداد سال‌ها", font="Yas").grid(row=20,column=1)
    year=Entry(root, textvariable=years)
    year.insert(10,"200")
    year.grid(row=20,column=2)


    y=StringVar()
    yy = Label(root, text="Y =", font="Yas").grid(row=21,column=1)
    yy=Entry(root, textvariable=y)
    yy.insert(20,"1")
    yy.grid(row=21,column=2)

    k=StringVar()
    kk = Label(root, text="K =", font="Yas").grid(row=22,column=1)
    kk=Entry(root, textvariable=k)
    kk.insert(30,"1")
    kk.grid(row=22,column=2)

    n=StringVar()
    nn = Label(root, text="N =", font="Yas").grid(row=23,column=1)
    nn=Entry(root, textvariable=n)
    nn.insert(40,"0.98")
    nn.grid(row=23,column=2)


    p=StringVar()
    pp = Label(root, text="P =", font="Yas").grid(row=24,column=1)
    pp=Entry(root, textvariable=p)
    pp.insert(50,"1")
    pp.grid(row=24,column=2)

    tr=StringVar()
    trr = Label(root, text="= نرخ مالیات", font="Yas").grid(row=25,column=1)
    trr=Entry(root,textvariable=tr)
    trr.insert(60,"0")
    trr.grid(row=25,column=2)

#Scenario Selection
    Label(root,
      text="انتخاب سناریو:",
      font = "Yas 14 bold",
      justify = RIGHT,
      padx = 20).grid(row=30,column=2)
    sc=StringVar()
    sc.set("dream")
    Radiobutton(root,
            text="رؤیا",
            font = "Yas",
            padx = 20,
            variable=sc,
            justify=LEFT,
            value="dream").grid(row=31,column=1)
    Radiobutton(root,
            text="کابوس",
            font = "Yas",
            padx = 20,
            variable=sc,
            justify=LEFT,
            value="horror").grid(row=32,column=1)
    Radiobutton(root,
            text="فرار",
            font = "Yas",
            padx = 20,
            variable=sc,
            justify=LEFT,
            value="escape").grid(row=33,column=1)
    Radiobutton(root,
            text="بدون تغییر",
            font = "Yas",
            padx = 20,
            variable=sc,
            justify=LEFT,
            value="no_change").grid(row=34,column=1)
    #Radiobutton(root,
    #            text="فرار (۰٫۲۵)",
    #            font = "Yas",
    #            padx = 20,
    #            variable=sc,
    #            justify=LEFT,
    #            value="escape25").grid(row=34,column=1)

#State Form
    Label(root,
      text="اعمال نویز:",
      font = "Yas 14 bold",
      justify = RIGHT,
      padx = 20).grid(row=40,column=2)

    noise=BooleanVar()
    noise.set(False)
    Radiobutton(root,
            text="بله",
            font = "Yas",
            padx = 20,
            variable=noise,
            value=True).grid(row=41,column=2)
    Radiobutton(root,
            text="خیر",
            font = "Yas",
            padx = 20,
            variable=noise,
            value=False).grid(row=41,column=1)


#Buttons
    button = Button(root, text='خروج', font="Yas 14 bold", width=15, command=root.destroy)
    button.grid(row=50,column=1)
    button = Button(root, text='ادامه', font="Yas 14 bold", width=15, command=root.destroy)
    button.grid(row=50,column=2)

    root.mainloop()

#get values from window
    years=int(years.get())
    y=float(y.get())
    k=float(k.get())
    n=float(n.get())
    p=float(p.get())
    tr=float(tr.get())
    sc=sc.get()
    noise=noise.get()

    return (years,y,k,n,p,tr,sc,noise)

from tkinter import *
from tkinter import ttk
(years,y,k,n,p,tr,sc,noise)=mainmenu()
print(years,y,k,n,p,tr,sc,noise)
