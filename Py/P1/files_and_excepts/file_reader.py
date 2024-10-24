filename = 'mytextfile.txt'

# with open(filename, encoding='utf-16') as file_object:
#     lines = file_object.readlines()
    # for line in file_object:
    #     print(line.rstrip())
    
# for line in lines:
#     print(line.replace('python', 'c++').rstrip())

with open(filename, 'a', encoding='utf-16') as file_object:
    file_object.write('This is a new line.\n')
    file_object.write('This is another line.\n')
    file_object.write('This is yet another line.\n')
    file_object.write('This is the final line.\n')




