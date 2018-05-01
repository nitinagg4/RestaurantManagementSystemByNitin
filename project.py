from tkinter import *
from tkinter import messagebox, Entry
index=0
w=Tk()
w.title("Restaurant Management System")
count=0
def ok():
        print("OK")
        s1.set("OK")
def addrec():
        f=open("mydata.txt","a")
        n=s1.get()
        a=s2.get()
        b=s3.get()
        c=s4.get()
        d=s5.get()
        for i in range(len(n),20):
                n=n+" "
        for i in range(len(a),20):
                a=a+" "
        
        for i in range(len(b),20):
                b=b+" "
        
        for i in range(len(c),20):
                c=c+" "
        for i in range(len(d),20):
                d=d+" "
        f.writelines(n+" "+a+" "+b+" "+c+" "+d+"\n")
        f.close()
def nextrec():
        file=open('mydata.txt','r')
        global index
        index=index+1
        file.seek(index)
        try:
                c=file.readlines()
                xyz = c[index]
                l=list(xyz.split())
                t1.delete(0,'end');t2.delete(0,'end');t3.delete(0,'end');t4.delete(0,'end');t5.delete(0,'end');
                t1.insert(0,l[0]);t2.insert(0,l[1]);t3.insert(0,l[2]);t4.insert(0,l[3]);t5.insert(0,l[4]);
        except:
                messagebox.showinfo("Title", "")
        file.close()

def prevrec():
        file=open('mydata.txt','r')
        global index
        index=index-1
        try:
                file.seek(index)
                c=file.readlines()
                xyz = c[index]
                l=list(xyz.split())
                t1.delete(0,'end');t2.delete(0,'end');t3.delete(0,'end');t4.delete(0,'end');t5.delete(0,'end');
                t1.insert(0,l[0]);t2.insert(0,l[1]);t3.insert(0,l[2]);t4.insert(0,l[3]);t5.insert(0,l[4]);
        except:
                messagebox.showinfo("Title", "no more records")
        file.close()
def firstrec():
        file=open('mydata.txt','r')
        t1.delete(0,'end');t2.delete(0,'end');t3.delete(0,'end');t4.delete(0,'end');t5.delete(0,'end');
        file.seek(0)
        k=file.readline()
        k=k.split()
        t1.insert(0,k[0]);t2.insert(0,k[1]);t3.insert(0,k[2]);t4.insert(0,k[3]);t5.insert(0,k[4]);
        file.close()
def updaterec():
        file=open('mydata.txt','r')
        lines=file.readlines()
        file.close()
        file=open('mydata.txt','w')
        for line in lines:
                com=line.split()
                if com[0]==t1.get():
                        file.write(t1.get()+'\t'+t2.get()+'\t'+t3.get()+'\t'+t4.get()+'\t'+t5.get()+'\n')
                        messagebox.showinfo('Title','updated')
                else:
                        file.write(line)
        t1.delete(0,'end');t2.delete(0,'end');t3.delete(0,'end');t4.delete(0,'end');t5.delete(0,'end');
        file.close()
def exitt():
        w.destroy()
def deleterec():
        f=open("mydata.txt","r")
        lines = f.readlines()
        f.close()
        f = open("mydata.txt","w")
        for line in lines:
                com = line.split()
                if com[0] != s4.get():
                        f.write(line)
        messagebox.showinfo("Alert","Record Deleted!")
        s5.delete(0,"end")
        s4.delete(0,"end")
        s3.delete(0,"end")
        s2.delete(0,"end")
        s1.delete(0,"end")
        f.close()
def lastrec():
        file=open('mydata.txt','r')
        t1.delete(0,'end');t2.delete(0,'end');t3.delete(0,'end');t4.delete(0,'end');t5.delete(0,'end');
        for i in file:
                k=i
        k=k.split()
        t1.insert(0,k[0]);t2.insert(0,k[1]);t3.insert(0,k[2]);t4.insert(0,k[3]);t5.insert(0,k[4]);
        file.close()
l1=Label(w,text="Food")
l2=Label(w,text="Drinks")
l3=Label(w,text="Total")
l4=Label(w,text="Reference")
l5=Label(w,text="Type")
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
t1=Entry(w,textvariable=s1)
t2=Entry(w,textvariable=s2)
t3=Entry(w,textvariable=s3)
t4=Entry(w,textvariable=s4)
t5=Entry(w,textvariable=s5)
l1.grid(row=0,column=1)
l2.grid(row=1,column=1)
l3.grid(row=2,column=1)
l4.grid(row=3,column=1)
l5.grid(row=4,column=1)
t1.grid(row=0,column=2)
t2.grid(row=1,column=2)
t3.grid(row=2,column=2)
t4.grid(row=3,column=2)
t5.grid(row=4,column=2)
b1=Button(w,text="ADD",command=addrec)
b2=Button(w,text=">",command=nextrec)
b3=Button(w,text="EXIT",command=exitt)
b4=Button(w,text="LAST",command=lastrec)
b5=Button(w,text="<",command=prevrec)
b6=Button(w,text="FIRST",command=firstrec)
b7=Button(w,text="UPDATE",command=updaterec)
b8=Button(w,text="DELETE",command=deleterec)
b1.grid(row=5,column=1)
b2.grid(row=5,column=2)
b3.grid(row=5,column=3)
b4.grid(row=5,column=4)
b5.grid(row=6,column=1)
b6.grid(row=6,column=2)
b7.grid(row=6,column=3)
b8.grid(row=6,column=4)
w.mainloop()
