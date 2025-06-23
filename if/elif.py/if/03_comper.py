# num_1 = 10
# num_2 = 20
# print(f'{num_1 == num_2}:')

fruits = ['apple', 'banana', 'cherry']
find_fruit = str(input("กรุณาใส่ชื่อผลไม้ที่ต้องการค้นหา: "))
if find_fruit in fruits:
    position = fruits.index(find_fruit)
    print(f"มี {find_fruit} อยู่ที่ตำแหน่ง {position}")
else:
    print(f"ไม่มี {find_fruit} ในรายการผลไม้")