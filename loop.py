# for loop
for i in range(1,11):
    print(f"Welcome to my shop! Customer {i}")

mycustomer = ("Eric", "Lavender", "Christine", "Victor", "Angela")

for n in mycustomer:
    print(f"Welcome to my School {n}")

# suppose you buy
# bread ksh130
# milk ksh100
# sugar ksh200
# blueband ksh120
# caLculate the total expense

my_shopping=[130,100,200,120]
total =0

for s in my_shopping:
    total=total+s
print(f"Your total expense is {total}")

# while loop
num=0
while num <=8:
    print(f" Loops: {num}")
    num+=2

# imagine you start with 0 and save 100 everday until you save 500
money = 0
while money < 500:
    money=money+100
    print(f"Money saved: {money}")

print("Congratulation! you reached your target")