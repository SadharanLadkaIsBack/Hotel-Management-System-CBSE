import random
import time
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import Treeview
import mysql.connector as mc
import traceback

Grand_total = 0
BillPrintLine = 7.0
bill_no = random.randint(1000,9999)
user = ''
order = {bill_no:[]}

root = Tk()
root.geometry("474x660+500+20")
root.title("Hotel Management System")

Mframe = Frame(root,bg='#9AD2A1',relief="ridge",bd="4")
Mframe.place(x=0,y=0,relheight=1,width=474)

bgImage = PhotoImage(file="./assets/MainBg.png")
bgImage = bgImage.subsample(1,1)

bgImgLab = Label(Mframe,image=bgImage)
bgImgLab.place(x=0,y=0,relwidth=1,relheight=1)

ChefImg = PhotoImage(file="./assets/chef.png")
ChefImg = ChefImg.subsample(2,2)

TitleImg = PhotoImage(file="./assets/Ng_TitleImg.png")
TitleImg = TitleImg.subsample(2,2)

StarterButImg = PhotoImage(file="./assets/StarterBut.png")
StarterButImg = StarterButImg.subsample(1,1)

PizzaButImg = PhotoImage(file="./assets/PizzaBut.png")
PizzaButImg = PizzaButImg.subsample(1,1)

DeserButImg = PhotoImage(file="./assets/DsertBut.png")
DeserButImg = DeserButImg.subsample(1,1)

BeverButImg = PhotoImage(file="./assets/BeverBut.png")
BeverButImg = BeverButImg.subsample(1,1)

NoodButImg = PhotoImage(file="./assets/NoodBut.png")
NoodButImg = NoodButImg.subsample(1,1)

SandwitButImg = PhotoImage(file="./assets/SandBut.png")
SandwitButImg = SandwitButImg.subsample(1,1)

SaladButImg = PhotoImage(file="./assets/SaladBut.png")
SaladButImg = SaladButImg.subsample(1,1)

MainCoButImg = PhotoImage(file="./assets/MainCoBut.png")
MainCoButImg = MainCoButImg.subsample(1,1)

PayButImg = PhotoImage(file="./assets/pay-button.png")
PayButImg = PayButImg.subsample(9,9)

AddDishButImg = PhotoImage(file="./assets/Add_Dish.png")
AddDishButImg = AddDishButImg.subsample(9,9)

DeleteDishButImg = PhotoImage(file="./assets/Delete_Dish.png")
DeleteDishButImg = DeleteDishButImg.subsample(9,9)

tilt_Lab = Label(Mframe,image=TitleImg,text="Nitin's Kitchen",bg='#9AD2A1',fg='red',font=('Chiller',32,'bold'),
                 compound='left')
tilt_Lab.place(x=100,y=30)

chef_Lab = Label(Mframe,image=ChefImg,bg='#9AD2A1')
chef_Lab.place(x=100,y=210)


roomNumber = PhotoImage(file="./assets/roomNumberIco.png")
roomNumber = roomNumber.subsample(2,2)

roomNumLab = Label(Mframe,image=roomNumber,text="Room No: ",bg='#9AD2A1',fg='chocolate',font=('Courier New', 15, 'bold'),
                 compound='left')
roomNumLab.place(x=100,y=120)

