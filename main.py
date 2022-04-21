from tkinter import *
from tkinter.ttk import *


def print_on_screen(txt):
    output_field.insert(END,txt+'\n')    


def start(txt):
    if (txt[0]>='a' and txt[0]<='z') or(txt[0]>='A' and txt[0]<='Z') :
        dfa=2
        print_on_screen(f"{txt}:id:2")
    elif txt[0].isdigit():
        try:
            float(txt)
            dfa=2
            print_on_screen(f"{txt}:num:2")
        except:
            dfa=5
            print_on_screen(f"{txt}:wrong_id:5")
    else:
        dfa=5
        print_on_screen(f"{txt}:op:5")
    return dfa

def state2(txt):
    if txt=='+' or txt=='-' or txt=='*' or txt=='/':
        dfa=3
        print_on_screen(f"{txt}:op:3")
    else:
        dfa=5
        if (txt>='a' and txt<='z') or(txt>='A' and txt<='Z'):
            print_on_screen(f"{txt}:id:5")
        else:
             print_on_screen(f"{txt}:num:5")
    return dfa


def state3(txt):
    if (txt[0]>='a' and txt[0]<='z') or(txt[0]>='A' and txt[0]<='Z') :
        dfa=4
        print_on_screen(f"{txt}:id:4")
    elif txt[0].isdigit():
        try:
            float(txt)
            dfa=4
            print_on_screen(f"{txt}:num:4")
        except:
            dfa=5
            print_on_screen(f"{txt}:wrong_id:5")
    else:
        dfa=5
        print_on_screen(f"{txt}:op:5")
    return dfa

def state4(txt):
    if txt=='+' or txt=='-' or txt=='*' or txt=='/':
        dfa=3
        print_on_screen(f"{txt}:op:3")
    else:
        dfa=5
        if (txt>='a' and txt<='z') or(txt>='A' and txt<='Z'):
            print_on_screen(f"{txt}:id:5")
        else:
             print_on_screen(f"{txt}:num:5")
            
    return dfa

def take_string(lst):
    dfa=1
    for txt in lst:
        if dfa==1:
            dfa=start(txt)
        elif dfa==2:
            dfa=state2(txt)
        elif dfa==3:
            dfa=state3(txt)
        elif dfa==4:
            dfa=state4(txt)
        else:
            print_on_screen("error occur")
            break

def parse_str(str_in):
    string = ""
    lst = []
    for char in str_in:
        if char==' ':
            continue
        elif char not in('+','*','/','-'):
            string=string+char
        else:
            if string:
                lst.append(string)
            lst.append(char)
            string=""
    if string:
        lst.append(string)
    return lst

def propagate(str_in):
    lst = parse_str(str_in)
    take_string(lst)

def on_submit():
    output_field.config(state=NORMAL)
    output_field.delete("1.0",END)
    propagate(str_input.get())
    output_field.config(state=DISABLED)

if __name__ == "__main__":

    root =  Tk()
    root.title('Compiler project')
    img = PhotoImage(file='dfa.png')
    image = Label(root,image=img)
    re_img =  PhotoImage(file='regular-expression-resized.png')
    re_image = Label(root,image=re_img)
    str_input = Entry(root,width=145)
    submit_button = Button(root,text="Submit text",command=on_submit)
    output_field = Text(root)
    output_field.config(state=DISABLED)
    str_input.grid(row=0,column=0,columnspan=2)
    image.grid(row=1,column=0,rowspan=2)
    re_image.grid(row=1,column=1)
    submit_button.grid(row=0,column=2)
    output_field.grid(row=2,column=1,columnspan=2)
    root.mainloop()
    