# ---------file system

f = open("doc.txt")  # read file
for lines in f:
    print(lines)
f.close()


# "a"  for append text to end of file
# 'w'  for over write the content
a = open("doc.txt",'a')
a.write("i also do freelanceing")
a.close()

ope = open('doc.txt')
print(ope.read())

# print(f.readline())
# print(f.readline())
