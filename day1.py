with open("data/day1.txt") as file:
    lines = file.read().split()

pos = 50
res1, res2 = 0, 0

for inst in lines:
    drct, num = inst[0], int(inst[1:])
    if drct == 'L': num *= -1
    rots = abs(num)//100
    res2 += rots
    if pos + num < 0: res2 += 1
    elif pos + num > 99: res2 += 1
    pos = (pos + num) % 100
    print(rots, pos)

# for inst in lines:
#     drct, num = inst[0:], int(inst[1:])
#     if drct == 'L': num *= -1
#     pre = pos
#     pos += num
#     if pos < 0:
#         count += abs(pos//100)
#         if pre == 0: count -= 1
#         if pos%100 == 0: count -= 1
#         pos = pos%100
#     elif pos > 99:
#         # print(pre, pos, count)
#         count += pos//100
#         if pos%100 == 0: count -= 1
#         if pre == 0 and pos%100 == 0: count -= 1
#         pos = pos%100
#     if pos == 0: count += 1

print(pos, res2)

# dial = 50
# result1 = 0
# result2 = 0
# with open('data/day1.txt', 'r') as f:
#     for line in f.readlines():
#         num = int(line[1:])
#         if line[0] == 'L':
#             num *= -1
#         full_rots = abs(num) // 100
#         result2 += full_rots
#         remainder = num + (-1 if num > 0 else -1)*100*full_rots

#         if remainder < 0 < dial and remainder + dial <= 0:
#             result2 += 1
#         elif remainder > 0 and remainder + dial > 99:
#             result2 += 1

#         dial = (dial + num) % 100
#         if dial == 0:
#             result1 += 1

# print(result1)
# print(result2)

