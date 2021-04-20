from openpyxl import load_workbook as load

path = r'D:\Docs\Works\InProgress\Thesis\\'
src = path + 'data.xlsx'
dst = path + 'converted.xlsx'

wb1 = load(src)
ws1 = wb1.active

wb2 = load(dst)
ws2 = wb2.active
    
# 14
prob = {
    '不可能': 1,
    '不太可能': 2,
    '中立': 3,
    '可能': 4,
    '很大可能': 5
    }

# 6, 10, 11, 12, 13
agr = {
    '强烈反对': 1,
    '不同意': 2,
    '中性': 3,
    '同意': 4,
    '非常同意': 5
    }

# 7, 8
yn = {
    '否': 0,
    '是的': 1
    }

# 9
apr = {
    '强烈反对': 1,
    '不是很赞赏': 2,
    '中立': 3,
    '赞赏': 4,
    '非常赞赏': 5
    }

# 2
age = {
    '18岁以下': 1,
    '18~24岁': 2,
    '25~30岁': 3,
    '31~40岁': 4,
    '41~50岁': 5,
    '51~60岁': 6,
    '61岁及以上': 7
    }

# 3
time = {
    '1小时或以下': 1,
    '2小时': 2,
    '3小时': 3,
    '4小时': 4,
    '5小时': 5,
    '5小时以上': 6
    }

# 2
sex = {
    '女': 0,
    '男': 1
    }

# 5
dur = {
    '0小时': 1,
    '1-3小时': 2,
    '4-6小时': 3,
    '7-9小时': 4,
    '10小时以上': 5
    }

maps = {
    'af': prob,
    'ab': agr,
    'ac': agr,
    'ad': agr,
    'ae': agr,
    'x': agr,
    'y': yn,
    'z': yn,
    'aa': apr,
    't': age,
    'u': time,
    's': sex,
    'v': yn,
    'w': dur
    }

def Replace(dst_let, src_lets):
    global maps

    temp = []
    for let in src_lets:
        for row in range(2, 503):
            ans = ws1[let + str(row)].value
            val = maps[let][ans]
            temp.append(val)

    for i in range(0, len(temp)):
        ws2[dst_let + str(i+2)] = temp[i]

Replace('b', ['af']) # Y, Question 14
Replace('c', ['ab', 'ac', 'ad', 'ae']) # X1, Questions 10, 11, 12, 13
Replace('d', ['x']) # X2, Question 6
Replace('e', ['aa']) # X3, Question 9
Replace('f', ['y', 'z'])# X4, Questions 7, 8

Replace('g', ['t'])# X5, Question 2
Replace('h', ['u'])# X6, Question 3
Replace('i', ['s'])# X7, Question 1
Replace('j', ['v'])# X8, Question 4
Replace('k', ['w'])# X9, Question 5

wb2.save('results.xlsx')
