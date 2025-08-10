
while True:
    a=int(input("Enter the first number: "))
    c=int(input("Enter the Second number: "))
    b=input("Enter the operation \n(+,-,*/) or q to quit: ")
    res=0
    
    match b:
        case '+':
            res=a+c
        case '-':
            res=a-c
        case '*':
            res=a*c
        case '/':
            if c != 0:
                res= a/c
            else:
                res= "Error: Division by zero"
        case 'q':
            res="Thank you, bye"
        case _:
            res="Invalid Operation"
    print(f"Result: {res}\n")       

