
# ====== 14-10-2026 ======

# read()

file = open("file_handling_demo.txt", mode="r")
read_data = file.read()
print(read_data)
file.close()


# readline()

file = open("file_handling_demo.txt", mode="r")
read_data = file.readline()
print(read_data)
file.close()


# readlines()

file = open("file_handling_demo.txt", mode="r")
read_data = file.readlines()
print(read_data)
file.close()


# write() - append mode (a)

file = open("file_handling_demo.txt", mode="a")
write_data = file.write("\nThis is append operation by using mode a")
file.close()


# write() - write mode (w)

file = open("file_handling_demo2.txt", mode="w")
write_data = file.write("This is write operation using mode w")
file.close()


# writelines()

voter_data = ["\nvasu\n", "kiran\n","kumar\n","srinu"]
file = open("file_handling_demo2.txt", mode="a")
write_data = file.writelines(voter_data)
file.close()


# w+ mode - write and read

file = open("demo123.txt", mode="w+")
file.write("This is write operation using w+")
file.seek(0)
read_data = file.read()
print(read_data)
file.close()


# r+ mode - read and write

file = open("file_handling_demo.txt", mode="r+")
read_data = file.read()
print(read_data)
file.seek(0)
file.write("Hello Python")
file.close()


# a+ mode - append and read

file = open("demo123.txt", mode="a+")
file.write("\nThis is append operation using a+")
file.seek(0)
read_data = file.read()
print(read_data)
file.close()
