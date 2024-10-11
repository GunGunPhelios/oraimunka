def sorter(*args):
    newlist= list(args)
    newlist.sort()
    print(newlist)
sorter(3,4,5,1,2,8,9)
def lowercaseof (anystring):
    temp= None
    return anystring.lower
for betu in anystring:
    if betu.islower():
        temp += betu.upper()
    else:
        temp+= betu.lower()
return temp

print(lowertoupper("KUtYa"))


print(lowercaseof("ADFGFDE"))
names = ["Bela", "Janos", "Ferenc", "Robert"]

names.sort(key=lowercaseof)
print(names)