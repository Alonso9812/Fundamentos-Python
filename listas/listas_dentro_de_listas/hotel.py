rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True

rooms[0][4][1] = False

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(f"Number of vacant rooms in the third floor: {vacancy}")
print(f"Room 1 on the second floor is {'occupied' if rooms[1][4][1] else 'vacant'}.")
print(f"Room 14 on the first floor is {'occupied' if rooms[0][9][13] else 'vacant'}.")
print(f"Room 13 on the second floor is {'occupied' if rooms[1][9][13] else 'vacant'}.")
print(f"Room 1 on the first floor is {'occupied' if rooms[0][4][1] else 'vacant'}.")

