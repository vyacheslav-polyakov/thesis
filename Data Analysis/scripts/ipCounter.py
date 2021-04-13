file = open('575ips.txt', 'r', encoding = 'utf-16')
count = 0
for line in file:
    count += 1
print(count)
file.close()
