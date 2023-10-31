# A code to know your secret santa without repetion 

import os
import random

# assign directory
Folder = '/home/redon213/secretsanta'
 
famillies = []

def get_families(Folder):
    # iterate over files in
    # that directory
    for filename in os.listdir( Folder + "/List_familly" ) :
        f = os.path.join( Folder + "/List_familly", filename )
        # checking if it is a file
        if os.path.isfile( f ) :

            # opening the file in read mode 
            my_file = open( f, "r" ) 

            # reading the file 
            data = my_file.read() 

            # splitting the text it further when '/n' is seen. 
            # and deleting empty values
            new_familly = data.split( "\n" )
            new_familly.remove( '' )

            # add the new familly to the list 
            famillies.append( new_familly )

            # close the file
            my_file.close() 
    return famillies


def get_last_chrismas(Folder):

    # opening the file in read mode 
    my_file = open( Folder+'/Last_chrismas.txt', "r" ) 

    # reading the file 
    data = my_file.read() 

    # splitting the text it further when '/n' is seen. 
    # and deleting empty values
    last_chrismas = data.split( "\n" )
    return last_chrismas

last_chrismas = get_last_chrismas(Folder)

# get families as list of list
famillies = get_families(Folder)

# get names as list
names = sum( famillies, [] ) 

already_gifted_lst = []

chrismas_list=[]
i = 0 
for name in names :
    name_gifter = name
    last_gifted = last_chrismas[i].split( " " )
    already_gifted = 'yes'
    while already_gifted == 'yes' :
        name_gifted = random.choice(names)
        for familly in famillies :
            if name_gifter in familly:
                list_familly = familly
        
        if name_gifted not in already_gifted_lst and name_gifted not in list_familly and name_gifter not in last_gifted[1] : #
            already_gifted = 'no'
            already_gifted_lst.append(name_gifted)
            chrismas_list.append( name_gifter + " " + name_gifted + "\n" )
            i = i+1
          
            


my_file = open( Folder+"/Last_chrismas.txt", "w" ) 
my_file.writelines(chrismas_list) 
my_file.close()
