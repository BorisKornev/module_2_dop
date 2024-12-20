n = random.randint(3, 20)
ans = ""

for i in range (1, n):
    for j in range (i+1, n):
        if n % (i + j) == 0:
            ans += str (i) + str (j)
print("Подходящие пары чисел для:", n, ans)