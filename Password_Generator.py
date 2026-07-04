import random as rd 
import customtkinter
#Defining different values to be included in passwords
ua = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
la = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ['0','1','2', '3', '4','5','6','7','8','9']
syb = ['!','@','#','$','&',"%","^","*","(",")","-","_","~","`","{","}","[","]","'",'"',":",";","|",'/',"?","<"
       ">",".",",","+","=","₹"]


#Making Complex Password Fuction
def Random_List_Generator_Complex(nua,nla,nnum,nsyb):

    #Random Lists Generated
    rua = []
    rla = []
    rnum = []
    rsyb = []

    #Random Values Choosen using random function from the predefined values to be used in password
    for i in range (nua):
        rvua = rd.choice(ua)
        rua.append(rvua)
    
    #Random Values Choosen using random function from the predefined values to be used in password
    for i in range (nla):
        rvla = rd.choice(la)
        rla.append(rvla)
    
    #Random Values Choosen using random function from the predefined values to be used in password
    for i in range (nnum):
        rvnum = rd.choice(num)
        rnum.append(rvnum)
    
    #Random Values Choosen using random function from the predefined values to be used in password
    for i in range (nsyb):
        rvsyb = rd.choice(syb)
        rsyb.append(rvsyb)

    #Shuffinling the lists to make it more random and hard to crack
    rd.shuffle(rua)
    rd.shuffle(rla)
    rd.shuffle(rnum)
    rd.shuffle(rsyb)

    genlsps = rua+rla+rnum+rsyb #Adding all the list in one place

    #Shuffinling the lists to make it more random and hard to crack
    rd.shuffle(genlsps)

    #Converting the list into String Value
    genps = ''
    for i in genlsps:
        genps = genps + i

    #Returning The generated password as output of the fuction 
    return genps


#Regular Password genration Fuction making 

fls = ua+la+num+syb #Adding all the predefined values 
rd.shuffle(fls) #Shuffling the values to make it more random

#defining function for the regular password 
def Random_List_Generator_Regular(nrgps):

    #Random Values Choosen using random function from the predefined values to be used in password
    rgpsls = []
    for i in range (nrgps):
        rvrg = rd.choice(fls)
        rgpsls.append(rvrg)

    #Shuffinling the lists to make it more random and hard to crack
    rd.shuffle(rgpsls)
    
    #Converting the list into String Value
    genps = ''
    for i in rgpsls:
        genps = genps + i

    #Returning The generated password as output of the fuction 
    return genps


def Custom_Password_Generator_With_Custom_Values(nv,ccv,cv,rc):
    
    #Shuffinling the lists to make it more random and hard to crack
    rd.shuffle(cv)

    #Decision Making 
    if rc == 'Y':

        cv = cv+fls #Adding default values to the custom values 

        #Shuffinling the lists to make it more random and hard to crack
        rd.shuffle(cv)

        #Random Values Choosen using random function from the mixed values to be used in password
        rcvpsls = []
        for i in range(nv):
            rcv = rd.choice(cv)
            rcvpsls.append(rcv)
        
        #Shuffinling the lists to make it more random and hard to crack
        rd.shuffle(rcvpsls)

        #Converting the list into String Value
        genps = ''
        for i in rcvpsls:
            genps = genps + i

        #Returning The generated password as output of the fuction 
        return genps
    
    else:
        
        #Random Values Choosen using random function from the values inputed by the users to be used in password
        rcvpsls = []
        for i in range(nv):
            rcv = rd.choice(cv)
            rcvpsls.append(rcv)
        
        #Shuffinling the lists to make it more random and hard to crack
        rd.shuffle(rcvpsls)

        #Converting the list into String Value
        genps = ''
        for i in rcvpsls:
            genps = genps + i

        #Returning The generated password as output of the fuction 
        return genps
    
