from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
import tkinter as tk
import datetime as dt
import brandlist
from time import strftime
from PIL import ImageTk, Image
from tkinter import *
from tkscrolledframe import ScrolledFrame
#-------------------------------------main window----------------------------------------
tasmac=Tk()
tasmac.title("TASMAC")
tasmac.geometry("600x400")
#------------------------------------menu bar-----------------------
menubar = Menu(tasmac)
tasmac.config(menu=menubar)
#-------------------------------------- create a menu----------------------
file_menu = Menu(menubar)
help_menu = Menu(menubar)
#------------------------------------file menu to menu bar------------
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Help",menu=help_menu)
#------------------------------------ add a menu item to the menu---------------
file_menu.add_command(label='Add',command="")
file_menu.add_command(label='Exit',command=tasmac.destroy)
#----------------------------------------frame layout-------------------------------------
#-----------------------------------------calculation-------------------------------------
#----------------------------------------column entries empty lists--------------------------------------
#to get all entry from tavle
entries = []   # received bottle entry list
entries2 = []  # sales bottle entry list
opbtentry120_var = []  # open bottle entry list
totentry120_var = []   # total entry list
clbtentry120_var = []  # close bottle entry list
clvlentry120_var = []  # close value entry list
slvlentry120_var = []  # sales vlaue entry list
slbtentry120_var = []  # slaes vlaue entry list
mrpentry120_var = []   # mrpentry list
"""opbtentry160_var = []  
totentry160_var = []
clbtentry160_var = []
clvlentry160_var = []
slvlentry160_var = []
slbtentry160_var = []
mrpentry160_var = []"""
#---------------------------------------------
class test:
    def getdata(self,entries,entries2,opbtentry,totentry,clbtentry,clvlentry,mrpentry,slvlentry
            ): # parameters<---aruguments passed from initaiting  class objects
        #self.total=entries
        self.entries=entries #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 3(recived bottle))
        self.entries2=entries2 #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 7(sales bottle bottle))
        self.opbtentry=opbtentry #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 1(open bottle bottle))
        self.totentry120=totentry #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 4(total bottle))
        self.clbtentry120=clbtentry #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 5(closing bottle))
        self.clvlentry=clvlentry #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 6(closing value))
        self.mrpentry = mrpentry #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 8(mrp))
        self.slvlentry=slvlentry #(assigning to self variable<----parameters<----argument from  initaiting class object<-----received entries list<----column 9(sales value))
        #above entries only get entry text box numbers eg:- frame--->notebook---->scrollframe--->entry,entry2,entry34,entry67.
    def calculate(self):
        self.receivedlist = [] #this list get user input values from entry box--->received bottle values
        self.salesbtlist = [] #this list get user input values from entry box--->sales bottle values
        self.totallist = [] # this list to add open bottle + recived bottle
        self.openbtlist = [] # this list to set values(open bottle) to entry box ----> column 1
        self.closebtlist = [] # this list to set values(close bottle) to entry column ----> column 5
        self.closevllist = [] # this list to set values(close value bottle) to entry column ----> column 6
        self.salesvllist = [] # this list to set values(open bottle) to entry column ----> column 9
        for entry in entries: # for loop to get entry values from list entries(received bottle) one by one
            self.received = entry.get() # geting user values using pre-defined function get() & stored in received variables
            self.receivedbt= int(self.received)  # converting each user data to integer & stored in receivedbt variable
            self.receivedlist.append(self.receivedbt) # appending each user data to receivedlist using pre-defined append() function
        for entry in entries2:# for loop to get entry values from list entries2(sales-bottle) one by one
            self.sales = entry.get() # geting user values using pre-defined function get() & stored in sales variables
            self.salesbt = int(self.sales)  # converting each user data to integer & stored in salesbt variable
            self.salesbtlist.append(self.salesbt) # appending each user data to salesbtlist using pre-defined append() function
            self.totallist = [sum(i) for i in zip(self.receivedlist, brandlist.ml180opbtlist)] # add two lists open bottle list & closed bottle lists
            #The sum() function adds list elements one by one using the index. And the zip() function groups the two list items together.
            self.closebtlist = [x2 - x1 for (x1, x2) in zip(self.salesbtlist, self.totallist)] # subtract salesbtlist & totlalist
