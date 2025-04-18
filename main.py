from tkinter import*
import random
import time
from tkinter import messagebox
import datetime

root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background='black')
Tops=Frame(root,width=1350,height=100,bd=14,relief="raise")
Tops.pack(side=TOP)
f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)
f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)
ft2=Frame(f2,width=440,height=450,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440,height=250,bd=16,relief="raise")
fb2.pack(side=BOTTOM)
f1aa=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)
f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)
Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
#====================================costofitem=====================================
def Costofitem():
    item1=float(elatte.get())
    item2 = float(eirishcoffee.get())
    item3 = float(ecoldcoffee.get())
    item4 = float(eorangesquash.get())
    item5 = float(emangosquash.get())
    item6 = float(efruitjuice.get())
    item7 = float(ecolddrink.get())
    item8 = float(evirginmojito.get())
    item9 = float(edrycake.get())
    item10 = float(echoclatecake.get())
    item11 = float(ebutterscothcake.get())
    item12 = float(eblackforestcake.get())
    item13 = float(eredvelvetcake.get())
    item14 = float(etriocake.get())
    item15 = float(edryfruitcake.get())
    item16 = float(efreshfruitcake.get())
    priceofdrinks=item1*50+item2*100+item3*150+item4*200+item5*250+item6*300+item7*350+item8*400
    priceofcakes=item9*50+item10*100+item11*150+item12*200+item13*250+item14*300+item15*350+item16*400
    drinksprice="Rs.",str('%.2f'%(priceofdrinks))
    cakesprice = "Rs.", str( '%.2f'%(priceofcakes))
    Costofcakes.set(cakesprice)
    Costofdrinks.set(drinksprice)
    sc="Rs.",str('%.2f'%(100))
    Servicecharge.set(sc)
    Subtotalofitems=float('%.2f'%(priceofdrinks+priceofcakes+100))
    Subtotal.set(Subtotalofitems)
    tax=float('%.2f'%((Subtotalofitems)*0.15))
    Paidtax.set(tax)
    tt=((priceofdrinks+priceofcakes+100)*0.15)
    tc="Rs.",str('%.2f'%(priceofcakes+priceofdrinks+100+tt))
    Totalcost.set(tc)

def Qexit():
    Qexit=messagebox.askyesno("quit System","Do you want to quit?" )
    if(Qexit>0):
        root.destroy()
        return

def Reset():
    Paidtax.set("")
    Subtotal.set("")
    Totalcost.set("")
    Costofdrinks.set("")
    Costofcakes.set("")
    Servicecharge.set("")
    txtreceipt.delete("1.0",END)
    elatte.set("0")
    efreshfruitcake.set("0")
    edryfruitcake.set("0")
    etriocake.set("0")
    eredvelvetcake.set("0")
    eblackforestcake.set("0")
    ebutterscothcake.set("0")
    echoclatecake.set("0")
    edrycake.set("0")
    evirginmojito.set("0")
    ecolddrink.set("0")
    efruitjuice.set("0")
    emangosquash.set("0")
    eorangesquash.set("0")
    ecoldcoffee.set("0")
    eirishcoffee.set("0")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    txtlatte.configure(state=DISABLED)
    txtirishcoffee.configure(state=DISABLED)
    txtmangosquash.configure(state=DISABLED)
    txtorangesquash.configure(state=DISABLED)
    txtcoldcoffee.configure(state=DISABLED)
    txtcolddrink.configure(state=DISABLED)
    txtfruitjuice.configure(state=DISABLED)
    txtvirginmojito.configure(state=DISABLED)
    txtblackforest.configure(state=DISABLED)
    txtbutterscothcake.configure(state=DISABLED)
    txtchoclatecake.configure(state=DISABLED)
    txtdrycake.configure(state=DISABLED)
    txtdryfruitcake.configure(state=DISABLED)
    txtfreshfruitcake.configure(state=DISABLED)
    txtredvelvetcake.configure(state=DISABLED)
    txttriocake.configure(state=DISABLED)


