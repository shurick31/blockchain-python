f = open('demo.txt', mode='r')
# file_content = f.readlines()
# # f.write('Add this content \n')
# f.close()
# print(file_content)

# print(f.readline())
# f.close()

line = f.readline()

while line:
    print(line)
    line = f.readline()

f.close()