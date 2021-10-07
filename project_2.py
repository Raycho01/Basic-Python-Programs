

windows_serial_number = "abc-def-ghi-jkl"

var1 = windows_serial_number[0:3]
var2 = windows_serial_number[4:7]
var3 = windows_serial_number[8:11]
var4 = windows_serial_number[12:15]

print(var1 +" " +var2 +" " +var3 +" " +var4)

var1 = var1.replace('abc', 'aaa')
var2 = var2.replace('def', 'bbb')
var3 = var3.replace('ghi', 'ccc')
var4= var4.replace('jkl', 'ddd')
print(var1 +" " +var2 +" " +var3 +" " +var4)

encoded_serial_numb = var1 +"-" +var2 +"-" +var3 +"-" +var4
print(encoded_serial_numb)

justnumber = 2
print(str(justnumber) +" " +encoded_serial_numb)

justdiffnumber = 5**2
print(justdiffnumber)

hardnumb = 1.12345678
print("%.2f" % hardnumb)

hardnumb_in_int = int(hardnumb)
print(hardnumb_in_int)

hardnumb_in_int_in_float = float(hardnumb_in_int)
print(hardnumb_in_int_in_float)

array_one = ["One", "Two", "Three"]
print(array_one)

array_one.append("Four")
print(array_one)