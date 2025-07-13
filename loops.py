def calc_exp(base,exp):
    result=1
    for i in range(exp):
        result = result*base
    return result

base = int(input("Base :"))
exp = int(input("Exponent : "))
print("The base is:",base," its exponent is:",exp,"\nResult:",calc_exp(base,exp))

def even_checker():
    num = int(input("Enter a Number that is divisble by 2:"))

    if(num>60 and num%2!=0):
        print("Are you EVEN trying?")
        return 1
    elif(num%2!=0 and num>20):
        print("Don't worry EVENtually you'll get it")
        return 1
    elif(num%2!=0):
        print("EVEN Smart people struggle sometimes")
        return 1
    else:
        print("Oddly enough this is an Even number, NICE!")
        return 10
i=0
while i != 10:
    i =even_checker()


