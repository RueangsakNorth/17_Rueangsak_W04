# Sort เรียงลำดับข้อมูล
numbers = [5, 2, 9, 1, 5, 6]
numbers_copy = numbers # สร้างสำเนาของ list
numbers.sort()  # เรียงลำดับจากมากไปน้อย
print(numbers_copy)  # Output: [5, 5, 6, 9]
numbers_copy.sort(reverse=True)  # เรียงลำดับจากน้อยไปมาก