

# Código 1

# for xxxx in range(15):
# 	print("Teño fame")
#print("Vou comer")



# for numElefantes in range(6):
# 	print(numElefantes, ' elefantes se balanceaban sobre la tela... ')


# for cuenta in range(1, 51):
# 	print(cuenta,"cuenta")
    

import random 

secreto = random.randint(0, 100)


for xxx in range(5):
    contestado = input("Que número dis?")
    resp = int(contestado)

    if(resp == secreto):
         print("ole")

    if(resp<secreto):
        print("mayor")

    if(resp>secreto):
        int("menor")

 

