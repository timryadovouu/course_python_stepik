import re

result = re.split(r'(/)', '/beegeek/stepik/python/')

print(result)

text = 'bee     geek py  stepik          python'
result1 = text.split()
result2 = text.split(' ')
print(result1, result2)

text = '''bee geek
stepik python'''
print(text.split())

result = re.split(r'\D+', '1 + 2 - 3 =')

print(result)


print(re.split(r"(?:---|\+\+\+)", "'Timur---Arthur+++Dima****Anri'"))