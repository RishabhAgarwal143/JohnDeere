#!/usr/local/bin/python3.7  
from tkinter import *
import json

Field_names = []
Field_deleted = []
Field_operation_name = ["Seeding","Spraying","Tillage","Harvest"]
Field_operation_deleted = []

Field_Field_operation_link = {}

def Main_screen():

    root = Tk()
    root.geometry("750x500")

    l0 = Label(root,text="Field Operation Tracking System",width=35,font =("arial",15,"bold") )
    l0.place(x = 200,y=50)

    l1 = Label(root,text="Field",width=20,font =("arial",10,"bold") )
    l1.place(x = 100,y=150)

    l2 = Label(root,text="Field Operartions",width=20,font =("arial",10,"bold") )
    l2.place(x = 100,y=200)

    l3 = Label(root,text="Field Assignments",width=20,font =("arial",10,"bold") )
    l3.place(x = 100,y=250)

    def buttonfunc1():

        root.destroy()
        Fields_screen_create()

    def buttonfunc2():

        root.destroy()
        Field_screen_update()

    def buttonfunc3():

        root.destroy()
        Field_screen_delete()

    def buttonfunc4():

        root.destroy()
        Fields_operation_screen_create()

    def buttonfunc5():

        root.destroy()
        Field_operation_screen_update()

    def buttonfunc6():

        root.destroy()
        Field_operation_screen_delete()

    def buttonfunc7():

        root.destroy()
        Field_operation_screen_restore()
    
    def buttonfunc8():

        root.destroy()
        Field_screen_restore()
    
    def buttonfunc9():

        root.destroy()
        Field_assignments()

    def buttonfunc10():

        root.destroy()
        Field_view()


    button_01 = Button(root, text='CREATE',command=buttonfunc1,relief= 'groove')
    button_01.place(x = 350 , y = 150)

    button_02 = Button(root, text='UPDATE', command=buttonfunc2,relief= 'groove')
    button_02.place(x = 450 , y = 150)

    button_03 = Button(root, text='DELETE', command=buttonfunc3,relief= 'groove')
    button_03.place(x = 550 , y = 150)


    button_04 = Button(root, text='CREATE', command=buttonfunc4,relief= 'groove')
    button_04.place(x = 350 , y = 200)

    button_05 = Button(root, text='UPDATE', command=buttonfunc5,relief= 'groove')
    button_05.place(x = 450 , y = 200)

    button_06 = Button(root, text='DELETE', command=buttonfunc6,relief= 'groove')
    button_06.place(x = 550 , y = 200)

    button_07 = Button(root, text='Restore Field operations', command=buttonfunc7,relief= 'groove')
    button_07.place(x = 400 , y = 400)

    button_08 = Button(root, text='Restore Fields', command=buttonfunc8,relief= 'groove')
    button_08.place(x = 250 , y = 400)

    button_09 = Button(root, text=' Field Assignments ', command=buttonfunc9,relief= 'groove')
    button_09.place(x = 350 , y = 250)

    button_10 = Button(root, text=' View Assignments ', command=buttonfunc10,relief= 'groove')
    button_10.place(x = 490 , y = 250)
    root.mainloop()


