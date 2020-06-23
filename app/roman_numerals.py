roman_numerals = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
}


def parse(roman_num):
    
    idx = len(roman_num)-1
    nums = []
    try:    
        while(idx >= 0):
            if(idx == 0):
                nums.append(roman_numerals[roman_num[idx]])
                idx -= 1
            elif(roman_numerals[roman_num[idx]] <= roman_numerals[roman_num[idx-1]]):
                nums.append(roman_numerals[roman_num[idx]])
                idx -= 1
            elif(roman_numerals[roman_num[idx]] > roman_numerals[roman_num[idx-1]]):
                numeral = roman_num[idx-1]+roman_num[idx]
                nums.append(roman_numerals[numeral])
                idx -= 2
        return sum(nums)

    except:
        return 'The number you passed in was not a correctly formatted Roman numeral!'


print('final', parse('XCIXQQ'))
