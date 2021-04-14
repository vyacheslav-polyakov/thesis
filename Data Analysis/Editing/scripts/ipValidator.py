file = open('575ips.txt', 'r', encoding='utf-16')
ips = []
rep = []
try:
    for line in file:
        if line in ips:
            rep.append(line)
        else:
            ips.append(line)
    print(rep)
except:
    pass
finally:
    file.close()
