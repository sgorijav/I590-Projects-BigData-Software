def fizzbuzz(n):
    for i in range(1,n+1):
        factor2 = i%2
        factor3 = i%3
        if factor2 == 0 and factor3 == 0:
            print('fizzbuzz')
        else:
            if factor2 == 0:
                print('fizz')
            else:
                if factor3 == 0:
                    print('buzz')
                else:
                    print(i)
    
number = input("enter number: ")

if type(number) == int:
    print("You entered the number ",number)
    fizzbuzz(number)
else:
    print("You didnt enter valid Number. Try Again")
