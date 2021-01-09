
def person():
    name = input("please tell me your name ")
    print("hello " + name)
    age = input("what is your age? ")
    print("hello " + name + " your age is " + age)
    if int(age) >= 60:
        print("you are elderly")
    elif int(age) >= 18 and int(age) <= 60 :
        print("you are an adult")
    else:
        print("you are still a child")

person()


