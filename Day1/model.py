#model.py
def factorial_sum (num = 10):
    sum = 1
    for i in range(1,num+1):
        sum = sum * i
    return sum

if __name__ == "__main__":
    total = factorial_sum()
    print(total)