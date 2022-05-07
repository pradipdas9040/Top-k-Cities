n = int(input("Enter a number: "))
print("Enter name of the cities: ")
inputs = []
inputs1 = []
inputs2 = []
while True:
    inp = input()
    if inp == "":
        break
    inputs.append(inp.split())

for i in range (len(inputs)):
    for j in range (len(inputs[i])):
        inputs1.append(inputs[i][j])

count = 0
while count < n:
    max_f = 0
    res = inputs1[0]
    for i in inputs1:
        f = inputs1.count(i)
        if f > max_f:
            max_f = f
            res = i
    inputs2.append(res)
    while res in inputs1:
        inputs1.remove(res)
    count += 1
    
if n > 1:
    print("\nTop",n,"cities are",end = " " )
if 1 == n:
    print("\nTop",n,"citi is",end = " " )
for i in range (len(inputs2)):
    print(inputs2[i],end = " ")