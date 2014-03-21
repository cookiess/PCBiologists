#http://docs.python.org/2/library/tk.html

from Tkinter import *
import sys
import MySQLdb
 
connect = MySQLdb.connect("127.0.0.1", user="temp", passwd="temp", db="PCBio" )
cursor = connect.cursor ()


#function to save
def SaveData(event=None):
    f = a.get()
    g = b.get()
    h = c.get()
    cursor.execute ("""INSERT INTO genes (taxon, gene, sequence) VALUES("%s", "%s", "%s")"""% (f,g,h))
    print "Number of rows inserted: %d" % cursor.rowcount

root = Tk()
ent_frame = Frame(root)

# define the label
Label(ent_frame, text="taxon:").pack(side=LEFT)

# define the field
a = Entry(ent_frame, width=15)

# pack is a method needed to define the geometry; it indicates where the form will be when the window is resized
a.pack(side=LEFT)

#same as above but this one is defined as b
Label(ent_frame, text="gene:").pack(side=LEFT)
b = Entry(ent_frame, width=15)
b.pack(side=LEFT)

#same as above but this one is defined as c
Label(ent_frame, text="sequence:").pack(side=LEFT)
c = Entry(ent_frame, width=15)
c.pack(side=LEFT)
ent_frame.pack()

def onclick(event=None):
    print("You clicked the button")

root.bind('<Return>', SaveData)
# Button(root, text="Save",command=SaveData)
 
mainloop()
connect.close()