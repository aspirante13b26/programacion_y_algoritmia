def getTotalX(a, b):
    # Write your code here
    max_a, min_b = max(a), min(b)
    if max_a > min_b: return 0
    num = max_a
    mult = 1
    res = 0
    while num <= min_b:
        div_a , div_b = True, True
        for m in a[:-1]:
            if num%m != 0:
                div_a = False
                break
        if div_a: 
            for n in b:
                if n%num != 0:
                    div_b = False
                    break
            if div_b:
                res += 1
        mult += 1
        num = mult*max_a
    return res


a = [2,4]
b = [16,32,96]

print(getTotalX(a,b))

hour = "five"
minutes = "ten"
print(hour + minutes)

def timeInWords(h, m):
    # Write your code here
    res = ""
    dic = {
        0: " o' clock",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "half"
    }
    
    past = False
    
    if m == 0: return dic[h] + dic[m]
    if m == 30: return dic[m] + " past " + dic[h]
    if m > 30:
        m = 60 - m
        past = True
    if m == 15: 
        if past: 
            if h+1 > 12: h = 0
            return dic[m] + " to " + dic[h + 1] 
        return dic[m] + " past " + dic[h]
    if m > 20 and m < 30:
        units = m%20
        minutes = "".join([dic[20], " ", dic[units]])
    else:
        minutes = dic[m]
    if past: 
        if h+1 > 12: h = 0
        return minutes + " minutes to " + dic[h + 1]
    return minutes + " minutes past " + dic[h]

print(timeInWords(7, 25))
