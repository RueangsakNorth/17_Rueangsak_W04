number = [12, 34, 56, 78, 90]
divisor = 6
print(f"ตัวที่หาร{divisor} ลงตัว :")
found = 0
for i in number:
    if i % divisor == 0:
        print(f"{i} ลงตัว(={i // divisor})")
        found += 1
        if found == 3:
             break