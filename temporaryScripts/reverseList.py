original = [[0x7c, 0x44, 0x7c], [0, 0, 0x7c], [0x5c, 0x54, 0x74], [0x54, 0x54, 0x7c], [0x70, 0x10, 0x7c], [0x74, 0x54, 0x5c], [0x7c, 0x54, 0x5c], [0x40, 0x40, 0x7c], [0x7c, 0x54, 0x7c], [0x74, 0x54, 0x7c]]
newer = []

for x in original:
    push = []
    for y in x:
        push.append(hex(int('{:08b}'.format(y)[::-1], 2)))
    newer.append(push)
print(newer)


