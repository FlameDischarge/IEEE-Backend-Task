s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("The strings are balanced")
else:
    for i in s1:
        if i in s2:
            print("They are not complementary")
            break
    else:
        print("They are complementary")
