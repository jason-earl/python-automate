#!/usr/bin/env python3

DIGITS = ['zero',
          'one',
          'two',
          'three',
          'four',
          'five',
          'six',
          'seven',
          'eight',
          'nine',
          'ten',
          'eleven',
          'twelve',
          'thirteen',
          'fourteen',
          'fifteen',
          'sixteen',
          'seventeen',
          'eighteen',
          'nineteen']

TENS = ['zero',
        'ten',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety']

def int_to_english(num):
    english = []
    hundreds = num // 100
    thousands = num // 1000
    millions = num // 1000000
    billions = num // 1000000000
    trillions = num // 1000000000000
    if trillions > 0:
        english.append(int_to_english(trillions))
        english.append("trillion")
        num = num % 1000000000000
        hundreds = num // 100
        thousands = num // 1000
        millions = num // 1000000
        billions = num // 1000000000
    if billions > 0:
        english.append(int_to_english(billions))
        english.append("billion")
        num = num % 1000000000
        hundreds = num // 100
        thousands = num // 1000
        millions = num // 1000000
    if millions > 0:
        english.append(int_to_english(millions))
        english.append("million")
        num = num % 1000000
        hundreds = num // 100
        thousands = num // 1000
    if thousands > 0:
        english.append(int_to_english(thousands))
        english.append("thousand")
        num = num % 1000
        hundreds = num // 100
    if hundreds > 0:
        english.append(int_to_english(hundreds))
        english.append("hundred")
        num = num % 100
    if num < 20:
        if num == 0:
            if len(english) == 0:
                return 'zero'
        else:
            english.append(DIGITS[num])
    else:
        tens = num // 10
        one = num % 10
        english.append(TENS[tens])
        if one != 0:
            english.append(DIGITS[one])
    return " ".join(english)

def main():
    for i in range(10000):
        print(int_to_english(i))

if __name__ == '__main__':
    main()
