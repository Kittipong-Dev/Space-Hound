import pygame

# making label
4*1
3*10
1*9

amour = {}

x = 0
y = 0
for i in range(4):
    amour[i] = {'pos' : (x, y), 'item' : ''}
    y += 16

print(amour)
print('\n\n\n')

inventory = {}

x = 0
y = 0
for i in range(30):
    inventory[i] = {'pos' : (x, y), 'item' : ''}
    x += 16
    if x == 160:
        x = 0
        y += 16
        

print(inventory)
print('\n\n\n')

equipment = {}

x = 0
y = 0
for i in range(9):
    equipment[i] = {'pos' : (x, y), 'item' : ''}
    x += 16

equipment[0]['item'] = 'ore extractor'
print(equipment)
print('\n\n\n')

# need to create rect function
# pygame.Rect(l, t, w, h)

# int(//size)
# if holding remove pos blit on mpos if not holding detect mpos then // 16 then blit on that pos 

# like tilemap that snaps


a = {-3, -2, -1, 0, 1, 2, 3}
axa = set()
for x in a:
    for y in a:
        axa.add((x, y))

print(axa)
print("\n\n")
print(len(axa))

r1 = set()

for member in axa:
    x, y = member
    if x**2 + y ** 2 < 8:
        r1.add(member)

print(r1)
print("\n\n")
print(len(r1))

r2 = set()

for member in axa:
    x, y = member
    if not (abs(x) == 3 or abs(y) == 3 or (abs(x) == 2 and abs(y) == 2)):
        r2.add(member)

print(r2 == r1)