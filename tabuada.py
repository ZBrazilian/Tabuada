from time import sleep
tabuada = int(input("Qual tabuada vc quer saber ?\n"))
print("-"*15)
zero = 0
dez = 10
sleep(1)
while dez:
	zero = zero+1
	print(f"{tabuada} x {zero} = {tabuada*zero}")
	dez -= 1
print("-"*15)