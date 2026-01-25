d = {}
for i in range(4):
    name=input("Name:")
    lang=input("language:")
    d.update({name:lang})
print(d)

# if 2 languages are same the keys(name) are unchanged as they are still unique