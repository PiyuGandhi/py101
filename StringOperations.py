s = "Hello Bhishma \n Welcome to code wizards"

vowels = ["a","i","e","o","u","A","E","I","O","U"]
ans = 0

print(type(vowels))

for ele in s:
    if ele in vowels:
        ans += 1

print "Total vowels are " + str(ans)
        