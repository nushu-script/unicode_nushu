from collections import defaultdict
import json

d = defaultdict(list)

with open('data.csv', encoding='utf-8') as f:
    next(f)  # skip header
    for line in f:
        女书字符, 字帖序, 对应汉字, 江永方言代表发音 = line.rstrip('\n').split(',')
        for ch in 对应汉字:
            d[ch].append(女书字符)

d = dict(sorted(((k, ''.join(vs)) for k, vs in d.items())))

s = json.dumps(d, ensure_ascii=False, indent=0)

with open('correspond.json', 'w', encoding='utf-8') as f:
    f.write(s)