def Receipt():
    txtreceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomref=str(x)
    txtreceipt.insert(END,'\t\t'+Dateoforder.get()+"\n")
    txtreceipt.insert(END,'Items\t\t\t'+'Quantity of items\n\n')
    txtreceipt.insert(END,'Latte:\t\t\t\''+elatte.get()+"\n")
    txtreceipt.insert(END, 'Irish Coffee:\t\t\t' + eirishcoffee.get() + "\n")
    txtreceipt.insert(END, 'Cold Coffee:\t\t\t' + ecoldcoffee.get() + "\n")
    txtreceipt.insert(END, 'Orange Squash:\t\t\t' + eorangesquash.get() + "\n")
    txtreceipt.insert(END, 'Mango Squash:\t\t\t' + emangosquash.get() + "\n")
    txtreceipt.insert(END, 'Fruit Juice:\t\t\t' + efruitjuice.get() + "\n")
    txtreceipt.insert(END, 'Cold Drink:\t\t\t' + ecolddrink.get() + "\n")
    txtreceipt.insert(END, 'Virgin Mojito:\t\t\t' + evirginmojito.get() + "\n")
    txtreceipt.insert(END, 'Dry Cake:\t\t\t' + edrycake.get() + "\n")
    txtreceipt.insert(END, 'Choclate Cake\t\t\t' +echoclatecake.get() + "\n")
    txtreceipt.insert(END, 'Butter Scoth Cake:\t\t\t' + ebutterscothcake.get() + "\n")
    txtreceipt.insert(END, 'Black Forest Cake:\t\t\t' + eblackforestcake.get() + "\n")
    txtreceipt.insert(END, 'Red Velvet Cake:\t\t\t' + eredvelvetcake.get() + "\n")
    txtreceipt.insert(END, 'Trio Cake:\t\t\t' + etriocake.get() + "\n")
    txtreceipt.insert(END, 'Dry Fruit Cake:\t\t\t' + edryfruitcake.get() + "\n")
    txtreceipt.insert(END, 'Fresh Fruit Cake:\t\t\t' + efreshfruitcake.get() + "\n")
    txtreceipt.insert(END, 'Cost Of Drinks:\t\t\t' + Costofdrinks.get() + "\n")
    txtreceipt.insert(END, 'Cost Of Cakes:\t\t\t' + Costofcakes.get() + "\n")
    txtreceipt.insert(END, 'Service Charge:\t\t\t' + Servicecharge.get() + "\n")


#===========================heading=================================================
Lblinfo=Label(Tops,font=('arial',50,'bold'),text="Cafe Management System",bd=10)
Lblinfo.grid(row=0,column=0)
#===========================calculator=================================================
def checkbutton_value():
    if (var1.get()==1):
        txtlatte.configure(state=NORMAL)
    elif(var1.get()==0):
        txtlatte.configure(state=DISABLED)
    if (var2.get()==1):
        txtirishcoffee.configure(state=NORMAL)
    elif(var2.get()==0):
        txtirishcoffee.configure(state=DISABLED)
    if (var3.get()==1):
        txtcoldcoffee.configure(state=NORMAL)
    elif(var3.get()==0):
        txtcoldcoffee.configure(state=DISABLED)
    if (var4.get()==1):
        txtorangesquash.configure(state=NORMAL)
    elif(var4.get()==0):
        txtorangesquash.configure(state=DISABLED)
    if (var5.get()==1):
        txtmangosquash.configure(state=NORMAL)
    elif(var5.get()==0):
        txtmangosquash.configure(state=DISABLED)
    if (var6.get()==1):
        txtfruitjuice.configure(state=NORMAL)
    elif(var6.get()==0):
        txtfruitjuice.configure(state=DISABLED)
    if (var7.get()==1):
        txtcolddrink.configure(state=NORMAL)
    elif(var7.get()==0):
        txtcolddrink.configure(state=DISABLED)
    if (var8.get()==1):
        txtvirginmojito.configure(state=NORMAL)
    elif(var8.get()==0):
        txtvirginmojito.configure(state=DISABLED)
    if (var9.get()==1):
        txtdrycake.configure(state=NORMAL)
    elif(var9.get()==0):
        txtdrycake.configure(state=DISABLED)
    if (var10.get()==1):
        txtchoclatecake.configure(state=NORMAL)
    elif(var10.get()==0):
        txtchoclatecake.configure(state=DISABLED)
    if (var11.get()==1):
        txtbutterscothcake.configure(state=NORMAL)
    elif(var11.get()==0):
        txtbutterscothcake.configure(state=DISABLED)
    if (var12.get()==1):
        txtblackforest.configure(state=NORMAL)
    elif(var12.get()==0):
        txtblackforest.configure(state=DISABLED)
    if (var13.get()==1):
        txtredvelvetcake.configure(state=NORMAL)
    elif(var13.get()==0):
        txtredvelvetcake.configure(state=DISABLED)
    if (var14.get()==1):
        txttriocake.configure(state=NORMAL)
    elif(var14.get()==0):
        txttriocake.configure(state=DISABLED)
    if (var15.get()==1):
        txtdryfruitcake.configure(state=NORMAL)
    elif(var15.get()==0):
        txtdryfruitcake.configure(state=DISABLED)
    if (var16.get()==1):
        txtfreshfruitcake.configure(state=NORMAL)
    elif(var16.get()==0):
        txtfreshfruitcake.configure(state=DISABLED)

