print('\n\n_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
print('\n\t\t\t\t\t\t\t\t\t|APPLICATION PROGRAM|\n\t\t\t\t\t\t\t\t    *****************************')
print('\n\t\t\t\t\t\t\t\t(TO ADMIT THE PATIENT IN THE HOSPITAL)\n\t\t\t\t\t\t\t  ________________________________________________')
print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
"""
Following are the details of data regarding the hospital are given in this Application : 
        -common rooms = 120
        -A.C rooms = 100 
        -special rooms= 80 
        -patients admitted in a=100 
        -patients admitted in b=80 
        -patients admitted in c=70 
        -cost of common room=5000 per day 
        -cost of A.C room=10000 per day
        -cost of special room=20000 per day 
        -discount offer=50% on each room
"""     

a='common room'
b='A.C room'
c='special room'

A=[]
A.append(a)
A.append(b)
A.append(c)
print('\n\n  • First let us check are the rooms available or not !')

pa=100
### where pa=patients admitted in common room
pb=80
### where pb=patients admitted in A.C room 
pc=70
### where pc=patients admitted in special room 
ta=120
### where ta=total number of common rooms 
tb=100
### here tb=total number of A.C rooms 
tc=80
### where tc=total number of special rooms 

totalrooms=ta+tb+tc
currentpatients=pa+pb+pc
if(currentpatients<totalrooms):
	print('\n\n\t\t\t\t Yes rooms are available for the patient :)\n\t\t\t\t_____________________________________________')
	print('\n\n  • We have the following categories of room:\n\n\t\t\t\t',A,'\n\t\t\t\t_____________________________________________')
else:
	print('\n\n\t\t\t\t Oops ! :( sorry ! not in range\n\t\t\t\t***********************************')		
print('\n\n  • Following are the details about the cost of rooms:\n\n\t\t\t\t- Cost of common room=5000 per day\n\t\t\t\t_____________________________________\n\n\t\t\t\t- Cost of A.C room =10000 per day\n\t\t\t\t_____________________________________\n\n\t\t\t\t- Cost of special room=20000 per day\n\t\t\t\t_____________________________________')	

pa=100
pb=80
pc=70

ta=120
tb=100
tc=80

r=input('\n\n  • Enter which room would you like to elect? then we will tell you about its cost:')
if(r==a):
		if(pa<ta):
			print('\n\n\t\t\t\t Yes !',a,'is available\n\t\t\t\t_________________________________')
		else:
			print('\n\n\t\t\t\t Sorry :(',a,'is not available !\n\t\t\t\t________________________')
elif(r==b):
		if(pb<tb):
			print('\n\n\t\t\t\t  Yes !',b,'is available\n\t\t\t\t_______________________________')
		else:
			print('\n\n\t\t\t\t Sorry :(',b,'is not available !\n\t\t\t\t ____________________________')
elif(r==c):
	if(pc<tc):
			print('\n\n\t\t\t\t Yes !',c,'is available\n\t\t\t\t__________________________________')
	else:
		print('\n\n\t\t\t\t Sorry ;(',c,'is not available !\n\t\t\t\t _______________________________')
else:
	print('\n\n\t\t\t\t Please inter valid room name !\n\t\t\t\t________________________________')
	if(not r==a and not r==b and not r==c):
		print('\n\n  • Again run the program and choose between the following list of rooms:\n\n\t\t\t\t-',A,'\n\t\t\t\t________________________________________________')			

price_a=5000
price_b=10000
price_c=20000

B=[]
B.append(price_a)
B.append(price_b)
B.append(price_c)

ca=price_a/2
if(r==a or r==b or r==c):
        d=int(input('\n\n  • How much would you pay because we also have discount opportunity?:'))
        if(d>=price_a):
                print('\n\n\t\t\t\tgreat ! bring your patient to the desired room\n\t\t\t      __________________________________________________')
        elif(d<ca):
                print('\n\n\t\t\t\t:( Sorry ! not in our range even after discount as well\n\t\t\t\t___________________________________________________________')
        else:
                print('\n\n\t\t\t\tyou should go for discount opportunity!\n\t\t\t\t_______________________________________')
if(d>=price_a or d<price_a or d<ca):    
        y='yes'
        n='no'
        o='none'			
        if(r==a or r==b or r==c):
                h=input("\n\n  • Do you want to avail the discount offer?:")
                if(h==y):
                        print("\n\n  • Ok let us tell you about the details of discount offer:")

                        """
                        -we are giving 50% discount on each room
                        -ca=cost of common room 
                        -cb=cost of A.C room 
                        -cc=cost of special room

                        """
                        ca=price_a/2
                        cb=price_b/2
                        cc=price_c/2

                        print('\n\n\t\t\t\t- Cost of',a,'after discount =',ca,'\n\t\t\t\t_______________________________________________')
                        print('\n\n\t\t\t\t- Cost of',b,'after discount=',cb,'\n\t\t\t\t_______________________________________________')
                        print('\n\n\t\t\t\t- Cost of',c,'after discount=',cc,'\n\t\t\t\t_______________________________________________')

                        z=input('\n\n  • Now which room will be affordable for you?:')

### since patients admitted in common room=100,it means room number 1 to 100 are reserved !
                        if(z==a):
                                print('\n\n\t\t\t\tGreat!pay the bill and bring your patient to common room#101\n\t\t\t\t_____________________________________________________________')

### since patients admitted in A.C room =80,it means room number 1 to 80 are reserved ! 						
                        elif(z==b):
                                print('\n\n\t\t\t\tGreat!pay the bill and bring your patient to the A.C room#81\n\t\t\t\t_____________________________________________________________')

### since patients admitted in special room=70,it means room number 1 to 70 are reserved !		
                        elif(z==c):
                                print('\n\n\t\t\t\tGreat!pay the bill and bring your patient to special room#71\n\t\t\t\t_____________________________________________________________')
                        elif(z==o):
                                print('\n\n\t\t\t\t:( So you can bring your patient to another hospital !\n\t\t\t\t_______________________________________________________')
                        else:
                                print('\n\n\t\t\t\tPlease enter valid room name by again running the program!\n\t\t\t\t___________________________________________________________')		

                elif (h==n):
                        print("\n\n\t\t\t\t\tno worries :) its up to you !\n\t\t\t\t  _______________________________________")
                        if(r==a):
                                if(pa<ta):
                                        if(d>=price_a):
                                                print('\n\n\t\t\t     Well ! as you elected,',a,'is available\n\t\t\t    ___________________________________________________')
                                                print('\n\n\t\t\t     Now you can bring your patient to the',a,'\n\t\t\t    __________________________________________________')
                                        else:
                                                print('\n\n\t\t\t\tNow you can take your patient to another hospital\n\t\t\t   _________________________________________________________')
                                else:
                                        print('\n\n\t\t\t Sorry :(',a,'is not available !\n\t\t\t  _________________________________________')
                        elif(r==b):
                                if(pb<tb):
                                        if(d>=price_b):
                                                print('\n\n\t\t\t\tWell ! as you elected,',b,'is available\n\t\t\t\t_____________________________________________\n\n\t\t\t\tNow you can bring your patient to the',b,'\n\t\t\t  _______________________________________________________')
                                        else:
                                                print('\n\n\t\t\t\tNow you can take your patient to another hospital\n\t\t\t   _________________________________________________________')
                                else:
                                        print('\n\n\t\t\t Sorry :(',b,'is not available !\n\t\t\t     _______________________________________')
                        elif(r==c):
                                if(pc<tc):
                                        if(d>=price_c):
                                                print('\n\n\t\t\t      Well ! as you elected,',c,'is available\nt\t\t\t     __________________________________________________\n\n\t\t\t      Now you can bring your patient to the',c,'\n\t\t\           _____________________________________________________')
                                        else:
                                                print('\n\n\t\t\t\tNow you can take your patient to another hospital\n\t\t\t   _________________________________________________________')
                                else:
                                        print('\n\n\t\t\t    Sorry :(',c,'is not available !\n\t\t\t    _______________________________________________')

                else:
                        if(not h==n and not h==y):
                                print('\n\t\t\t\t ok ! it means you are not interested to avail discount offer\n\t\t\t\t________________________________________________________________')
                                if(r==a):
                                        if(pa<ta):
                                                if(d>=price_a):  
                                                        print('\n\n\t\t\t       Well ! as you elected,',a,'is available\n\t\t\t      ________________________________________________\n\n\t\t\t      Now you can bring your patient to the',a,'\n\t\t\t    _____________________________________________________')
                                                else:
                                                        print('\n\n\t\t\t\tNow you can take your patient to another hospital\n\t\t\t      ______________________________________________________')
                                        else:
                                                print('\n\n\t\t\t Sorry :(',a,'is not available !\n\t\t\t  _______________________________')
                                elif(r==b):
                                        if(pb<tb):
                                                if(d>=price_b):
                                                        print('\n\n\t\t\t\tWell ! as you elected,',b,'is available\n\t\t\t\t_____________________________________________\n\n\t\t\t\tNow you can bring your patient to the',b,'\n\t\t\t\t_______________________________________________')
                                                else:
                                                        print('\n\n\t\t\t\tNow you can take your patient to another hospital\n\t\t\t     _______________________________________________________')
                                        else:
                                                print('\n\n\t\t\t Sorry :(',b,'is not available !\n\t\t\t     ______________________________')
                                elif(r==c):
                                        if(pc<tc):
                                                if(d>=price_c):
                                                        print('\n\n\t\t\t\tWell ! as you elected,',c,'is available\n\t\t\t\t________________________________________________\n\n\t\t\t\tNow you can bring your patient to the',c,'\n\t\t\t\t_____________________________________________________')
                                                else:
                                                        print('\n\n\t\t\t\tNow you can take your patient to another hospital\n\t\t\t      _____________________________________________________')
                                        else:
                                                print('\n\n\t\t\t Sorry :(',c,'is not available !\n\t\t\t________________________________________')


print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('\n\n\t\t\t\t\t\t\t\t | Made by : MAHAM TAHIR |\n\t\t\t\t\t\t\t      *******************************')	
print('\n_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