def Fields_screen_create():

    
    root1 = Tk()
    root1.geometry("500x500")

    var = StringVar()

    def getvar():
        
        x = var.get()
        root1.destroy()
        Field_storage(x)
        Main_screen()


    l1 = Label(root1,text="Field Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    entrylist1 = Entry(root1,textvar = var)
    entrylist1.place(x = 200,y=100)
    
    button_02 = Button(root1, text='ADD FIELD',command=getvar)
    button_02.place(x = 250 , y = 400)

    root1.mainloop


def Field_screen_update():
    
    global Field_names

    root2 = Tk()
    root2.geometry("500x500")
    
    var = StringVar()
    var.set(Field_names[0])

    var1 = StringVar()

    def get_var():

        x = var1.get()
        y = var.get()
        root2.destroy()
        Update_Field_Name(y,x)
        Main_screen()

    l1 = Label(root2,text="Field Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 50,y=100)

    l2 = Label(root2,text="New Field Name",width=30,font =("arial",10,"bold") )
    l2.place(x = 10,y=200)

    dropdown = OptionMenu(root2, var, *Field_names )
    dropdown.place(x = 250 , y =100)

    entrylist1 = Entry(root2,textvar = var1)
    entrylist1.place(x = 200,y=200)

    button = Button(root2, text='UPDATE', command=get_var)
    button.place(x = 250 , y = 400)

    root2.mainloop()
    




def Field_screen_delete():

    global Field_names

    root3 = Tk()
    root3.geometry("500x500")

    var = StringVar()
    var.set(Field_names[0])

    def get_var():

        x = var.get()
        Field_delete(x)
        root3.destroy()
        Main_screen()

    l1 = Label(root3,text="Field Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    dropdown = OptionMenu(root3, var, *Field_names)
    dropdown.place(x = 200 , y =100)

    button = Button(root3, text='DELETE', command=get_var)
    button.place(x = 250 , y = 400)


def Field_screen_restore():

    global Field_deleted
    root3 = Tk()
    root3.geometry("500x500")

    var = StringVar()
    var.set(Field_deleted[0])

    def get_var():

        x = var.get()
        Field_storage(x)
        root3.destroy()
        Main_screen()

    l1 = Label(root3,text="Field Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    dropdown = OptionMenu(root3, var, *Field_deleted )
    dropdown.place(x = 200 , y =100)

    button = Button(root3, text='Restore', command=get_var)
    button.place(x = 250 , y = 400)

def Field_storage(name):
    
    global Field_names
    global Field_Field_operation_link

    Field_names.append(name)
    Field_Field_operation_link['name'] = []

def Field_operation_storage(name):
    
    global Field_operation_name
    Field_operation_name.append(name)

def Field_delete(name):

    global Field_names
    global Field_deleted

    Field_deleted.append(name)
    Field_names.remove(name)
    del Field_Field_operation_link['name']

def Field_operation_delete(name):

    global Field_operation_name
    global Field_operation_deleted

    Field_operation_deleted.append(name)
    Field_operation_name.remove(name)


def printf():
    global Field_names
    print(Field_names)

def Fields_operation_screen_create():

    
    root1 = Tk()
    root1.geometry("500x500")

    var = StringVar()

    def getvar():
        
        x = var.get()
        root1.destroy()
        Field_operation_storage(x)
        Main_screen()


    l1 = Label(root1,text="Field  Operation Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    entrylist1 = Entry(root1,textvar = var)
    entrylist1.place(x = 200,y=100)
    
    button_02 = Button(root1, text='ADD FIELD', command=getvar)
    button_02.place(x = 250 , y = 400)

    root1.mainloop


def Field_operation_screen_update():
    
    global Field_operation_name

    root2 = Tk()
    root2.geometry("500x500")
    
    var = StringVar()
    var.set(Field_operation_name[0])

    var1 = StringVar()

    def get_var():

        x = var1.get()
        y = var.get()
        root2.destroy()
        Update_Field_operation_Name(y,x)
        Main_screen()

    l1 = Label(root2,text="Field Operation Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    l2 = Label(root2,text="New Field Operation Name",width=35,font =("arial",10,"bold") )
    l2.place(x = 10,y=200)

    dropdown = OptionMenu(root2, var, *Field_operation_name )
    dropdown.place(x = 200 , y =100)

    entrylist1 = Entry(root2,textvar = var1)
    entrylist1.place(x = 200,y=200)

    button = Button(root2, text='UPDATE', command=get_var)
    button.place(x = 250 , y = 400)

def Field_operation_screen_delete():

    global Field_operation_name

    root3 = Tk()
    root3.geometry("500x500")

    var = StringVar()
    var.set(Field_operation_name[0])

    def get_var():

        x = var.get()
        Field_operation_delete(x)
        root3.destroy()
        Main_screen()

    l1 = Label(root3,text="Field Operation Name",width=35,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    dropdown = OptionMenu(root3, var, *Field_operation_name )
    dropdown.place(x = 200 , y =100)

    button = Button(root3, text='DELETE', command=get_var)
    button.place(x = 250 , y = 400)


def Field_operation_screen_restore():

    global Field_operation_deleted
    root3 = Tk()
    root3.geometry("500x500")

    var = StringVar()
    var.set(Field_operation_deleted[0])

    def get_var():

        x = var.get()
        Field_operation_storage(x)
        root3.destroy()
        Main_screen()

    l1 = Label(root3,text="Field Operation Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 10,y=100)

    dropdown = OptionMenu(root3, var, *Field_operation_deleted )
    dropdown.place(x = 200 , y =100)

    button = Button(root3, text='Restore', command=get_var)
    button.place(x = 250 , y = 400)


def Field_assignments():

    global Field_names

    root2 = Tk()
    root2.geometry("500x500")
    
    var = StringVar()
    var.set(Field_names[0])

    var1 = IntVar()

    def get_var():

        x = var1.get()
        y = var.get()
        root2.destroy()
        Field_assignments_screen2(x,y)


    l1 = Label(root2,text="Field Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 100,y=100)

    l2 = Label(root2,text="Number of Assignments",width=20,font =("arial",10,"bold") )
    l2.place(x = 100,y=200)

    dropdown = OptionMenu(root2, var, *Field_names )
    dropdown.place(x = 300 , y =100)

    entrylist1 = Entry(root2,textvar = var1)
    entrylist1.place(x = 300,y=200)

    button = Button(root2, text='NEXT', command=get_var)
    button.place(x = 250 , y = 400)

def Field_assignments_screen2(num_assignments, f_name):

    global Field_operation_name

    root = Tk()
    root.geometry("500x500")

    labellist = ['l1','l2','l3','l4','l5','l6','l7','l8']
    entrylist = ['e1','e2','e3','e4','e5','e6','e7','e8']
    subjectlist = ['S1','S2','S3','S4','S5','S6','S7','S8']

    posx= 150
    posy = 100

    for i in range(num_assignments):

        subjectlist[i] = StringVar()
        subjectlist[i].set(Field_operation_name[i])

        labellist[i] = Label(root,text=("Field operator", i+1),width=20,font =("arial",10,"bold") )
        labellist[i].place(x = posx,y=posy)

        entrylist[i] = OptionMenu(root,subjectlist[i],*Field_operation_name)
        entrylist[i].place(x = posx + 150,y=posy)

        posy += 50

    def getvar():
        Subject = []
        for i in range(num_assignments):
            x = subjectlist[i].get()
            Subject.append(x)
        root.destroy()
        Dict_update(Subject,f_name)
        Main_screen()

    button_01 = Button(root, text='Next', command=getvar)
    button_01.place(x = 200 , y = 300)
    root.mainloop()

    
def Dict_update(Values, Key):

    global Field_Field_operation_link

    Field_Field_operation_link[Key] = Values

def Field_view():

    global Field_names

    root2 = Tk()
    root2.geometry("500x500")
    
    var = StringVar()
    var.set(Field_names[0])

    def get_var():

        y = var.get()
        root2.destroy()
        Field_view_screen2(y)

    l1 = Label(root2,text="Field Name",width=20,font =("arial",10,"bold") )
    l1.place(x = 100,y=100)

    dropdown = OptionMenu(root2, var, *Field_names )
    dropdown.place(x = 300 , y =100)

    button = Button(root2, text='Next', command=get_var)
    button.place(x = 200 , y = 300)
    root2.mainloop()


def Field_view_screen2(f_name):

    global Field_Field_operation_link

    root2 = Tk()
    root2.geometry("500x500")

    l = Label(root2,text = "Field Operator Assignments",width=25,font =("arial",10,"bold"))
    l.place(x =150, y= 50)

    posx = 100
    posy = 100
    
    for i in range(len(Field_Field_operation_link[f_name])):

        l1 = Label(root2,text = Field_Field_operation_link[f_name][i],width=20,font =("arial",10,"bold") )
        l1.place(x = posx+200, y= posy)

        labellist2 = Label(root2,text=("Field operator ", i+1),width=20,font =("arial",10,"bold") )
        labellist2.place(x = posx,y=posy)

        posy += 50

    def get_var():

        root2.destroy()
        Main_screen()

    button = Button(root2, text='Next', command=get_var)
    button.place(x = 200 , y = 300)
    root2.mainloop()

def Update_Field_Name(Odd_name, new_name):

    global Field_names
    global Field_Field_operation_link

    for i in range(len(Field_names)):
        if (Field_names[i] == Odd_name):
            Field_names[i] = new_name

    if(Odd_name in Field_Field_operation_link):
        Field_Field_operation_link[new_name] = Field_Field_operation_link.pop(Odd_name)
    

    
def Update_Field_operation_Name(Odd_name,new_name):

    global Field_operation_name
    for i in range(len(Field_operation_name)):

        
        if (Field_operation_name[i] == Odd_name):
            Field_operation_name[i] = new_name
    
    for i in Field_Field_operation_link:
        for j in range (len(Field_Field_operation_link[i])):
            if Field_Field_operation_link[i][j] == Odd_name:
                Field_Field_operation_link[i][j] = new_name
                


Main_screen()



