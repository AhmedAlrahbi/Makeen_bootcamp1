#ICA sum digit inherted from parameter
def sum_digit(entryU):
    entry = entryU
    digit_sum = 0

    while entry > 0:
        digit = entry % 10
        print(digit)
        digit_sum += digit
        entry = entry // 10

    print("sum of the digits:", digit_sum)
def main():
    sum_digit(234)
main()