print("*       *       * * *")
print("*       *         *")
print("* * * * *         *")
print("*       *         *")
print("*       *       * * *")
name=input("Hello! What's your name? ")
age=int(input("Hi, "+name+"! How old are you? "))
old=100-age
if age >= 100:
    print("Wow, your old!")
elif age > 30:
    school=input("So in "+str(old)+" years, you'll be 100 years old. Cool!")
elif age >= 21:
    drink=input("Do you drink a lot?")
    if drink==yes or drink==yeah:
        print("I don't drink much because I'm a computer.")
    else:
            print("I don't drink a lot either because I am a computer. However, I do like some lubricant every once and a while.")
elif age >= 18:
    print("So in "+str(old)+" years, you'll be 100 years old. Cool!")
elif age >= 16:
    driver=input ("Do you have a driver's license?")
    if driver == "yes":
        print ("Than you can drive. Cool!")
    else:
        print ("Oh well. You should get one though.")
elif age == 11:
    print ("So your age in Roman numerals is XI. Cool! What school do you go to, "+name+"? ")
else:
    school=input("So in "+str(old)+" years, you'll be 100 years old. Cool! What school do you go to, "+name+"? ")
    print("So you go to "+school+", "+name+"? Nice.")
color=input("What's your favorite color? ")
print("You like "+color+"? Good to know.")
