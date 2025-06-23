# ค้นหาและเรียงลำดับใน Python Search and Sort
numbers = [5, 2, 9, 1, 5, 6]
if 5 in numbers:  # ตรวจสอบว่ามี 5 ใน list หรือไม่
    position = numbers.index(5)  # ค้นหาตำแหน่งของ 5
    print(f"5 is found at position {position}")  