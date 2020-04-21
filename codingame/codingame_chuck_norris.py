import sys
import math

message = "Chuck Norris' keyboard has 2 keys: 0 and white space."
bin = ''
for i in message:
    bin += format(ord(i),'b')
if len(bin) < 8:
    zeros = 7 - len(bin)
    print("zer:" + str(zeros), file=sys.stderr)
    bin = '0'* zeros + bin 
    print("cur:" + str(bin), file=sys.stderr)

print(bin, file=sys.stderr)
stack = []
d = {
    '1': '0',
    '0': '00' 
     }

def top(s):
    if len(s) == 0:
        return -1
    return s[-1]

def popAndPrint(st):
    size = len(st)
    which = d[top(st)]
    return str(which) + ' ' +  '0' * size + ' '

# 1000011
rett = ''
for i in range(0, len(bin)):
    cur = bin[i]
    if len(stack) == 0:
        stack.append(cur)
    elif top(stack) == cur:
        stack.append(cur)
    elif top(stack) != cur:
        rett += popAndPrint(stack)
        stack = []
        stack.append(cur)
    else:
        print("ELSE", file=sys.stderr)
rett += popAndPrint(stack)
rett = rett[0:-1]
actual = "0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 0 0 000 00 0"
#index 90
print(rett, file=sys.stderr)
#print(actual[90:100], file=sys.stderr)
print("\n")

print(actual == rett)
