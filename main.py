def app():
     try:
     name= input("Enter the name:")
     print(name)
     age = int(input("Your age:"))
     print(age)
     gender= input("Enter your gender:")
     if (gender!='male') or  (gender!='female'):
          raise Exeption
     print(gender)
     salary=int(input("Your salary:"))
     print(salary)
     state= input("Your State:")
     if(len(state)>=5):
          print(state)
     else:
          print("Enter the correct state")
     city= input("Your city:")
     if(len(city)>=4):
          print(city)
     else:
          print("Enter the correct city")
         
     
     except:
          print('Enter the correct gender')
          

app()
