def LuhnCheck(x):
    d=0
    s=str(x)
    if len(s)!=16:
        return False
    else:
        for i in range(len(s)):
            t=int(s[i])
            if i%2!=0:
                d+=t
            else:
                if t*2>=10:
                    d+=(t*2-9)
                else:
                    d+=(t*2)
        if d%10==0:
            return True
        else:
            return False
          
print("Welcome to the Credit Card Validator!")
try:
    a=int(input("Enter the Credit Card Number: "))
    if LuhnCheck(a):
        print("Congratulations, the entered Credit Card number is valid!")
    else:
        print("Unfortunately, you have entered an invalid Credit Card number....")
except TypeError:
    print("Occurence of non-numeric character is invalid... Please try again!")
    