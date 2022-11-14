string = ""
overskrift=''
l=[]

for k in range(1, 11):
    overskrift = overskrift + "  " + str(k)
print("    ", overskrift)

for k in range(1, 11):
    for m in range(1, 11):
        string = string + "  " + str(m*k)
    print(k, ': ', string, '\n')
    string = ""