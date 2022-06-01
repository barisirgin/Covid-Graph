import json
import matplotlib.pyplot as pl
from tkinter import *
import PIL.Image
import PIL.ImageTk

with open ( "turkey.json" ) as tr:
    data = json.load ( tr )
    tarih = []
    vaka = []
    gunVaka = []
    olu = []
    gunOlu = []
    aVaka = []
    iyi = []
    gunIyı = []

    for i in range (100): # Api de bazı variler girilmediği için grafikte sıkıntı yaşadım.O yüzden ilk 100 gün üzerinden işlem yapıyorum.
        print ( "Tarih : " + data[i]["Date"][:10] )
        print ( "Vaka Sayısı : " + str ( data[i]["Confirmed"] ) )
        print ( "Günlük Vaka Saysı : " + str ( data[i]["Confirmed"] - data[i - 1]["Confirmed"] ) )
        print ( "Ölüm Saysı : " + str ( data[i]["Deaths"] ) )
        print ( "Günlük Ölüm Saysı : " + str ( data[i]["Deaths"]-data[i-1]["Deaths"] ) )
        print ( "İyileşen Kişi Sayısı : " + str ( data[i]["Recovered"] ) )
        print ( "Günlük İyileşen Kişi Sayısı : " + str ( data[i]["Recovered"] - data[i-1]["Recovered"] ) )
        print ( "Aktif Vaka Sayısı : " + str ( data[i]["Active"] ) )
        tarih.append ( i )
        gunVaka.append ( (data[i+1]["Confirmed"]) - (data[i]["Confirmed"]) )
        vaka.append ( data[i]["Confirmed"] )
        gunOlu.append((data[i+1]["Deaths"])-(data[i]["Deaths"]))
        olu.append ( data[i]["Deaths"] )
        aVaka.append ( data[i]["Active"] )
        iyi.append ( data[i]["Recovered"] )
        gunIyı.append((data[i+1]["Recovered"]) - (data[i]["Recovered"]) )
        print ( "--------------------" )

    pl.plot ( tarih,vaka )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "Vaka" )
    pl.title ( "Türkiye Covid-19 Vaka Analiz Grafiği" )
    pl.savefig ( "vaka.PNG" )
    #pl.show ()

    pl.plot ( tarih,gunVaka )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "Günlük Vaka" )
    pl.title ( "Türkiye Covid-19 Günlük Vaka Analiz Grafiği" )
    pl.savefig ( "gunVaka.PNG" )
    #pl.show ()

    pl.plot ( tarih,olu )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "Ölü" )
    pl.title ( "Türkiye Covid-19 Ölüm Analiz Grafiği" )
    pl.savefig ( "olu.PNG" )
    #pl.show ()

    pl.plot ( tarih,gunOlu )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "Günlük Ölüm Sayısı" )
    pl.title ( "Türkiye Covid-19 Günlük Ölüm Analiz Grafiği" )
    pl.savefig ( "gunOlu.PNG" )
    #pl.show ()

    pl.plot ( tarih,aVaka )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "Aktif Vaka Sayısı" )
    pl.title ( "Türkiye Covid-19 Aktif Vaka Analiz Grafiği" )
    pl.savefig ( "aktif.PNG" )
    #pl.show ()

    pl.plot ( tarih,iyi )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "iyileşen Sayısı" )
    pl.title ( "Türkiye Covid-19 İyileşen Kişi Analiz Grafiği" )
    pl.savefig ( "iyi.PNG" )
    #pl.show ()

    pl.plot ( tarih,gunIyı )
    pl.xlabel ( "Gün" )
    pl.ylabel ( "Günlük iyileşen Sayısı" )
    pl.title ( "Türkiye Covid-19 Günlük İyileşen Kişi Analiz Grafiği" )
    pl.savefig ( "gunIyı.PNG" )
    pl.show ()


pencere = Tk ()


# pencere.geometry("250x300+50+50")

def vaka():
    root = Toplevel ()
    im = PIL.Image.open ( "vaka.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

def gunVaka():
    root = Toplevel ()
    im = PIL.Image.open ( "gunVaka.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

def gunOlu():
    root = Toplevel ()
    im = PIL.Image.open ( "gunOlu.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

def olu():
    root = Toplevel ()
    im = PIL.Image.open ( "olu.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

def aktif():
    root = Toplevel ()
    im = PIL.Image.open ( "aktif.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

def iyi():
    root = Toplevel ()
    im = PIL.Image.open ( "iyi.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

def gunIyı():
    root = Toplevel ()
    im = PIL.Image.open ( "gunIyı.PNG" )
    photo = PIL.ImageTk.PhotoImage ( im )
    label = Label ( root,image=photo )
    label.image = photo
    label.pack ()
    root.mainloop ()

Frame1 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame1.grid ( row=0,column=0 )
Frame2 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame2.grid ( row=4,column=0 )
Frame3 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame3.grid ( row=8,column=0 )
Frame4 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame4.grid ( row=12,column=0 )
Frame5 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame5.grid ( row=16,column=0 )
Frame6 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame6.grid ( row=20,column=0 )
Frame7 = Frame ( highlightthickness=8,bd=8,relief=GROOVE )
Frame7.grid ( row=24,column=0 )

app = pencere.title ( "Covid -19 Grafik Uygulaması" )

vakaButton = Button ( Frame1,text="        Vaka Sayısı        ",font="DejaVuSans 15 bold",command=vaka,fg="white",bg="red" )
vakaButton.grid ( row=10,column=10,columnspan=2 )

gunVakaButton = Button ( Frame2,text="     Günlük Vaka Sayısı    ",font="DejaVuSans 15 bold",command=gunVaka,fg="white",bg="red" )
gunVakaButton.grid ( row=10,column=10,columnspan=2 )

aktifButton = Button ( Frame3,text="     Aktif Vaka Sayısı     ",font="DejaVuSans 15 bold",command=aktif,fg="white",bg="red" )
aktifButton.grid ( row=10,column=10,columnspan=2 )

oluButton = Button ( Frame4,text="        Ölüm Sayısı        ",font="DejaVuSans 15 bold",command=olu,fg="white",bg="red" )
oluButton.grid ( row=10,column=10,columnspan=2 )

gunOluButton = Button ( Frame5,text="     Günlük Ölüm Sayısı    ",font="DejaVuSans 15 bold",command=gunOlu,fg="white",bg="red" )
gunOluButton.grid ( row=10,column=10,columnspan=2 )

iyiButton = Button ( Frame6,text="    İyileşen Kişi Sayısı   ",font="DejaVuSans 15 bold",command=iyi,fg="white",bg="red" )
iyiButton.grid ( row=10,column=10,columnspan=2 )

gunIyiButton = Button ( Frame7,text="Günlük İyileşen Kişi Sayısı",font="DejaVuSans 15 bold",command=gunIyı,fg="white",bg="red" )
gunIyiButton.grid ( row=10,column=10,columnspan=2 )

mainloop ()
