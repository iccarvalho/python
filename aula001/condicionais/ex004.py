print("Informe dois valores para mostrar os números entre eles")
A = int(input("Informe um número: "))
B = int(input("Informe outro número: "))

if(A < B):
    while(A <= B):
        print(A)
        A = A + 1
elif(A > B):
    while(A >= B):
        print(B)
        B = B + 1
else:
    print("Os valores são iguais")