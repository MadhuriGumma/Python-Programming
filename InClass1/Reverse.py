num = int(input('Enter a number to Reverse:'))


Reverse = 0

while(num > 0):
    remind = num % 10
    Reverse = (Reverse * 10) + remind
    num = num // 10

print(Reverse)
