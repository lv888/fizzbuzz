#fizzbuzzattemptsLV
# Example output: "1 2 fizz 4 buzz fizz 7"
# fizz for numbers divisible by three
# buzz for numbers divisible by five
i = int(input("Enter a number: "))
num = 0
while num < i:
    num += 1 
    if num == 0:
        continue
    if num%3 == 0:
        print("fizz")
        continue
    if num%5 == 0:
        print("buzz")
        continue
    print(num)



exit()