#--------------------------------------------------------closebt variable & empty list declaretion--------------------------------------
#empty list variable to separate close bottle values we get from above calaculation (self.closebtlist)-->because we get mrp120,mrp140,mpr160 to single list
            self.ml180120clbt = []
            self.ml180140clbt = []
            self.ml180160clbt = []
            self.ml180120clvl = []
            self.ml180140clvl = []
            self.ml180160clvl = []
#-----------------------------------------------closebt list slicing----------------------------------------------
            self.ml180120clbt = self.closebtlist[:brandlist.ml180120len]# here we slicing list self.closelist using ml180-mrp120 length-->self.ml180120clbt
            self.ml180140clbtlen = brandlist.ml180120len + brandlist.ml180140len # here adding lenght ml180mrp120 + ml180mrp140-->self.ml180120clbt
            self.ml180140clbt = self.closebtlist[brandlist.ml180120len:self.ml180140clbtlen] # # here we slicing list self.closelist using ml180mrp120 b/w mrp120:mrp140 length-->self.ml180140clbt
            #self.ml180160clbtlen = brandlist.ml180120len + brandlist.ml180160len
            self.ml180160clbt = self.closebtlist[self.ml180140clbtlen:]#here we slicing list self.closlist using mrp120:mrp140 afterwards
#-----------------------------------------------close value calcuations------------------------------------------------\
            self.ml180120clvl = [i * 120 for i in self.ml180120clbt]# mrp120 close vlaues claculation (for i in list[items])
            self.ml180140clvl = [i * 140 for i in self.ml180140clbt]# mrp140 close vlaues claculation (for i in list[items])
            self.ml180160clvl = [i * 160 for i in self.ml180160clbt]# mrp160 close vlaues claculation (for i in list[items])
            self.closevllist = self.ml180120clvl.copy()#copying above calculated mrp120 to close value using copy() pre-defined fns-->closevllist
            self.closevllist.extend(self.ml180140clvl)#here extending mrp140 above close value list using extend() pre-defined fns--->closevllist
            self.closevllist.extend(self.ml180160clvl)#here extending mrp160 above close value list using extend() pre-defined fns--->closevllist
#---------------------------------------------sales bottle & its calculations-------------------------------------------
#--------------------------------------------sales bottle variable & its empty list declarations--------------
# empty list variable to separate close bottle values we get from above calaculation (self.closebtlist)-->because we get mrp120,mrp140,mpr160 in single list
            self.ml180120slbt = []
            self.ml180140slbt = []
            self.ml180160slbt = []
            self.ml180120slvl = []
            self.ml180140slvl = []
            self.ml180160slvl = []
#--------------------------------------------------slicing values in list salesbtlist-----------------------------------------
            self.ml180120slbt = self.salesbtlist[:brandlist.ml180120len]
            self.ml180140slbtlen = brandlist.ml180120len + brandlist.ml180140len
            self.ml180140slbt = self.salesbtlist[brandlist.ml180120len:self.ml180140clbtlen]
            # self.ml180160clbtlen = brandlist.ml180120len + brandlist.ml180160len
            self.ml180160clbt = self.salesbtlist[self.ml180140clbtlen:]
# --------------------------------sales---value calculations------------------------------------------------------------\
            self.ml180120slvl = [i * 120 for i in self.ml180120slbt]
            self.ml180140slvl = [i * 140 for i in self.ml180140slbt]
            self.ml180160slvl = [i * 160 for i in self.ml180160slbt]
            self.salesvllist = self.ml180120slvl.copy()
            self.salesvllist.extend(self.ml180140clvl)
            self.salesvllist.extend(self.ml180160clvl)
