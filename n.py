from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
def about():
    showinfo('notepad',"helo")


def openn():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])

    if file==" ":
        file=None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled-Notepad",defaultextension=".txt",filetypes=[("All files","*.*"),
                                                                                               ("Text documents","*.*")])
        if file=="":
            file=None
        else:
        #save as new file
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()




def new():
    global file
    root.title("Untitles-Notepad")
    textarea.delete(1.0,END)

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

if __name__ == '__main__':
    root=Tk()
    #title
    root.title('Untitled-Notepad')
    file=None
    root.geometry('800x500')
    #textarea where we write

    textarea=Text(root)
    textarea.pack(fill=BOTH,expand=True)

    #creating menu

    menubar=Menu(root)
    #filemenu start

    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="New      Ctrl+N",command=new)
    filemenu.add_command(label="Open     Ctrl+O",command=openn)
    filemenu.add_command(label="Save      Ctrl+S",command=save)
    filemenu.add_separator()
    filemenu.add_command(label="Print     Ctrl+P")
    filemenu.add_command(label="Exit")

    menubar.add_cascade(label="File",menu=filemenu)
    #edit menu

    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Cut        Ctrl+X",command=cut)
    editmenu.add_command(label="Copy        Ctrl+C",command=copy)
    editmenu.add_command(label="Paste      Ctrl+V",command=paste)

    menubar.add_cascade(label="Edit",menu=editmenu)

    #helpmenu

    help = Menu(menubar,tearoff=0)
    help.add_command(label="AboutNotepad",command=about)

    menubar.add_cascade(labe="help",menu=help)

    root.config(menu=menubar)

#adding scrollbar
    scroll=Scrollbar(textarea,cursor='Arrow')
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    root.mainloop()