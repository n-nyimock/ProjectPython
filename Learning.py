x = input("What is your name? ")


def function():
    print(x.upper()+ ", you are Awesome")

function()




#Global variable
def globe():
    global x #makes the variable x to be used anywhere
    x = "Awesome"
globe()
print('Python is '+x)



#Incorrect, will throw an error/global not set
def lobe():
    y = "Mind blowing"

lobe()
print('Python is '+y) #error y is not defined


b = 1j
print(type(b))
