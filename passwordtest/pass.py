
password="123456789"

passin=" "
x=0
while x<6:

    passin=input("enter le pass : ")
    if passin == password:
        print("conecte")

    elif passin=='0':
        break
          
    else:
        print("pass icorect ! ressayer nbr de tentation",x+1) 
           
       
    x+=1  


else:
    print("vous avez dépassé les 5 eteration !")
   
