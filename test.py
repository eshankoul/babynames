import re

f = open('baby1990.html','r')
names = f.read()
#print(names)
year=0
year = re.findall(r'(\d\d\d\d)</h3>',names)
extract=[]
extract.append(year[0])
#print(extract)

tuples= re.findall(r'<td>([\w]+)</td>+<td>([\w]+)</td>',names)
for tuple in tuples:
    print(tuple[1]+' '+str(tuple[0]))
    extract.append(tuple[1]+' '+str(tuple[0]))


print(extract)