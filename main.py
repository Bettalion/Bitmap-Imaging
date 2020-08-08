f = open('Bitmap_T.txt','r')
pcontents = f.readlines()
print(pcontents)
contents=[]
for element in pcontents:
  check = element[len(element)-1:]
  if check == '\n':
    element= element[:len(element)-1]
  contents.append(element)
print(contents)

