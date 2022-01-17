# 我应该怎么办呢
import os
import requests

if not os.path.exists('data'):
    os.makedirs('data')
csv_file = ''
for name in os.listdir('.'):
    if name.endswith('.csv'):
        csv_file = name
        break

assert csv_file

f = open(csv_file, 'r', encoding='utf-8', errors='ignore')
b = 5
i = b
s = requests.Session()
for line in f.readlines()[b:]:
    print('===', i, line.strip())
    temp = line.strip().split(',')
    frame, name, s3_url = temp[0], ','.join(temp[1:-1]), temp[-1]
    # urlretrieve(s3_url, 'data/{}'.format(name))
    r = s.get(s3_url)
    if r.status_code == 200:
        open('data/{}'.format(name), 'wb').write(r.content) # 将内容写入图片
        # print('load success !!!')
    else:
        print('load error !!!')
    i += 1
