#Importing Password Functions 
import Password_Generator as pg
import Password_File_Saver_in_text as pfsit

#Making loop
while True:
    try:
        #Taking the choice of user
        print('Welcome to the basic password generator code')
        print('Enter 1 to generate Simple password')
        print('Enter 2 to generate Complex')
        print('Enter 3 to generate Customised password with custom values')
        print('Enter 4 to exit the Code')
        print('Please input values in integer only')
        inp = int(input("Select your Choice : "))


        #Decion Making

        #Regular Password Genration
        if (inp == 1):

            #Basic Input
            nrgps = int(input('Enter The length Of The password :'))

            #Using Fuction to genterate password defined in password_generator file 
            ps = pg.Random_List_Generator_Regular(nrgps)

            print("Your Simple Password is generated = ",ps)

        #Complex Password Genration
        elif (inp == 2):
            
            #Basic Input
            nua = int(input("Enter No. of Upper-case Letters to include (<100) : "))
            nla = int(input("Enter No. of Lower-case Letters to include (<100) : "))
            nsyb = int(input("Enter No. of Special Characters to include (<100) : "))
            nnum = int(input("Enter Numbers to include (<100) : "))

            #Using Fuction to genterate password defined in password_generator file 
            ps = pg.Random_List_Generator_Complex(nua,nla,nnum,nsyb)

            print('Your Complex password is generated = ', ps)

        #CUSTOM Password Genration
        elif (inp == 3):

            #Basic Input
            nv = int(input('Enter The length Of The password : '))

            #Using Fuction to genterate password defined in password_generator file 
            ps = pg.Custom_Password_Generator_With_Custom_Values(nv)

            print('Your Customised password with custom values is generated = ', ps)
        
        #Code Exit 
        elif (inp == 4):

            #Credits
            print('Thanks For Using The Basic Password Generator Code')
            print("Develped By Dipankar & Sunil")
            print('12 Science - KVSR - 2023-24')

            break

        else:
            print('Please Enter Correct and acceptable values only!')

        #Asking if the user want to save the password in text file in a defined path 
        dec = input('Do you want to save the password in a text file (Y/N) : ')

        #Calling the function to save the file using the fuction defined earlier
        pfsit.file_saver(ps,dec)

    #Exceotion Handaling 
    except TypeError:

        print('Oops You encountered a !!TypeError!!')

    except ValueError:

        print('Oops You encountered a !!ValueError!!')