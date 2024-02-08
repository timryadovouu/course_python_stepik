#именованные срезы
person = ('Alex', 'Smith', "May", 10, 1980)
NAME, BIRTHDAY = slice(None, 2), slice(2, None)
print(person[NAME])
print(person[BIRTHDAY])