roomNoForOrder = StringVar()
roomNo = Entry(Mframe, textvariable=roomNoForOrder, width=10, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
roomNo.place(x=230, y=120)
roomNo.focus()
roomNo.delete(0,END)

def connecttodataBase():
    con=mc.connect(host="localhost",user='root',password='dav123')
    mycursor=con.cursor()
    query="use Hotel;"
    mycursor.execute(query)

def FrameRaise_ButFun(framNam):

    if roomNoForOrder.get() == '':
        messagebox.showerror('ERROR',"Room No Field Cannot Be Empty !!!",parent=Mframe)
    else:
        try:
            roomNum = int(roomNoForOrder.get())
            connecttodataBase()

            mycursor.execute("select room_No, room_status from room where room_No = %s AND room_status != %s;",(roomNum ,'AVAILABLE'))
            data=mycursor.fetchall()
            if data:
                root.geometry("948x660+220+20")
                framNam.tkraise()
                roomNo.configure(state ='disabled')
            else:
                messagebox.showerror('ERROR',"No Guest in these Room !!!",parent=Mframe)
                roomNoForOrder.set('')
        except ValueError:
            messagebox.showerror('ERROR',"Room Number Must be Number !!!",parent=Mframe)
            roomNoForOrder.set('')


def BillFrameRaiseFun():
    root.geometry("474x660+500+20")
    M3frame.tkraise()

def allOrders():
    Orderroot = Toplevel()
    Orderroot.title("ORDERS")
    Orderroot.geometry("1200x550+50+40")

    Orderframe=Frame(Orderroot,bg='lightblue',relief="sunken",bd="4")
    Orderframe.place(x=0,y=0,relheight=1,relwidth=1)

    usernameimg = PhotoImage(file='./assets/orderTitle.png')
    usernameimg = usernameimg.subsample(8,8)

    Order_Title = Label(Orderframe,bg='#6D93B1',image = usernameimg,fg = 'white',text= 'ORDERS',font=('courier',25,'italic bold'),relief="sunken",bd="4",compound ='left')
    Order_Title.place(x=10,y=10,height=75,width=1175)

    OrderTabframe=Frame(Orderframe,bg='#E6D1A4',relief="groove",bd="4")
    OrderTabframe.place(x=20,y=120,height=400,width=1160)

    OrderScrolly=Scrollbar(OrderTabframe,orient="vertical")

    style.configure('Order.Treeview',font=('Calibri',15,'italic'),fieldbackground='white',foreground='black',
                    background='white',rowheight=40)
    style.configure('Order.Treeview.Heading',font=('courier',12,'bold'),foreground='white',background='#6D93B1')
    style.map('Order.Treeview',background=[('selected','#6D93B1')],foreground=[('selected','white')])

    ordertab=Treeview(OrderTabframe,columns=('OrderId','Total_amt','Employee_Id','Bill_Status','Date'),style='Order.Treeview',yscrollcommand=OrderScrolly.set)

    OrderScrolly.pack(side='right',fill='y',anchor=N)

    OrderScrolly.configure(command=ordertab.yview)

    ordertab.column("#0",width=0,stretch=NO)
    ordertab.column("OrderId",width=100,anchor=CENTER)
    ordertab.column("Total_amt",width=400,anchor=CENTER)
    ordertab.column("Employee_Id",width=100,anchor=CENTER)
    ordertab.column("Bill_Status",width=100,anchor=CENTER)
    ordertab.column("Date",width=200,anchor=CENTER)



    ordertab.heading('#0',text="")
    ordertab.heading('OrderId',text="Order Id")
    ordertab.heading('Total_amt',text="Total Amount")
    ordertab.heading('Employee_Id',text="Employee Id")
    ordertab.heading('Bill_Status',text="Bill Status")
    ordertab.heading('Date',text="Date")


    ordertab.pack(fill='both')

    mycursor.execute("select Order_Id,Total_amt,Employee_Id,Bill_Status,Date from customer_order;")
    data=mycursor.fetchall()
    for i in data:
        ordertab.insert('',END,values=(i[0],i[1],i[2],i[3],i[4]))

    Orderroot.mainloop()

def deleteMoreDishies():
    pass

Home_Buttonimg = PhotoImage(file='./assets/HomeBtn.png')
Home_Buttonimg = Home_Buttonimg.subsample(1,1)

def backHomeFun():
    root.geometry("474x660+500+20")
    HomeFrame.tkraise()

Home_Button = Button(Mframe,image=Home_Buttonimg,command=backHomeFun,bd="4")
Home_Button.place(x=410,y=10)

Str_Button = Button(Mframe,image=StarterButImg,command=lambda:FrameRaise_ButFun(Startframe),height=38,width=160,
                    text=" Starter's",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Str_Button.place(x=60,y=170)

piz_Button = Button(Mframe,image=PizzaButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Pizzaframe),
                    text="  PIZZA",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
piz_Button.place(x=270,y=170)

Des_Button = Button(Mframe,image=DeserButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Dessframe),
                    text="  Dessert",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Des_Button.place(x=60,y=260)

Brev_Button = Button(Mframe,image=BeverButImg,height=38,command=lambda:FrameRaise_ButFun(Breveframe),width=160,
                     text="   Beverages",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Brev_Button.place(x=270,y=260)

Nod_Button = Button(Mframe,image=NoodButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Noodframe),
                    text=" Noodle's",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Nod_Button.place(x=60,y=350)

SAND_Button = Button(Mframe,image=SandwitButImg,height=38,command=lambda:FrameRaise_ButFun(SandWframe),width=160,
                     text="Sandwich's",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
SAND_Button.place(x=270,y=350)

Salad_Button = Button(Mframe,image=SaladButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Saladframe),
                      text="  Salad",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Salad_Button.place(x=60,y=440)

MAN_Button = Button(Mframe,image=MainCoButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(MainCoframe),
                    text="Main Course",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
MAN_Button.place(x=270,y=440)

Pay_Button = Button(Mframe,image=PayButImg,bg="#9AD2A1",font=('Times',14,'bold'),command=BillFrameRaiseFun,
                    borderwidth=0)
Pay_Button.place_forget()

allOrders_Button = Button(Mframe,image=AddDishButImg,bg="#9AD2A1",font=('Times',14,'bold'),command=allOrders,
                        borderwidth=0)
allOrders_Button.place(x=120,y=500)

DeleteDish_Button = Button(Mframe,image=DeleteDishButImg,bg="#9AD2A1",font=('Times',14,'bold'),command=deleteMoreDishies,
                        borderwidth=0)
DeleteDish_Button.place(x=220,y=500)


def BillingFun(Item,ItmPrice,itmAmount,TotalAmt):
    global BillPrintLine
    BillArea.insert(BillPrintLine,f'  {Item}\t\t\t\t{ItmPrice}\t {itmAmount}\t {TotalAmt}\n')
    global Grand_total
    Grand_total += TotalAmt
    BillPrintLine += 1
    Pay_Button.place(x=320,y=505)


def SelectedFrameFun(itm,price):
    Selectroot = Toplevel()
    Selectroot.geometry("500x340+500+200")
    Selectroot.title("Selected Item")
    Selectroot.resizable(False,False)

    Selectbg = PhotoImage(file="./assets/SelectItemBg1.png")
    Selectbg = Selectbg.subsample(1,2)

    SelectCan = Canvas(Selectroot,relief="ridge",bg='#E4B388',bd=4)
    SelectCan.place(x=0,y=0,relwidth=1,relheight=1)

    SelectCan.create_image((0,0),image=Selectbg,anchor=NW)
    SelectCan.create_text((73,107),text='Item :',anchor=NW,font=('Georgia',13,'italic bold'),fill='black')
    SelectCan.create_text((160,107),text=itm,anchor=NW,font=('Courier New',15,'italic bold'),fill='red')
    SelectCan.create_text((70,160),text='Amount :',anchor=NW,font=('Georgia',13,'italic bold'),fill='black')
    SelectCan.create_text((160,158),text=price,anchor=NW,font=('Georgia',14,'bold'),fill='red')
    SelectCan.create_text((70,220),text="Quantity : ",anchor=NW,font=('Georgia',13,'italic bold'),fill='black')

    Quant = StringVar()
    QuantVal = Entry(SelectCan,textvariable=Quant,width=5,fg='red',relief='groove',bd=4,font=('Georgia',15,'bold'))
    QuantVal.place(x=170,y=215)
    QuantVal.focus()
    Quant.set('')

    def addToBill():
        if Quant.get() == '':
            messagebox.showerror('ERROR',"Amount Cannot Be Empty !!!",parent=Selectroot)
        else:
            try:
                global bill_no
                x = int(Quant.get())
                total = x * int(price)
                order[bill_no].append(itm)
                BillingFun(itm,price,Quant.get(),total)
                QuantVal.delete(0,END)
                Selectroot.destroy()

            except ValueError:
                messagebox.showerror('ERROR',"Amount Must be Number !!!",parent=Selectroot)
                QuantVal.delete(0,END)

    SelSubmitBut = Button(SelectCan,text="Select",bg='#B97B3F',fg='white',bd=5,font=('Georgia',12,'bold'),
                          command=addToBill)
    SelSubmitBut.place(x=130,y=270)

    def SelCancelButFun():
        Selectroot.destroy()

    SelCancelBut = Button(SelectCan,text="Cancel",bg='#B97B3F',fg='white',bd=5,font=('Georgia',12,'bold'),
                          command=SelCancelButFun)
    SelCancelBut.place(x=230,y=270)

    Selectroot.mainloop()


##Starter Frame
Startframe = Frame(root,bg='#232731',relief="ridge",bd="3")
Startframe.place(x=474,y=0,relheight=1,width=474)

starbg = PhotoImage(file="./assets/StarterBg.png")
starbg = starbg.subsample(2,2)

starTitlImg = PhotoImage(file="./assets/StarterTitleImg.png")
starTitlImg = starTitlImg.subsample(7,7)

StarCan = Canvas(Startframe)
StarCan.place(x=0,y=0,relwidth=1,relheight=1)

StarCan.create_image((0,0),image=starbg,anchor=NW)
StarCan.create_image((80,70),image=starTitlImg,anchor=NW)
StarCan.create_text((160,70),text="STARTER",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Startminiframe = Frame(Startframe,bg='#232731',relief="ridge",bd="4")
Startminiframe.place(x=20,y=200,height=300)

# Startilt_Lab = Label(Startframe,image = TitleImg,text = "STARTER",bg = '#232731',fg= 'red',font = ('Chiller', 50,'bold'),compound ='left')
# Startilt_Lab.place(x=90,y=50)

Scrolly = Scrollbar(Startminiframe,orient="vertical")

style = ttk.Style()
style.theme_use('clam')
style.configure('Start.Treeview',font=('times',15,'italic'),fieldbackground='#394051',foreground='white',
                background='#394051',rowheight=50)
style.configure('Start.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='#232731')
style.map('Start.Treeview',background=[('selected','#232731')],foreground=[('selected','white')])

starttab = Treeview(Startminiframe,columns=('Menu','Price'),style="Start.Treeview",yscrollcommand=Scrolly.set)

Scrolly.pack(side='right',fill='y',anchor=N)

Scrolly.configure(command=starttab.yview)

starttab.column("#0",width=0,stretch=NO)
starttab.column("Menu",width=300)
starttab.column("Price",width=100,anchor=CENTER)

starttab.heading('#0',text="")
starttab.heading('Menu',text="MENU")
starttab.heading('Price',text="PRICE")

starttab.pack(fill='both')

con = mc.connect(host="localhost",user='root',password='dav123')
mycursor = con.cursor()
query = "use Hotel;"
mycursor.execute(query)

# dict1 = {}
# for key in dict1:
#     q = 'insert into Starter values(%s ,%s);'
#     mycursor.execute(q,(key,dict1[key]))

mycursor.execute("select Menu ,Price from food where Catagories = 'starter';")
data = mycursor.fetchall()
for i in data:
    starttab.insert('',END,values=(i[0],i[1]))


def on_select(event):
    a = starttab.focus()
    value = starttab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


starttab.bind('<Double-1>',on_select)

# ## PIZZA Frame
Pizzaframe = Frame(root,bg='#DC8480',relief="ridge",bd="4")
Pizzaframe.place(x=474,y=0,relheight=1,width=474)

Pizzabg = PhotoImage(file="./assets/PizzaFrameBg.png")
Pizzabg = Pizzabg.subsample(1,1)

PizzCan = Canvas(Pizzaframe)
PizzCan.place(x=0,y=0,relwidth=1,relheight=1)

PizzCan.create_image((0,0),image=Pizzabg,anchor=NW)
PizzCan.create_text((160,70),text="Pizza's",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Pizzminiframe = Frame(Pizzaframe,bg='#C64E1D',relief="ridge",bd="4")
Pizzminiframe.place(x=50,y=190,height=300)

PizzScrolly = Scrollbar(Pizzminiframe,orient="vertical")

style.configure('Pizz.Treeview',font=('times',15,'italic'),fieldbackground='#C64E1D',foreground='white',
                background='#C64E1D',rowheight=50)
style.configure('Pizz.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='#E7B237')
style.map('Pizz.Treeview',background=[('selected','#7A3218')],foreground=[('selected','white')])

Pizztab = Treeview(Pizzminiframe,columns=('Menu','Price'),style='Pizz.Treeview',yscrollcommand=PizzScrolly.set)

PizzScrolly.pack(side='right',fill='y',anchor=N)
PizzScrolly.configure(command=Pizztab.yview)

Pizztab.column("#0",width=0,stretch=NO)
Pizztab.column("Menu",width=248)
Pizztab.column("Price",width=100,anchor=CENTER)

Pizztab.heading('#0',text="")
Pizztab.heading('Menu',text="MENU")
Pizztab.heading('Price',text="PRICE")

Pizztab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'pizza';")
data = mycursor.fetchall()
for i in data:
    Pizztab.insert('',END,values=(i[0],i[1]))


def on_piz_select(event):
    a = Pizztab.focus()
    value = Pizztab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Pizztab.bind('<Double-1>',on_piz_select)

## Dessert Frame
Dessframe = Frame(root,bg='#DC8480',relief="ridge",bd="4")
Dessframe.place(x=474,y=0,relheight=1,width=474)

Dessbg = PhotoImage(file="./assets/DessBackGImg.png")
Dessbg = Dessbg.subsample(1,1)

# DessTitlImg = PhotoImage(file = "IceCreame.png")
# DessTitlImg = DessTitlImg.subsample(8,8)

DessCan = Canvas(Dessframe)
DessCan.place(x=0,y=0,relwidth=1,relheight=1)

DessCan.create_image((0,0),image=Dessbg,anchor=NW)
DessCan.create_text((160,70),text="Dessert",font=('Chiller',50,'bold'),fill='red',anchor=NW)
# DessCan.create_image((80,150),image = DessTitlImg ,anchor =NW)

Dessminiframe = Frame(Dessframe,bg='#232731',relief="ridge",bd="4")
Dessminiframe.place(x=20,y=200,height=300)

DessScrolly = Scrollbar(Dessminiframe,orient="vertical")

style.configure('Dess.Treeview',font=('times',15,'italic'),fieldbackground='#F4D0DC',foreground='black',
                background='#F4D0DC',rowheight=50)
style.configure('Dess.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='pink')
style.map('Dess.Treeview',background=[('selected','#FF537B')],foreground=[('selected','white')])

Desstab = Treeview(Dessminiframe,columns=('Menu','Price'),style='Dess.Treeview',yscrollcommand=DessScrolly.set)

DessScrolly.pack(side='right',fill='y',anchor=N)

DessScrolly.configure(command=Desstab.yview)

Desstab.column("#0",width=0,stretch=NO)
Desstab.column("Menu",width=300)
Desstab.column("Price",width=100,anchor=CENTER)

Desstab.heading('#0',text="")
Desstab.heading('Menu',text="MENU")
Desstab.heading('Price',text="PRICE")

Desstab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'dessert';")
data = mycursor.fetchall()
for i in data:
    Desstab.insert('',END,values=(i[0],i[1]))


def on_des_select(event):
    a = Desstab.focus()
    value = Desstab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Desstab.bind('<Double-1>',on_des_select)

# ## Breverages Frame
Breveframe = Frame(root,bg='#DC8480',relief="ridge",bd="4")
Breveframe.place(x=474,y=0,relheight=1,width=474)

Brevebg = PhotoImage(file="./assets/BreverageFrameBg.png")
Brevebg = Brevebg.subsample(1,1)

BreveCan = Canvas(Breveframe)
BreveCan.place(x=0,y=0,relwidth=1,relheight=1)

BreveCan.create_image((0,0),image=Brevebg,anchor=NW)
BreveCan.create_text((130,70),text="Breverage's",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Breveminiframe = Frame(Breveframe,bg='#C64E1D',relief="ridge",bd="4")
Breveminiframe.place(x=45,y=200,height=300)

BreveScrolly = Scrollbar(Breveminiframe,orient="vertical")

style.configure('Breve.Treeview',font=('times',15,'italic'),fieldbackground='#FDD768',foreground='black',
                background='#FDD768',rowheight=50)
style.configure('Breve.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='#E7B237')
style.map('Breve.Treeview',background=[('selected','#FF992B')],foreground=[('selected','white')])

Brevetab = Treeview(Breveminiframe,columns=('Menu','Price'),style='Breve.Treeview',yscrollcommand=BreveScrolly.set)

BreveScrolly.pack(side='right',fill='y',anchor=N)
BreveScrolly.configure(command=Brevetab.yview)

Brevetab.column("#0",width=0,stretch=NO)
Brevetab.column("Menu",width=260)
Brevetab.column("Price",width=100,anchor=CENTER)

Brevetab.heading('#0',text="")
Brevetab.heading('Menu',text="MENU")
Brevetab.heading('Price',text="PRICE")

Brevetab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'breveges';")
data = mycursor.fetchall()
for i in data:
    Brevetab.insert('',END,values=(i[0],i[1]))


def on_brev_select(event):
    a = Brevetab.focus()
    value = Brevetab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Brevetab.bind('<Double-1>',on_brev_select)

## Noodles Frame
Noodframe = Frame(root,bg='#2EAC63',relief="ridge",bd="4")
Noodframe.place(x=474,y=0,relheight=1,width=474)

Noodbg = PhotoImage(file="./assets/NoodleFrameBg.png")
Noodbg = Noodbg.subsample(1,1)

Noodtitlebg = PhotoImage(file="./assets/ChineseFrameTitlBg.png")
Noodtitlebg = Noodtitlebg.subsample(1,1)

NoodCan = Canvas(Noodframe)
NoodCan.place(x=0,y=0,relwidth=1,relheight=1)

NoodCan.create_image((0,0),image=Noodbg,anchor=NW)
NoodCan.create_image((20,40),image=Noodtitlebg,anchor=NW)
NoodCan.create_text((140,65),text="NOODLES",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Noodminiframe = Frame(Noodframe,bg='#DBD6CE',relief="ridge",bd="4")
Noodminiframe.place(x=25,y=200,height=300)

NoodleScrolly = Scrollbar(Noodminiframe,orient="vertical")

style.configure('Nood.Treeview',font=('times',15,'italic'),fieldbackground='#B6FFB0',foreground='black',
                background='#B6FFB0',rowheight=50)
style.configure('Nood.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#15B90A')
style.map('Nood.Treeview',background=[('selected','#2EAC63')],foreground=[('selected','white')])

Noodletab = Treeview(Noodminiframe,columns=('Menu','Price'),style='Nood.Treeview',yscrollcommand=NoodleScrolly.set)

NoodleScrolly.pack(side='right',fill='y',anchor=N)

NoodleScrolly.configure(command=Noodletab.yview)

Noodletab.column("#0",width=0,stretch=NO)
Noodletab.column("Menu",width=300)
Noodletab.column("Price",width=100,anchor=CENTER)

Noodletab.heading('#0',text="")
Noodletab.heading('Menu',text="MENU")
Noodletab.heading('Price',text="PRICE")

Noodletab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'noodles';")
data = mycursor.fetchall()
for i in data:
    Noodletab.insert('',END,values=(i[0],i[1]))


def on_Nod_select(event):
    a = Noodletab.focus()
    value = Noodletab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Noodletab.bind('<Double-1>',on_Nod_select)

## Sandwich's  Frame
SandWframe = Frame(root,bg='#E6D1A4',relief="ridge",bd="4")
SandWframe.place(x=474,y=0,relheight=1,width=474)

Sandbg = PhotoImage(file="./assets/SandBackGImg.png")
Sandbg = Sandbg.subsample(1,1)

SandCan = Canvas(SandWframe)
SandCan.place(x=0,y=0,relwidth=1,relheight=1)

SandCan.create_image((0,0),image=Sandbg,anchor=NW)
SandCan.create_text((100,80),text="SANDWICH'S",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Sandminiframe = Frame(SandWframe,bg='#E6D1A4',relief="ridge",bd="4")
Sandminiframe.place(x=20,y=200,height=300)

SandWScrolly = Scrollbar(Sandminiframe,orient="vertical")

style.configure('Sand.Treeview',font=('times',15,'italic'),fieldbackground='#E6D1A4',foreground='black',
                background='#E6D1A4',rowheight=50)
style.configure('Sand.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#CB8A4D')
style.map('Sand.Treeview',background=[('selected','#9E3D12')],foreground=[('selected','white')])

SandWtab = Treeview(Sandminiframe,columns=('Menu','Price'),style='Sand.Treeview',yscrollcommand=SandWScrolly.set)

SandWScrolly.pack(side='right',fill='y',anchor=N)

SandWScrolly.configure(command=Noodletab.yview)

SandWtab.column("#0",width=0,stretch=NO)
SandWtab.column("Menu",width=300)
SandWtab.column("Price",width=100,anchor=CENTER)

SandWtab.heading('#0',text="")
SandWtab.heading('Menu',text="MENU")
SandWtab.heading('Price',text="PRICE")

SandWtab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'sandwiches';")
data = mycursor.fetchall()
for i in data:
    SandWtab.insert('',END,values=(i[0],i[1]))


def on_Sand_select(event):
    a = SandWtab.focus()
    value = SandWtab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


SandWtab.bind('<Double-1>',on_Sand_select)

## Salad's  Frame
Saladframe = Frame(root,bg='#E6D1A4',relief="ridge",bd="4")
Saladframe.place(x=474,y=0,relheight=1,width=474)

Saladbg = PhotoImage(file="./assets/saladFrameBg.png")
Saladbg = Saladbg.subsample(1,1)

SaladCan = Canvas(Saladframe)
SaladCan.place(x=0,y=0,relwidth=1,relheight=1)

SaladCan.create_image((0,0),image=Saladbg,anchor=NW)
SaladCan.create_text((160,80),text="Salad'S",font=('Chiller',50,'bold'),fill='white',anchor=NW)

Saladminiframe = Frame(Saladframe,bg='#E6D1A4',relief="ridge",bd="4")
Saladminiframe.place(x=20,y=200,height=300)

SaladScrolly = Scrollbar(Saladminiframe,orient="vertical")

style.configure('Salad.Treeview',font=('times',15,'italic'),fieldbackground='#C3D7BB',foreground='black',
                background='#C3D7BB',rowheight=50)
style.configure('Salad.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#586E1B')
style.map('Salad.Treeview',background=[('selected','#78E8B7')],foreground=[('selected','blue')])

Saladtab = Treeview(Saladminiframe,columns=('Menu','Price'),style='Salad.Treeview',yscrollcommand=SaladScrolly.set)

SaladScrolly.pack(side='right',fill='y',anchor=N)

SaladScrolly.configure(command=Noodletab.yview)

Saladtab.column("#0",width=0,stretch=NO)
Saladtab.column("Menu",width=300)
Saladtab.column("Price",width=100,anchor=CENTER)

Saladtab.heading('#0',text="")
Saladtab.heading('Menu',text="MENU")
Saladtab.heading('Price',text="PRICE")

Saladtab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'salad';")
data = mycursor.fetchall()
for i in data:
    Saladtab.insert('',END,values=(i[0],i[1]))


def on_Salad_select(event):
    a = Saladtab.focus()
    value = Saladtab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Saladtab.bind('<Double-1>',on_Salad_select)

## Main Course  Frame
MainCoframe = Frame(root,bg='#810322',relief="ridge",bd="4")
MainCoframe.place(x=474,y=0,relheight=1,width=474)

Mainbg = PhotoImage(file="./assets/MainCorseFrameBg.png")
Mainbg = Mainbg.subsample(1,1)

MainCan = Canvas(MainCoframe)
MainCan.place(x=0,y=0,relwidth=1,relheight=1)

MainCan.create_image((0,0),image=Mainbg,anchor=NW)
MainCan.create_text((100,80),text="Main Course",font=('Chiller',50,'bold'),fill='white',anchor=NW)

MainCominiframe = Frame(MainCoframe,bg='#810322',relief="ridge",bd="4")
MainCominiframe.place(x=20,y=200,height=300)

MainCoScrolly = Scrollbar(MainCominiframe,orient="vertical")

style.configure('Main.Treeview',font=('times',15,'italic'),fieldbackground='#FF8173',foreground='black',
                background='#FF8173',rowheight=50)
style.configure('Main.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#C72319')
style.map('Main.Treeview',background=[('selected','#C72319')],foreground=[('selected','white')])

MainCotab = Treeview(MainCominiframe,columns=('Menu','Price'),style='Main.Treeview',yscrollcommand=MainCoScrolly.set)

MainCoScrolly.pack(side='right',fill='y',anchor=N)

MainCoScrolly.configure(command=MainCotab.yview)

MainCotab.column("#0",width=0,stretch=NO)
MainCotab.column("Menu",width=300)
MainCotab.column("Price",width=100,anchor=CENTER)

MainCotab.heading('#0',text="")
MainCotab.heading('Menu',text="MENU")
MainCotab.heading('Price',text="PRICE")

MainCotab.pack(fill='both')

mycursor.execute("select Menu ,Price from food where Catagories = 'main_course';")
data = mycursor.fetchall()
for i in data:
    MainCotab.insert('',END,values=(i[0],i[1]))


def on_Sand_select(event):
    a = MainCotab.focus()
    value = MainCotab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


MainCotab.bind('<Double-1>',on_Sand_select)

## BILL FRAME

M3frame = Frame(root,bg='#A47E52',relief="ridge",bd="4")
M3frame.place(x=0,y=0,relheight=1,width=474)

Billbg = PhotoImage(file="./assets/BillBackImg.png")
Billbg = Billbg.subsample(1,1)

BillTitlImg = PhotoImage(file="./assets/Bill.png")
BillTitlImg = BillTitlImg.subsample(4,4)

BillCan = Canvas(M3frame)
BillCan.place(x=0,y=0,relwidth=1,relheight=1)

BillCan.create_image((0,0),image=Billbg,anchor=NW)

BillCan.create_image((80,60),image=BillTitlImg,anchor=NW)
BillCan.create_text((130,70),text="Bill Board",font=('Courier New',30,'italic bold'),fill='brown',anchor=NW)

BillBominiframe = Frame(M3frame,bg='#D3B27F',relief="ridge",bd="2")
BillBominiframe.place(x=35,y=150,height=400,width=400)

Bill_Lab = Label(BillBominiframe,text='Nitin\'s Kitchen',bg='white',font=('Chiller',15,'bold underline'),fg='red')
Bill_Lab.place(x=0,y=0,relwidth=1)

BillArea = Text(BillBominiframe,font=('Courier New',9,'italic bold'),relief="flat")
BillArea.place(x=0,y=30,height=365,relwidth=1)
BillArea.insert(1.0,'\t\t\tCash Bill')

BillArea.insert(END,'\n\n   Bill No:' + str(bill_no))
date = time.strftime("%d/%m/%y")
BillArea.insert(END,'\t\t\t\t\t Date:' + date)
BillArea.insert(END,'\n  ____________________________________________________')
BillArea.insert(END,'\n   ITEM\t\t\t\tPRICE\tQTY\t TOTAL')
BillArea.insert(END,'\n  ____________________________________________________ \n')


def Generate_billFun():
    global order,bill_no,user,Grand_total
    try:
        con=mc.connect(host='localhost',user='root',password='dav123')
        mycursor=con.cursor()
        mycursor.execute('use hotel')
        mycursor.execute('INSERT INTO customer_order(Order_Id,room_no,Total_amt,Employee_Id) values(%s,%s ,%s ,%s)',(bill_no,roomNoForOrder.get(),Grand_total,user))
        order[bill_no]=[]
        BillAddMorBut.config(state = 'disabled')
        BillCancelBut.config(text='Back',bg = 'green')


    except:
        messagebox.showerror("Warning","Failed to add to DataBase",parent=root)

    BillArea.insert(END,'\n  ____________________________________________________')
    BillArea.insert(END,f'\n   Grand Total\t\t\t\t\t\t{Grand_total}\n')
    BillArea.insert(END,'  ____________________________________________________ ')
    BillArea.insert(END,'\n\n\t  THANK YOU... VISIT AGAIN !!!')


BillBut = Button(M3frame,text="Generate Bill",font=('Georgia',12,'bold'),fg='white',bg='#A47E52',bd=4,
                 command=Generate_billFun)
BillBut.place(x=45,y=570)


def Addmoreitem():
    BillArea.delete(BillPrintLine + 1,END)
    Mframe.tkraise()


BillAddMorBut = Button(M3frame,text="Add More",font=('Georgia',12,'bold'),fg='white',bg='#A47E52',bd=4,
                       command=Addmoreitem)
BillAddMorBut.place(x=200,y=570)

def cancelOrder():
    global order ,Grand_total ,roomNoForOrder
    BillArea.delete(7.0,END)
    order[bill_no] = []
    Grand_total = 0
    roomNo.configure(state='normal')
    roomNoForOrder.set('')
    Mframe.tkraise()
    BillAddMorBut.config(state='normal')
    BillCancelBut.config(text = 'Cancel',bg='red')


BillCancelBut = Button(M3frame,text="Cancel",font=('Georgia',12,'bold'),fg='white',bg='red',bd=4,
                       command=cancelOrder)
BillCancelBut.place(x=340,y=570)

# Login Page
loginFrame = Frame(root,bd =3,bg='lightgreen',relief = 'ridge')
loginFrame.place(x=0,y=0,relheight=1,width=474)


logBg = PhotoImage(file='./assets/logInBg.png')
logBg = logBg.subsample(2,2)

can = Canvas(loginFrame)
can.place(x=0,y=0,relwidth = 1 ,relheight = 1)

can.create_image(0,0,image = logBg ,anchor = 'nw')


Hotel_Title = Label(can,bg='#5B0200',fg = 'white',text= 'LOGIN',font=('Courier New',20,'italic bold'),relief="ridge",bd="4",compound ='left')
Hotel_Title.place(x=10,y=10,height=60,width=450)

usernameimg = PhotoImage(file='./assets/User.png')
usernameimg = usernameimg.subsample(1, 1)

passwordimg = PhotoImage(file='./assets/pass.png')
passwordimg = passwordimg.subsample(1, 1)


can.create_image((80,273),image = usernameimg,anchor = 'nw')
can.create_text((145,285),text = "User ID :",font=('times', 15, ' bold'),fill ='white')

can.create_image((80,356),image = passwordimg  ,anchor = 'nw')
can.create_text((155,366),text = "Password :",font=('times', 15, ' bold'),fill ='white')

#Login Entry Boxes
username = StringVar()
password = StringVar()

usernameEntry = Entry(loginFrame, textvariable=username, width=15, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
usernameEntry.place(x=215, y=270)
usernameEntry.focus()

passwordEntry = Entry(loginFrame, width=15, show='*', textvariable=password, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
passwordEntry.place(x=215, y=350)

def loginbtnfunc():
    global user,passw,Admin_name,con,mycursor
    user=username.get()
    passw=password.get()
    if (user == "" or passw == ""):
        messagebox.showinfo("Notification","All fields are required",parent=root)
    elif (len(passw) < 8):
        messagebox.showerror("Notification","Password Must be of 8 Characters!!!",parent=root)
    else:
        try:
            con=mc.connect(host='localhost',user='root',password='dav123')
            mycursor=con.cursor()
            query='use hotel;'
            mycursor.execute(query)
            query='select * from employee where Employee_Id =%s and password=%s;'
            t=mycursor.execute(query,(user,passw))
            if (t == True):
                HomeFrame.tkraise()
                data=mycursor.execute("select Employee_Name from employee where Employee_Id=%s;",(user))
                data=mycursor.fetchall()
                for i in data:
                    Admin_name=i[0]
                    print(Admin_name)

            else:
                messagebox.showerror('Notification','Incorrect Username or Password!!!\nPlease try again...',
                                     parent=root)

        except:
            print(traceback.format_exc())
            messagebox.showerror('Notification','Something is wrong!!!\nPlease try again...',parent=root)
            return

#Login Submit Button
loginbtn = Button(loginFrame, text='Login', font=('Courier New', 14, 'italic bold'),fg ='#FAFAFA', bg='#E9411E', bd=3, activebackground='#6D93B1',
                  activeforeground='white', command=loginbtnfunc ,width = 8 )
loginbtn.place(x=300, y=410)

#################### Home PAGE

HomeFrameBGimg = PhotoImage(file='./assets/logBg.png')
HomeFrameBGimg = HomeFrameBGimg.subsample(1, 1)

HomeFrame = Frame(root,bd =3,bg= 'orange')
HomeFrame.place(x=0,y=0,relheight=1,width=474)

HomeFrameCan = Canvas(HomeFrame)
HomeFrameCan.place(x=0,y=0,relwidth=1,relheight=1)

Hotel_Titleimg = PhotoImage(file='./assets/sasuke.png')
Hotel_Titleimg = Hotel_Titleimg.subsample(1, 1)

Hotel_Title = Label(HomeFrameCan,bg='#D8250E',image = Hotel_Titleimg,fg = 'white',text= 'Uchiha  Hotel',font=('chiller',30,'italic bold'),relief="ridge",bd="4",compound ='left')
Hotel_Title.place(x=10,y=10,height=75,width=450)


HomeFrameCan.create_image((0,0),image=HomeFrameBGimg,anchor=NW)

def bookRoomFrameRaise():
    root.geometry("948x660+220+20")
    RoomFrame.tkraise()

RoomBtnimg = PhotoImage(file='./assets/Room.png')
RoomBtnimg = RoomBtnimg.subsample(2, 2)


RoomBook = Button(HomeFrame,image = RoomBtnimg, text='BooK Room', font=('Courier New', 16, 'italic bold') ,fg ='white', bg='#F45430', bd=4, activebackground='#6D93B1',
                  activeforeground='white', command=bookRoomFrameRaise ,width = 150,compound='top',height=140 )
RoomBook.place(x=150, y=100)

FoodBtnimg = PhotoImage(file='./assets/Food.png')
FoodBtnimg = FoodBtnimg.subsample(2, 2)

orderFoodBtn = Button(HomeFrame,image = FoodBtnimg ,text=' Order Food', font=('Courier New', 16, 'italic bold'),fg ='white', bg='#F45430', bd=4, activebackground='#6D93B1',
                  activeforeground='white', command=lambda:Mframe.tkraise(),width = 150,compound='top',height=140 )
orderFoodBtn.place(x=150, y=290)

CheckOutBtnimg = PhotoImage(file='./assets/checkout.png')
CheckOutBtnimg = CheckOutBtnimg.subsample(5,5)

CheckOutBtn = Button(HomeFrame,image = CheckOutBtnimg ,text='CHECK OUT', font=('Courier New', 16, 'italic bold'),fg ='white', bg='#F45430', bd=4, activebackground='#6D93B1',
                  activeforeground='white', command=lambda:RoomCheckOutFrame.tkraise(),width = 150,compound='top',height=140 )
CheckOutBtn.place(x=150, y=480)

# HomeFrameCan.create_text((20,600),text=f"User : {user}",font=('Courier New',14,'bold'),fill='white',anchor=NW)


#### ROOM Frame

RoomFrame = Frame(root,bd =2)
RoomFrame.place(x=0,y=0,relheight=1,width=948)

RoomAvlbFrame = Frame(RoomFrame,bd =2,bg='lightyellow')
RoomAvlbFrame.place(x=0,y=0,relheight=1,width=474)


chkOuFrameCan = Canvas(RoomAvlbFrame,bd =3,relief = 'ridge')
chkOuFrameCan.place(x=0,y=0,relwidth=1,relheight=1)

bg = PhotoImage(file = "./assets/logInBg1.png")

chkOuFrameCan.create_image((0,0),image=bg,anchor=NW)

kak = PhotoImage(file='./assets/kakashi.png')
kak = kak.subsample(1,1)

Book_Title = Label(RoomAvlbFrame,image = kak,bg='#BA2127',fg = 'white',text= "Available Room's",font=('Courier New',22,'italic bold'),relief="ridge",bd="4",compound ='left')
Book_Title.place(x=10,y=10,height=60,width=450)

avlbTableframe = Frame(RoomAvlbFrame,bg='white',relief="ridge",bd="4")
avlbTableframe.place(x=20,y=120,height=450)

# Startilt_Lab = Label(Startframe,image = TitleImg,text = "STARTER",bg = '#232731',fg= 'red',font = ('Chiller', 50,'bold'),compound ='left')
# Startilt_Lab.place(x=90,y=50)

avlbTableScrolly = Scrollbar(avlbTableframe,orient="vertical")

style = ttk.Style()
style.theme_use('clam')
style.configure('Start.Treeview',font=('times',15,'italic'),fieldbackground='white',foreground='green',
                background='white',rowheight=50)
style.configure('Start.Treeview.Heading',font=('Courier New',12,'bold'),foreground='chocolate',background='lightgray')
style.map('Start.Treeview',background=[('selected','green')],foreground=[('selected','white')])

avlbTable = Treeview(avlbTableframe,columns=('Room_no','Room_price', 'Available'),style="Start.Treeview",yscrollcommand=avlbTableScrolly.set)

avlbTableScrolly.pack(side='right',fill='y',anchor=N)

avlbTableScrolly.configure(command=avlbTable.yview)

avlbTable.column("#0",width=0,stretch=NO)
avlbTable.column("Room_no",width=100,anchor=CENTER)
avlbTable.column("Room_price",width=130,anchor=CENTER)
avlbTable.column("Available",width=170,anchor=CENTER)

avlbTable.heading('#0',text="")
avlbTable.heading('Room_no',text="Room No.")
avlbTable.heading('Room_price',text="Room Price")
avlbTable.heading('Available',text="Availablility")

avlbTable.pack(fill='both')

con = mc.connect(host="localhost",user='root',password='dav123')
mycursor = con.cursor()
query = "use Hotel;"
mycursor.execute(query)

mycursor.execute("select room_No ,room_price,room_status from room ;")
data = mycursor.fetchall()
for i in data:
    avlbTable.insert('',END,values=(i[0],i[1],i[2]))


BookRoomFrame = Frame(RoomFrame)
BookRoomFrame.place(x=474,y=0,relheight=1,width=472)

BookRoomFrameCan = Canvas(BookRoomFrame,bd =3,relief = 'ridge')
BookRoomFrameCan.place(x=0,y=0,relwidth=1,relheight=1)


signCheck = PhotoImage(file='./assets/Nsign.png')
signCheck = signCheck.subsample(1,1)

Book_Title = Label(BookRoomFrameCan,image = signCheck,bg='#2D568C',fg = 'white',text= 'Book Room',font=('Courier New',25,'italic bold'),relief="ridge",bd="4",compound ='left')
Book_Title.place(x=10,y=10,height=75,width=450)


guestBG = PhotoImage(file='./assets/guestBG.png')
guestBG = guestBG.subsample(4,4)

BookRoomFrameCan.create_image((0,0),image=guestBG,anchor=NW)

Home_Button = Button(BookRoomFrameCan,image=Home_Buttonimg,command=backHomeFun,bd="4")
Home_Button.place(x=410,y=25)

roomno = IntVar()
BookRoomFrameCan.create_text((40,150),text="Room No:",font=('Courier New',14,'bold'),fill='black',anchor=NW)

roomnoEntry = Entry(BookRoomFrameCan, textvariable=roomno, width=10, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
roomnoEntry.place(x=140, y=150)
roomnoEntry.focus()
roomnoEntry.delete(0,END)

BookRoomFrameCan.create_text((40,220),text="Name:",font=('Courier New',14,'bold'),fill='black',anchor=NW)
Guest_NameVar = StringVar()
GuestName = Entry(BookRoomFrameCan, width=20, textvariable=Guest_NameVar, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
GuestName.place(x=140, y=220)


BookRoomFrameCan.create_text((40,290),text="Email:",font=('Courier New',14,'bold'),fill='black',anchor=NW)
GuestEmailVar = StringVar()
GuestEmail = Entry(BookRoomFrameCan, width=20, textvariable=GuestEmailVar, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
GuestEmail.place(x=140, y=290)

BookRoomFrameCan.create_text((40,360),text="Phone:",font=('Courier New',14,'bold'),fill='black',anchor=NW)
GuestPhoneNo = StringVar()
GuestPhone = Entry(BookRoomFrameCan, width=20, textvariable=GuestPhoneNo, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
GuestPhone.place(x=140, y=360)

BookRoomFrameCan.create_text((40,430),text="Aadhar No:",font=('Courier New',14,'bold'),fill='black',anchor=NW)
GuestAdharIdVar = StringVar()
GuestAdharId = Entry(BookRoomFrameCan, width=20,textvariable=GuestAdharIdVar, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
GuestAdharId.place(x=150, y=430)

chekInBtnIco = PhotoImage(file="./assets/chekInBtnIco.png")
chekInBtnIco = chekInBtnIco.subsample(1,1)

def clearRoomBooKInp():
    roomno.set('')
    Guest_NameVar.set('')
    GuestPhoneNo.set('')
    GuestAdharIdVar.set('')

def Book_ROOM_Btn_SubFun():
    if(roomno.get() == '' or Guest_NameVar.get() == '' or GuestPhoneNo.get() == '' or GuestAdharIdVar.get() == ''):
        messagebox.showwarning('Warning','Some Field is Empty !!!',parent =root)
    elif(type(roomno.get()) != int):
        messagebox.showwarning('Warning','No Room Available !!!',parent=root)
    elif(len(GuestPhoneNo.get()) != 10 ):
        messagebox.showwarning('Warning','Phone Number must be 10 digit !!!',parent=root)
    elif(len(GuestAdharIdVar.get()) != 12):
        messagebox.showwarning('Warning','AAdhar Number must be 12 digit !!!',parent = root)
    else:
        connecttodataBase()
        mycursor.execute("select * from room where room_no = %s AND room_status = 'AVAILABLE'",(roomno.get()))
        data = mycursor.fetchall()
        if(data):
            r = mycursor.execute("insert into guest(room_no,guest_name,guest_email,guest_phone,	guest_Id) values(%s,%s,%s,%s,%s);",(roomno.get(),Guest_NameVar.get(),GuestEmailVar.get(),GuestPhoneNo.get(),GuestAdharIdVar.get()))
            if(r):
                mycursor.execute("update room set room_status = 'BOOKED' where room_no = %s ",(roomno.get()))
                messagebox.showinfo('Information',f'Room Is Checked in !!!\n Room No : {roomno.get()} \n Guest Name : {Guest_NameVar.get()} \n\t Thank You ....',
                                 parent=root)
                clearRoomBooKInp()
        else:
            mycursor.execute('select room_status from room where room_no = %s ',(roomno.get()))
            r = mycursor.fetchall()
            for i  in r:
                print(i[0])
                messagebox.showwarning('Warning',f'Room is Already {i[0]}',parent = root)
                roomno.set('')

Book_ROOM_Button = Button(BookRoomFrameCan,image=chekInBtnIco,text ='CHECK IN ' ,command=Book_ROOM_Btn_SubFun,bd="4",font=('Courier New', 14, 'bold'),
                          compound = 'left' ,fg = 'white',bg ='#1872E1')
Book_ROOM_Button.place(x=300,y=580)

###########################   Checked OUT Section Frame   ####################

RoomCheckOutFrame = Frame(root)
RoomCheckOutFrame.place(x=0,y=0,relheight=1,width=474)

chkOutRoomFrameCan = Canvas(RoomCheckOutFrame,bd =3,relief = 'ridge')
chkOutRoomFrameCan.place(x=0,y=0,relwidth=1,relheight=1)


chkimg1 = PhotoImage(file='./assets/goat.png')
chkimg1 = chkimg1.subsample(1,1)

chkOutRoomFrameCan.create_image((0,0),image=chkimg1,anchor=NW)

nar = PhotoImage(file='./assets/nar.png')
nar = nar.subsample(1,1)

Hotel_Title = Label(chkOutRoomFrameCan,bg='#B58510',image = nar,fg = 'white',text= 'Checkout',font=('Courier New',25,'italic bold'),relief="ridge",bd="4",compound ='left')
Hotel_Title.place(x=10,y=10,height=75,width=450)


# chkOutRoomFrameCan.create_text((150,30),text="CHECK  OUT",font=('Courier New',23,'bold'),fill='red',anchor=NW)


Hotel_Title = Label(chkOutRoomFrameCan,bg='#170B10',fg = 'white',text= ' Room No:',font=('Courier New',15,'italic bold'))
Hotel_Title.place(x=28,y=100)

# chkOutRoomFrameCan.create_text((30,100),text="Room No :",font=('Courier New',15,'bold'),fill='hotpink',anchor=NW)

chkOutroomno = IntVar()

roomnoEntry = Entry(chkOutRoomFrameCan, textvariable=chkOutroomno, width=10, font=('Courier New', 14, 'italic'), bd=3, bg='white',relief = 'groove')
roomnoEntry.place(x=140, y=99)
roomnoEntry.focus()
roomnoEntry.delete(0,END)

checkOutPayment = 0
def getGuestDetail():
    global checkOutPayment
    try:
        connecttodataBase()
        mycursor.execute(
            'SELECT guest_name ,guest_phone,guest_Id,room_no ,guest_ChekIn_date FROM guest where room_no = %s ',
            (chkOutroomno.get()))
        data=mycursor.fetchall()

        PayArea.tag_configure("blue",font=('Courier New',13,'italic bold'),foreground="blue")
        PayArea.tag_configure("gray",foreground="gray")

        if (data):

            for i in data:
                PayArea.insert(END,'\n\n   Name :',"gray")
                PayArea.insert(END,f'\t\t\t{i[0]}\n')
                PayArea.insert(END,'\n   Phone :',"gray")
                PayArea.insert(END,f'\t\t\t{i[1]}\n')
                PayArea.insert(END,'\n   Id :',"gray")
                PayArea.insert(END,f'\t\t\t{i[2]}\n')
                PayArea.insert(END,'\n   Room No :',"gray")
                PayArea.insert(END,f'\t\t\t{i[3]}\n')
                y,m,d=((str(i[4]).split(' '))[0]).split('-')
                PayArea.insert(END,'\n   Date Of Check In :',"gray")
                PayArea.insert(END,f'\t\t\t{d}/{m}/{y}\n')

            PayArea.tag_configure("red",foreground="red")
            PayArea.insert(END,'\n\n\t\t\tROOM BILL ',"blue")
            PayArea.insert(END,
                           '\n  --------------------------------------------------------------------------------------------- ',
                           "red")
            PayArea.insert(END,'\n\t')
            mycursor.execute('SELECT room_price FROM room where room_no = %s ',
                             (chkOutroomno.get()))
            price=mycursor.fetchall()
            PayArea.insert(END,f'\n   Room Price Per Day\t\t\t\t\t\t{price[0][0]}',"gray")

            mycursor.execute(
                f'select DATEDIFF(CURRENT_TIMESTAMP(),(select guest_ChekIn_date from guest where room_no = %s))',
                (chkOutroomno.get()))
            day=mycursor.fetchall()
            PayArea.insert(END,f'\n   Total No Of Days\t\t\t\t\t\t{day[0][0] + 1}',"gray")
            roomtotalBill=(day[0][0] + 1)*price[0][0]
            PayArea.insert(END,f'\n\n   Room Total \t\t\t\t\t\t{roomtotalBill}')

            PayArea.insert(END,'\n  _____________________________________________________ \n',"gray")
            PayArea.insert(END,'\n\t\t\tFOOD BILL \n',"blue")
            PayArea.insert(END,'\n  Order Id\t\t\tDate\t\tAmount ',"red")
            PayArea.insert(END,
                           '\n  --------------------------------------------------------------------------------------------- ',
                           "red")
            mycursor.execute(f"select Order_Id ,Date ,Total_amt from customer_order where room_no = %s AND Bill_Status = 'PENDING' ",
                             (chkOutroomno.get()))
            order=mycursor.fetchall()
            foodTotalBill=0
            for i in order:
                y,m,d=((str(i[1]).split(' '))[0]).split('-')
                foodTotalBill+=int(i[2])
                PayArea.insert(END,f'\n  {i[0]}\t\t\t{d}/{m}/{y}\t\t{i[2]} \n',"gray")

            PayArea.insert(END,f'\n\n   food Total \t\t\t\t\t\t{foodTotalBill}')

            PayArea.insert(END,'\n  _____________________________________________________ \n',"gray")
            PayArea.insert(END,f'\n\n  Grand Total : ',"blue")

            checkOutPayment = roomtotalBill + foodTotalBill
            PayArea.insert(END,f'\t\t\t\t\t\t{roomtotalBill + foodTotalBill}\n',"blue")
            PayArea.insert(END,
                           '\n  --------------------------------------------------------------------------------------------- ',
                           "gray")
            PayArea.insert(END,'\n\n\t  THANK YOU... VISIT AGAIN !!!',"red")

            chkout_Payment_Button.config(state='normal')
        else:
            messagebox.showinfo('Info',"No Room Found !!!",parent=root)
            chkOutroomno.set()
    except:
        pass
        # messagebox.showerror('ERROR',"Something Went Wrong !!!",parent=root)


def checkOutClr():
    PayArea.delete(4.0,END)

def checkOutBack():
    checkOutClr()
    root.geometry("474x660+500+20")
    HomeFrame.tkraise()


Home_Button=Button(chkOutRoomFrameCan,image=Home_Buttonimg,command=checkOutBack,bd="4")
Home_Button.place(x=410,y=25)

chkout_getUserDetail_Button = Button(chkOutRoomFrameCan,image=chekInBtnIco,text ='Get Detail' ,command=getGuestDetail,bd="3",font=('Courier New', 12, 'bold'),
                          compound = 'left' ,fg = 'white',bg ='#EB3812')
chkout_getUserDetail_Button.place(x=300,y=99)

chkoutminiframe = Frame(chkOutRoomFrameCan,bg='#D3B27F',relief="ridge",bd="2")
chkoutminiframe.place(x=35,y=150,height=400,width=400)

Bill_Lab = Label(chkoutminiframe,text='GUEST DETAIL',bg='white',font=('Chiller',15,'bold underline'),fg='red')
Bill_Lab.place(x=0,y=0,relwidth=1)

PayArea = Text(chkoutminiframe,font=('Helvetica',10,'italic bold'),relief="flat" )
PayArea.place(x=0,y=30,height=365,relwidth=1)
date = time.strftime("%d/%m/%y")
PayArea.insert(END,'\n\t\t\t\t\tDate : ' + date)
# PayArea.insert(END,'\n  _____________________________________________________')



paybut = PhotoImage(file="./assets/pay.png")
paybut = paybut.subsample(2,2)

Paybg=PhotoImage(file="./assets/payBack.png")
Paybg=Paybg.subsample(1,1)

def PaymentFun():
    # try:
        Payroot=Toplevel()
        Payroot.geometry("500x340+500+200")
        Payroot.title("Payment")
        Payroot.resizable(False,False)

        PayCan=Canvas(Payroot,relief="ridge",bd=4,bg = 'white')
        PayCan.place(x=0,y=0,relwidth=1,relheight=1)

        PayCan.create_image((180,0),image=Paybg,anchor=NW)
        PayCan.create_text((250,22),text='PAYMENT',anchor=NW,font=('Georgia',16,'italic bold'),fill='orange')

        PayCan.create_text((70,107),text="Mode : ",anchor=NW,font=('Courier New',15,'italic bold'),fill='gray')
        modeval = StringVar()
        modeval.set("CASH")
        mode  = ttk.Combobox(PayCan, width = 20, textvariable = modeval,font=('',13,'italic bold'))
        mode['values'] = ("CASH","DEBIT CARD","UPI")
        mode.place(x=170,y=103)

        PayCan.create_text((70,160),text='Room No :',anchor=NW,font=('Georgia',13,'bold'),fill='gray')
        PayCan.create_text((170,160),text=chkOutroomno.get(),anchor=NW,font=('',14,'bold'),fill='green')
        PayCan.create_text((70,220),text="Amount : ",anchor=NW,font=('Georgia',13,'bold'),fill='gray')
        PayCan.create_text((170,220),text = checkOutPayment ,anchor=NW,font=('',14,'bold'),fill='green')


        def confirmPayButFun():
            global checkOutPayment
            connecttodataBase()
            res=mycursor.execute("UPDATE room set room_status ='AVAILABLE' WHERE room_No = %s",(chkOutroomno.get()))
            if (res):
                mycursor.execute("UPDATE customer_order set Bill_Status ='PAID' WHERE room_No = %s",
                                 (chkOutroomno.get()))
                mycursor.execute("UPDATE guest set guest_ChekOut_date = CURRENT_TIMESTAMP() WHERE room_No = %s",
                                 (chkOutroomno.get()))
                res = mycursor.execute("INSERT INTO  payment(mode ,room_no,Total_Amt) VALUES(%s,%s,%s)",
                                 (modeval.get(),chkOutroomno.get(),checkOutPayment))
                if(res):
                    messagebox.showinfo('INFO',"Payment SuccessFull !!!",parent=root)
                    chkOutroomno.set('')
                    PayArea.delete(4.0,END)
                    checkOutPayment = 0
                    Payroot.destroy()
                else:
                    Payroot.destroy()

        ConfPayBut=Button(PayCan,image=paybut,text=" Confirm Payment",bg='orange',fg='white',bd=5,font=('Georgia',12,'bold'),
                            command=confirmPayButFun,compound = 'left')
        ConfPayBut.place(x=210,y=270)
    # except:
    #     messagebox.showerror('ERROR',"Payment Failed !!!",parent=root)



chkout_Payment_Button = Button(chkOutRoomFrameCan,image=paybut,text =' PAYMENT ' ,command=PaymentFun,bd="3",font=('Courier New', 12, 'bold'),
                          compound = 'left' ,fg = 'black',bg ='lightblue',state = 'disabled')
chkout_Payment_Button.place(x=300,y=595)

loginFrame.tkraise()

root.mainloop()
