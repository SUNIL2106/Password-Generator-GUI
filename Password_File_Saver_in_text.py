
#defining function to save the file in desired path 
def file_saver(ps,dec):

    #checking the decision made by the user 
    if dec == 'Y':

        #asking for the relative path from the user
        print("Please Enter the relative path where you want to save the password as a text file", end = ' = ')
        p = str(input())

        #checking if the path ends with '\\' or not 
        if p.endswith('\\') == True:

            #Making a perfect path for the file to save
            p = p.removesuffix('\\') 
            p = p + '\\password.txt'

            #making the file on the designated path
            f = open(p,'wt')

            #Writing in the text file 
            f.write('Your Generated Password = ')
            f.write(str(ps)) #Saving the password
            f.write('\n')

            #Giving Credits in the text file
            f.write('\nThanks For using simple password generator')
            f.write('\nDeveloped By Sunil and Dipankar')
            f.write('\n12 Sci 2023-24')

            #Saving the file and closing it 
            f.flush()
            f.close()

            #Making the user sure that file is saved 
            print("Your password is saved at ", p)
        
        elif p.endswith('\\') == False:

            #Making a perfect path for the file to save
            p = p + '\\password.txt'

            #making the file on the designated path
            f = open(p,'wt')

            #Writing in the text file 
            f.write('Your Generated Password = ')
            f.write(str(ps)) #Saving the password
            f.write('\n')

            #Giving Credits in the text file 
            f.write('\nThanks For using simple password generator')
            f.write('\nDeveloped By Sunil and Dipankar')
            f.write('\n12 Sci 2023-24')

            #Saving the file and closing it 
            f.flush()
            f.close()

            #Making the user sure that file is saved 
            print("Your password is saved at ", p)

        else:

            #If the user entered wrong input bymistakely 
            print('Please check the provided path and try again later !') 

            #Making the user sure that file is not saved 
            print('Password not saved')

    
    elif dec == 'N':

        #Making the user sure that file is not saved 
        print('Password not saved')

    else:

        #If the user entered wrong input bymistakely
        print('Please enter correct vale and try again later !')

        #Making the user sure that file is not saved 
        print('Password not saved')
