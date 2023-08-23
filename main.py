from tkinter import *
root=Tk()
lb_name=Label(root,text="name").grid(row=0,column=0)
ent_name=Entry(root,width=50).grid(row=0,column=1)
lb_address=Label(root,text="address").grid(row=1,column=0)
ent_address=Entry(root,width=50).grid(row=1,column=1)
lb_mobile=Label(root,text="mobile").grid(row=2,column=0)
ent_mobile=Entry(root,width=50).grid(row=2,column=1)
lb_email=Label(root,text="email").grid(row=3,column=0)
ent_email=Entry(root,width=50).grid(row=3,column=1)

def showAll():
    pass
def create():
    pass
def edit():
    pass
def delete():
    pass
def close():
    pass
# lb2.grid(row=1,column=0)
btn_showAll=Button(root,text="show All",pady=10 ,command=showAll,fg="blue",bg="white").grid(row=4,column=0)
btn_create=Button(root,text="create",pady=10,command=create,fg="blue",bg="white").grid(row=4,column=1)
btn_edit=Button(root,text="edit",pady=10,command=edit,fg="blue",bg="white").grid(row=4,column=2)
btn_delete=Button(root,text="delete",pady=10,command=delete,fg="blue",bg="white").grid(row=4,column=3)
btn_close=Button(root,text="close",pady=10,command=close,fg="blue",bg="white").grid(row=4,column=4)


# lb1.pack()
# lb2.pack()
root.mainloop()
