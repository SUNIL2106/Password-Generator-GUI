import customtkinter
import Password_Generator as pg
from customtkinter import filedialog

#Setting theme

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#screen
root = customtkinter.CTk()
root.geometry("700x650")
root.title("Password Generator")

#text
label1 = customtkinter.CTkLabel(master=root,text="Password Generator",font=("Roboto",24))
label1.pack(pady=12,padx=10)
label2 = customtkinter.CTkLabel(master=root,text="Create strong and secure passwords to keep data safe .",font=("static/OpenSans_Condensed-Light.ttf",18))
label2.pack(pady=12,padx=10)

#Creating tabs
tabview = customtkinter.CTkTabview(master=root,height=500,width=600,border_width=3,corner_radius=20)
tabview.pack(padx=20, pady=20)

tabview.add("Simple password")  # add tab at the end
tabview.add("Complex password")
tabview.add("Customised password with custom values")  # add tab at the end


    
#simple password tab

#Taking input
entry11 = customtkinter.CTkEntry(master=tabview.tab("Simple password"),placeholder_text="Enter The length Of The password ",height=30,width=400,font=("Roboto",18),corner_radius=10)
entry11.pack(pady=12,padx=10)
entry12 = customtkinter.CTkEntry(master=tabview.tab("Simple password"),width=400,font=("Roboto",18),corner_radius=10)
entry12.pack(pady=12,padx=10)

bt11 = customtkinter.CTkButton(master=tabview.tab("Simple password"),text="Generate password" )


#password generating function     
def ps():
    a = int(entry11.get())
    entry12.delete(0,100)
    entry12.insert(0,pg.Random_List_Generator_Regular(a))

#save file function

def saveFile1():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text file",".txt")])
    filetext = str(entry12.get())
    file.write("Your password : "+filetext)
    file.close()
    filedialog.Open(file)

#button            
bt11 = customtkinter.CTkButton(master=tabview.tab("Simple password"),text="Generate password",command=ps )
bt11.pack(pady=12,padx=10)

bt11 = customtkinter.CTkButton(master=tabview.tab("Simple password"),text="Save password",command=saveFile1 )
bt11.pack(pady=12,padx=10)


#complex password tab

#Taking input
entry21 = customtkinter.CTkEntry(master=tabview.tab("Complex password"),placeholder_text="Enter No. of Upper-case Letters to include (<100)  ",width=450,font=("Roboto",18),corner_radius=10)
entry21.pack(pady=12,padx=10)
entry22 = customtkinter.CTkEntry(master=tabview.tab("Complex password"),placeholder_text="Enter No. of Lower-case Letters to include (<100)  ",width=450,font=("Roboto",18),corner_radius=10)
entry22.pack(pady=12,padx=10)
entry23 = customtkinter.CTkEntry(master=tabview.tab("Complex password"),placeholder_text="Enter No. of Special Characters to include (<100)  ",width=450,font=("Roboto",18),corner_radius=10)
entry23.pack(pady=12,padx=10)
entry24 = customtkinter.CTkEntry(master=tabview.tab("Complex password"),placeholder_text="Enter Numbers to include (<100)  ",width=400,font=("Roboto",18),corner_radius=10)
entry24.pack(pady=12,padx=10)
entry25 = customtkinter.CTkEntry(master=tabview.tab("Complex password"),width=400,font=("Roboto",18),corner_radius=10)
entry25.pack(pady=12,padx=10)

#password generating function  
def ps():
    a = int(entry21.get())
    b = int(entry22.get())
    c = int(entry23.get())
    d = int(entry24.get())
    entry25.delete(0,100)
    entry25.insert(0,pg.Random_List_Generator_Complex(a,b,c,d))

#save file function

def saveFile2():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text file",".txt")])
    filetext = str(entry25.get())
    file.write("Your password : "+filetext)
    file.close()
    
            
bt21 = customtkinter.CTkButton(master=tabview.tab("Complex password"),text="Generate password",command=ps )
bt21.pack(pady=12,padx=10)

bt21 = customtkinter.CTkButton(master=tabview.tab("Complex password"),text="Save password",command=saveFile2 )
bt21.pack(pady=12,padx=10)


#custom

#Taking input
entry31 = customtkinter.CTkEntry(master=tabview.tab("Customised password with custom values"),placeholder_text="Enter The length Of The password ",width=400,font=("Roboto",18),corner_radius=10)
entry31.pack(pady=12,padx=10)
entry32 = customtkinter.CTkEntry(master=tabview.tab("Customised password with custom values"),placeholder_text="Enter No. of custom values (<100) ",width=400,font=("Roboto",18),corner_radius=10)
entry32.pack(pady=12,padx=10)

#variables
nv = entry31.get()
ccv=entry32.get()
cv = []
count = 0
rc='N'

#function to handle input loop
def click_handler():
    global count
    global cv
    count+=1
    a = entry33.get()
    for i in range(int(entry32.get())):
        cv.append(a)
        entry33.delete(0,100)
        if count==int(entry32.get()):
            entry33.configure(state="disabled")
            entry32.configure(state="disabled")

#save file function

def saveFile3():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text file",".txt")])
    filetext = str(entry34.get())
    file.write("Your password : "+filetext)
    file.close()

    
entry33 = customtkinter.CTkEntry(master=tabview.tab("Customised password with custom values"),placeholder_text="Enter Any Values i.e to be included in password ",width=400,font=("Roboto",18),corner_radius=10)
entry33.pack(pady=12,padx=10)
bt31 = customtkinter.CTkButton(master=tabview.tab("Customised password with custom values"),text="Enter",command=click_handler )
bt31.pack(pady=12,padx=10)

#Switch
def switch_event():
    global rc
    if switch_var.get()=="off":
        rc='N'
    if switch_var.get()=="on":
        rc='Y'

switch_var = customtkinter.StringVar(value="off")
switch = customtkinter.CTkSwitch(master=tabview.tab("Customised password with custom values"), text="Do you want to mix your custom values with default values ", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.pack(pady=10,padx=10)


entry34 = customtkinter.CTkEntry(master=tabview.tab("Customised password with custom values"),width=400,font=("Roboto",18),corner_radius=10)
entry34.pack(pady=12,padx=10)

#password generating function         
def ps():
    global cv
    nv = entry31.get()
    ccv=entry32.get()
    entry34.delete(0,100)
    entry34.insert(0,pg.Custom_Password_Generator_With_Custom_Values(int(nv),int(ccv),cv,rc))

     
bt32 = customtkinter.CTkButton(master=tabview.tab("Customised password with custom values"),text="Generate password",command=ps )
bt32.pack(pady=12,padx=10)

bt33 = customtkinter.CTkButton(master=tabview.tab("Customised password with custom values"),text="Save password",command=saveFile3 )
bt33.pack(pady=12,padx=10)


root.mainloop()
