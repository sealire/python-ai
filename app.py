import re

text = '12dafdf32'

if re.search(r'\d', text):
    print(True)