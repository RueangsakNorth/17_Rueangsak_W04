# len
txt_1 = "rueangsak_north!"
# len_txt_1 = len(txt_1)  # นับจำนวนตัวอักษรใน txt_1
# print(f"Length of txt_1: {len_txt_1}")  

pass_input = input("กรุณาใส่รหัสผ่าน: ")
if len(pass_input) < 8:
    print("รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร")
else:
    print("รหัสผ่านถูกต้อง")
