f = open("test.json", "w+")

for i in range(100):
    f.writelines(str(i))

f.close()