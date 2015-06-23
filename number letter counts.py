import re

def convert_char(char):
     return {
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine',
        '10' : 'ten',
        '11' : 'eleven',
        '12' : 'twelve',
        '13' : 'thirteen',
        '14' : 'fourteen',
        '15' : 'fifteen',
        '16' : 'sixteen',
        '17' : 'seventeen',
        '18' : 'eighteen',
        '19' : 'nineteen',
    }.get(char,'')

def convert_char_tens(char):
     return {
        '1' : 'ten',
        '2' : 'twenty',
        '3' : 'thirty',
        '4' : 'forty',
        '5' : 'fifty',
        '6' : 'sixty',
        '7' : 'seventy',
        '8' : 'eighty',
        '9' : 'ninety',
        '0' : '',
    }.get(char,'')
    
def count_letters(string):
    test = string.replace(" ","")
    return len(test)

def two_digit(temp):
    return convert_char_tens(temp[0]) + " " + convert_char(temp[1])

def three_digit(temp):
    result = convert_char(temp[0]) + " hundred and "

    if (int(temp[-2:]) < 20):
        result += convert_char(str(int(temp[-2:])))
    else:
        result += two_digit(temp[-2:])

    result = re.sub(r'and\s*$',"",result)
    return result
        

count = 0
for i in range(1,1001):
    #number = raw_input("What number to convert? ")
    #numeric = int(number)
    number = str(i)
    numeric = i
    
    if (numeric == 1000):
        result = "one thousand"
    elif (numeric < 20):
        result = convert_char(number)
    elif (numeric < 100):
        result = two_digit(number)
    else:
        result = three_digit(number)
        
    #print result
    
    count += count_letters(result)
print count