#===================================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
Dateoforder=StringVar()
Receiptref=StringVar()
Paidtax=StringVar()
Subtotal=StringVar()
Totalcost=StringVar()
Costofcakes=StringVar()
Costofdrinks=StringVar()
Servicecharge=StringVar()

elatte=StringVar()
eirishcoffee=StringVar()
ecoldcoffee=StringVar()
eorangesquash=StringVar()
emangosquash=StringVar()
efruitjuice=StringVar()
ecolddrink=StringVar()
evirginmojito=StringVar()
edrycake=StringVar()
echoclatecake=StringVar()
ebutterscothcake=StringVar()
eblackforestcake=StringVar()
eredvelvetcake=StringVar()
etriocake=StringVar()
edryfruitcake=StringVar()
efreshfruitcake=StringVar()

elatte.set("0")
eirishcoffee.set("0")
ecoldcoffee.set("0")
eorangesquash.set("0")
emangosquash.set("0")
efruitjuice.set("0")
ecolddrink.set("0")
evirginmojito.set("0")
edrycake.set("0")
echoclatecake.set("0")
ebutterscothcake.set("0")
eblackforestcake.set("0")
eredvelvetcake.set("0")
etriocake.set("0")
edryfruitcake.set("0")
efreshfruitcake.set("0")

Dateoforder.set(time.strftime("%d/%m/%Y"))



#============================drinks======================
latte=Checkbutton(f1aa,text="Latte \t",variable=var1,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=0,column=0,sticky= W)
irishcoffee=Checkbutton(f1aa,text="Irish Coffee \t",variable=var2,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=1,column=0,sticky= W)
coldcoffee=Checkbutton(f1aa,text="Cold Coffee \t",variable=var3,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=2,column=0,sticky= W)
orangesquash=Checkbutton(f1aa,text="Orange Squash \t",variable=var4,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=3,column=0,sticky= W)
mangosquash=Checkbutton(f1aa,text="Mango Squash \t",variable=var5,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=4,column=0,sticky= W)
fruitjuice=Checkbutton(f1aa,text="Fruit juice \t",variable=var6,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=5,column=0,sticky= W)
colddrink=Checkbutton(f1aa,text="Cold Drink \t",variable=var7,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=6,column=0,sticky= W)
virginmojito=Checkbutton(f1aa,text="Virgin Mojito \t",variable=var8,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=7,column=0,sticky= W)
#=========================cakes===========================
drycake=Checkbutton(f1ab,text="Dry Cake \t",variable=var9,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=0,column=0,sticky= W)
choclatecake=Checkbutton(f1ab,text="Choclate Cake \t",variable=var10,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=1,column=0,sticky= W)
butterscothcake=Checkbutton(f1ab,text="ButterScoth Cake \t",variable=var11,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=2,column=0,sticky= W)
blackforestcake=Checkbutton(f1ab,text="Black Forest Cake \t",variable=var12,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=3,column=0,sticky= W)
redvelvetcake=Checkbutton(f1ab,text="Red Velvet Cake \t",variable=var13,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=4,column=0,sticky= W)
triocake=Checkbutton(f1ab,text="Trio Cake \t",variable=var14,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=5,column=0,sticky= W)
dryfruitcake=Checkbutton(f1ab,text="Dry Fruit Cake \t",variable=var15,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=6,column=0,sticky= W)
freshfruitcake=Checkbutton(f1ab,text="Fresh Fruit Cake \t",variable=var16,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=checkbutton_value).grid(row=7,column=0,sticky= W)
#=========================enter widgets for drinks======================================
txtlatte=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=elatte,state=DISABLED)
txtlatte.grid(row=0,column=1)
txtirishcoffee=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=eirishcoffee,state=DISABLED)
txtirishcoffee.grid(row=1,column=1)
txtcoldcoffee=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=ecoldcoffee,state=DISABLED)
txtcoldcoffee.grid(row=2,column=1)
txtorangesquash=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=eorangesquash,state=DISABLED)
txtorangesquash.grid(row=3,column=1)
txtmangosquash=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=emangosquash,state=DISABLED)
txtmangosquash.grid(row=4,column=1)
txtfruitjuice=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=efruitjuice,state=DISABLED)
txtfruitjuice.grid(row=5,column=1)
txtcolddrink=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=ecolddrink,state=DISABLED)
txtcolddrink.grid(row=6,column=1)
txtvirginmojito=Entry(f1aa,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=evirginmojito,state=DISABLED)
txtvirginmojito.grid(row=7,column=1)
#========================enter widgetsforcakes============================================
txtdrycake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=edrycake,state=DISABLED)
txtdrycake.grid(row=0,column=1)
txtchoclatecake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=echoclatecake,state=DISABLED)
txtchoclatecake.grid(row=1,column=1)
txtbutterscothcake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=ebutterscothcake,state=DISABLED)
txtbutterscothcake.grid(row=2,column=1)
txtblackforest=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=eblackforestcake,state=DISABLED)
txtblackforest.grid(row=3,column=1)
txtredvelvetcake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=eredvelvetcake,state=DISABLED)
txtredvelvetcake.grid(row=4,column=1)
txttriocake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=etriocake,state=DISABLED)
txttriocake.grid(row=5,column=1)
txtdryfruitcake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=edryfruitcake,state=DISABLED)
txtdryfruitcake.grid(row=6,column=1)
txtfreshfruitcake=Entry(f1ab,font=('arial',12,'bold'),bd=18,width=6,justify='left',textvariable=efreshfruitcake,state=DISABLED)
txtfreshfruitcake.grid(row=7,column=1)
#========================information=======================================================
lblreceipt=Label(ft2,font=('arial',10,'bold'),text='Receipt:',bd=2,anchor='w')
lblreceipt.grid(row=0,column=0,sticky=W)
txtreceipt=Text(ft2,width=48,height=22,bg="white",bd=8,font=('arial',10,'bold'))
txtreceipt.grid(row=1,column=0)

