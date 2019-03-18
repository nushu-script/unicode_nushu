#!/usr/bin/env python3

import pandas
from collections import defaultdict
import json

d = defaultdict(list)
data = pandas.read_csv('data.csv')
for v, ks in zip(data['女书字符'], data['对应汉字']):
    for k in ks:
        d[k].append(ord(v))
print(json.dumps(d, ensure_ascii=False, sort_keys=True).replace('], ', '],\n'))