#----------------------------------------------------------------------

    def display(self):
        for x in range(brandlist.ml180listlen-1):#lenght of ml180 list total(mrp120,mrp140,mrp160)
            self.opbtentry[x+1].set(brandlist.ml180opbtlist[x])#(open bottle --->entry[x].set[x]
            self.totentry120[x+1].set(self.totallist[x])
            self.clbtentry120[x+1].set(self.closebtlist[x])
            self.clvlentry[x + 1].set(self.closevllist[x])
            self.slvlentry[x+1].set(self.salesvllist[x])
    def savelist(self):
        brandlist.opbtsalist = self.closebtlist[:]#copying whole list closebtlist---->opbtlist
#-------------------------------------------calculation end--------------------------------
wall=Frame(tasmac)
wall.pack(fill="both")
#----------------------------------------note book layout--------------------------------
tablayout=Notebook(wall,width=50, height=620)
#------------------------------------------scroll frame----------------------------------
#------------------------------------------tab1 starts-----------------------------------
scrolltab1 = ScrolledFrame(tablayout, width=20, height=40)
scrolltab1.pack(side="top", expand=1, fill="both")
#-------------------------------------------scroll display widget------------------------
tab1 = scrolltab1.display_widget(tk.Frame)
#-------------------------------------------tab1 body------------------------------------
#entry variable list box is bind to the entry box to store the value entered to the Entry widget
sno_var=[]
ml180mrp120bna_var=[]
ml180mrp120_ent=[]
ml180mrp120ent_var=[]
head_var=[]
temp=[]
ml180mrp120len=len(brandlist.ml180120)
headlen=len(brandlist.tableheadlist)
len120=ml180mrp120len+1
#-------------append entry variable to list using length----------
for i in range(brandlist.headlen):#here heading length is 10 --->append stringvar() 10 times --->head_var
    head_var.append(StringVar())#head_var = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
for i in range(brandlist.ml180listlen):
    sno_var.append(StringVar)
for i in range(brandlist.ml180listlen):
    ml180mrp120bna_var.append(StringVar())
for i in range(brandlist.ml180listlen):
    opbtentry120_var.append(IntVar())
#--------------------------------
for i in range(brandlist.ml180listlen):
    totentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    clbtentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    clvlentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    slvlentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    slbtentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    mrpentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    slvlentry120_var.append(IntVar())
for i in range(brandlist.ml180listlen):
    temp.append(0)
#-----------------------------------forloop for table constructions-------------------------------

