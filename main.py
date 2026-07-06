import re

text = "axxxxxbaxxxb"
pattern = r"a.*b"

matches = re.findall(pattern, text)
print(f'Найденные подстроки: {matches}')