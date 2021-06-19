def app():
     name= input("Enter the name:")
     print(name)
     age = int(input("Your age:"))
     print(age)
     gender= input("Enter your gender:")
     if (gender=='male') or  (gender=='female'):
          print(gender)
     else:
          print("Enter the correct gender")
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

app()