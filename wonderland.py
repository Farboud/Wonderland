import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from gui import mainmenu
from calc import wonderland

def plot(x,y,x_name,y_name,scenario):
    # Plot
    root = Tk.Tk()
    root.wm_title(y_name)
    f = Figure(dpi=100)
    a = f.add_subplot(111)
    t = arange(0.0, 3.0, 0.01)
    
    a.plot(x,y)
    a.set_title(scenario.title())
    a.set_xlabel(x_name)
    a.set_ylabel(y_name)
    
    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    
    button = Tk.Button(master=root, text='ادامه', command=root.destroy, width=16, font="Yas 16 bold")
    button.pack(side=Tk.RIGHT, expand=Tk.YES)
    button = Tk.Button(master=root, text='خروج', command=sys.exit, width=16, font="Yas 16 bold")
    button.pack(side=Tk.LEFT, expand=Tk.YES)
    
#    root.iconbitmap(r'sharif.ico')
    
    
    Tk.mainloop()






def main():
    (years,y,k,n,p,tr,scenario,noise)=mainmenu()

    res=wonderland(years,y,k,n,p,tr,scenario,noise)
    y=[]
    x=[]
    for i in range(0,9):
        y.append((i+1)**(1/2))
        x.append(i+1)

# Plot
#Per Capita Output
    plot(res[4],res[0],"Time","Per Capita Output",scenario)
#Population
    plot(res[4],res[1],"Time","Population",scenario)
#Natural Capital
    plot(res[4],res[2],"Time","Natural Capital",scenario)
#Polution Per Unit Output
    plot(res[4],res[3],"Time","Polution Per Unit Output",scenario)


if __name__ == "__main__":
    main()
    