#======================cost of items==========================================
lblcostofdrinks=Label(f2aa,font=('arial',12,'bold'),text='Cost Of Drinks',bd=8,anchor='w')
lblcostofdrinks.grid(row=0,column=0,sticky=W)
txtcostofdrinks=Entry(f2aa,font=('arial',14,'bold'),bd=8,justify='left',textvariable=Costofdrinks)
txtcostofdrinks.grid(row=0,column=1,sticky=W)

lblcostofcakes=Label(f2aa,font=('arial',12,'bold'),text='Cost Of Cakes',bd=8,anchor='w')
lblcostofcakes.grid(row=1,column=0,sticky=W)
txtcostofcakes=Entry(f2aa,font=('arial',14,'bold'),bd=8,justify='left',textvariable=Costofcakes)
txtcostofcakes.grid(row=1,column=1,sticky=W)

lblservicecharge=Label(f2aa,font=('arial',12,'bold'),text='Service Charge',bd=8,anchor='w')
lblservicecharge.grid(row=2,column=0,sticky=W)
txtservicecharge=Entry(f2aa,font=('arial',14,'bold'),bd=8,justify='left',textvariable=Servicecharge)
txtservicecharge.grid(row=2,column=1,sticky=W)

#============================payment info==========================

lbltax=Label(f2ab,font=('arial',12,'bold'),text='Tax',bd=8)
lbltax.grid(row=0,column=0,sticky=W)
txttax=Entry(f2ab,font=('arial',14,'bold'),bd=8,textvariable=Paidtax,justify='left')
txttax.grid(row=0,column=1,sticky=W)

lblsubtotal=Label(f2ab,font=('arial',12,'bold'),text='SubTotal',bd=8)
lblsubtotal.grid(row=1,column=0,sticky=W)
txtsubtotal=Entry(f2ab,font=('arial',14,'bold'),bd=8,textvariable=Subtotal,justify='left')
txtsubtotal.grid(row=1,column=1,sticky=W)

lbltotal=Label(f2ab,font=('arial',12,'bold'),text='Total',bd=8)
lbltotal.grid(row=2,column=0,sticky=W)
txttotal=Entry(f2ab,font=('arial',14,'bold'),bd=8,textvariable=Totalcost,justify='left')
txttotal.grid(row=2,column=1,sticky=W)
#========================buttons===============================
btntotal=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,text='Total',command=Costofitem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,text='Receipt',command=Receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,text='Reset',command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,text='Exit',command=Qexit).grid(row=0,column=3)

root.mainloop()