for row in range(brandlist.ml180listlen):# row------>iteration variable
    for column in range(headlen):#column------------>iteration variavle
        if row == 0:
            for x in range(headlen):
                head_var[x].set(brandlist.tableheadlist[x])#column1-->heading1,column2-->heading2,column3-->heading3
            tabhead = Label(tab1, textvariable=head_var[column], bg="black", fg="white", padx=3, pady=3)
            tabhead.config(font=('Arial', 14))
            tabhead.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
        else:
            if column==1:#brandlist items
                for x in range(brandlist.ml180listlen):
                    ml180mrp120bna_var[x].set(brandlist.ml180list[x])
                bna = Label(tab1, textvariable=ml180mrp120bna_var[row], bg="white", fg="black", padx=3, pady=3,width=20)
                bna.config(font=('Arial', 14))
                bna.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column == 2:#open bottle items
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                openbten2 = Entry(tab1, textvariable=opbtentry120_var[row], state='readonly', **ENTRY_STYLES, width=10)
                openbten2.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==0:# serial numbers
                sno = Label(tab1, text=str(row), bg="black", fg="white", padx=3, pady=3,width=10)
                sno.config(font=('Arial', 14))
                sno.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==3:# recevied bottle
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                entry = IntVar()
                entry.set("0")
                rcbten3 = Entry(tab1, textvariable=entry, **ENTRY_STYLES, width=10)
                entries.append(rcbten3)
                rcbten3.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==7:#sales bottle
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                entry = IntVar()
                entry.set("0")
                slbten7 = Entry(tab1, textvariable=entry,**ENTRY_STYLES, width=10)
                entries2.append(slbten7)
                slbten7.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==4:#total bottle items
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                toten4= Entry(tab1, textvariable=totentry120_var[row],state='readonly', **ENTRY_STYLES, width=10)
                toten4.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==5:#close bottle items
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                clbten5= Entry(tab1, textvariable=clbtentry120_var[row],state='readonly', **ENTRY_STYLES, width=10)
                clbten5.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==6:#close value items
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                clvlen6= Entry(tab1, textvariable=clvlentry120_var[row],state='readonly', **ENTRY_STYLES, width=10)
                clvlen6.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column==8: #ml180----->mrps-->120,140,160
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                ml180mrp=[]#mrp empy list
            #using forloop to store mrp 120,140,160-->ml180mrp list according to lengths
                for x in range(brandlist.ml180120len):#here X--->iteration variables
                    ml180mrp.append(brandlist.mrplist[0])
                for x in range(brandlist.ml180140len):
                    ml180mrp.append(brandlist.mrplist[1])
                for x in range(brandlist.ml180160len):
                    ml180mrp.append(brandlist.mrplist[2])
            #using  mrp set values to the entry variables
                for x in range(brandlist.ml180listlen):
                    mrpentry120_var[x].set(ml180mrp[x])
                mrpen8= Entry(tab1, textvariable=mrpentry120_var[row],state='readonly', **ENTRY_STYLES, width=10)
                mrpen8.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            elif column == 9:
                ENTRY_STYLES = {"font": "verdana 14 bold"}
                slvlen9 = Entry(tab1, textvariable=slvlentry120_var[row], state='readonly', **ENTRY_STYLES, width=10)
                slvlen9.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
#--------------------------------------------tab1 body ends------------------------------
tablayout.add(scrolltab1,text="ML180")
#--------------------------------------------tab1 laypot end------------------------------

#----------------------------------------#tab2 starts--------------------------------------

#-------------------------------------------#scroll frame ---------------------------------
scrolltab2 = ScrolledFrame(tablayout, height=40)
scrolltab2.pack(side="top", expand=1, fill="both")
#------------------------------------------tab2 body---------------------------------------
tab1 = scrolltab2.display_widget(tk.Frame)
#-----------------------------------------180mlmrp120 entry------------------------------------

#-------------------------------- ----for 2------------------------------------------------------------
#-------------------------------------------------tab2 body end---------------------
#-----------------------------------------------tab2 scroll tab layout---------------
tablayout.add(scrolltab2,text="ML350")

tablayout.pack(fill="both")
#-----------------------------------------------binding arrow keys--------------------

scrolltab2.bind_arrow_keys(tablayout)
#----------------------------------------------binding wheels------------------------
scrolltab2.bind_scroll_wheel(tablayout)
#-------------------------------------------------------------------------------------
#-----------------------------------------------button function call------------------

def sentdata():
    obj = test() #class object declared
    obj.calculate() #class object initiated
    obj.getdata(entries,entries2,opbtentry120_var,totentry120_var,clbtentry120_var,clvlentry120_var,mrpentry120_var,slvlentry120_var)
    #argument passed using object to test class
    obj.display()
    #using class object---->invoke display method in class test
    obj.savelist()
    # using class object---->invoke savelist method in class test:--closelist--->openbtlist
#-------------------------------------------button---------------------------------------
button=Button(tasmac,text="Submit",command=sentdata).pack(side=RIGHT)
button1=Button(tasmac,text="Save",command=sentdata).pack(side=RIGHT)
#--------------------------------------main windows class-------------------------------
tasmac.mainloop()
