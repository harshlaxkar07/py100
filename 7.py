# from sys import exit as ex

if num:=int(input("enter the number: ")) <= 1:
    print(f"{num} is a non prime number")
else:
    for i in range(int(num**0.5 ),1,-1) :
        if  num%i == 0:
            print(f"{num} is not a prime number beacuse it is divisable by the {i}")
            break
    else:
        print(f"{num} is a prime number !!")