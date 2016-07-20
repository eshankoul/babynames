import re
#filename = input("Enter the file name\n")
f = open('baby1990.html','r')
names = f.read()
#print(names)
year=0
year = re.findall(r'(\d\d\d\d)</h3>',names)
extract=[]
extract.append(year[0])
#print(extract)

tuples= re.findall(r'<td>([\w]+)</td>+<td>([\w]+)</td>+<td>([\w]+)</td>',names)
dict={}
for tuple in tuples:
    if tuple[1] not in dict:
        dict[tuple[1]]=tuple[0]
    if tuple[2] not in dict:
        dict[tuple[2]]=tuple[0]

    # print(tuple[1]+' '+str(tuple[0]))
    # extract.append(tuple[1]+' '+str(tuple[0]))

dict_final=sorted(dict.keys())
for name in dict_final:
    extract.append(name+' '+dict[name])
print(extract)