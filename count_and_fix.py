with open('original.txt') as file_object:
    contents = file_object.read()
    contents1 = contents.replace(' i ', ' I ')
    contents2 = contents1.replace('-i-', '-I-')
    contents3 = contents2.replace('i ', 'I ')
    contents4 = contents3.replace(' i', ' I')
    f_contents = open('changed.txt', 'w')
    f_contents.write(contents4)

diff = 0
for char_a, char_b in zip(contents, contents4):
    if char_a != char_b:
        diff = diff + 1
print(f'There are {diff} errors')