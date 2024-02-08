from collections import defaultdict

# info = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# info1 = defaultdict(int, name='Timur', age=29, job='Teacher')
# info2 = defaultdict(int, [('name', 'Timur'), ('age', 29), ('job', 'Teacher')])
def first():
    data = [('Books', 1343), ('Books', 1166), ('Merch', 616),
            ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848),
            ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815),
            ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003),
            ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
    my_dict = defaultdict(int)
    for item in data:
        my_dict[item[0]] += item[1]
    [print(f"{item}: ${my_dict[item]}") for item in sorted(my_dict)]
    return True

def second():
    staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
             ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
             ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
             ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
             ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
             ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
             ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
             ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
             ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
             ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
             ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'),
             ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
             ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
             ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
             ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
             ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
             ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
    new_dict = defaultdict(int)
    for item in staff:
        new_dict[item[0]] += 1
    return "\n".join([f"{key}: {new_dict[key]}" for key in sorted(new_dict)])

def third():
    staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                    ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                    ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                    ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                    ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                    ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                    ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                    ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                    ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                    ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                    ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                    ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                    ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                    ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                    ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                    ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                    ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                    ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                    ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                    ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                    ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                    ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                    ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                    ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                    ('Accounting', 'Dale Houston')]
    new_dict = defaultdict(list)
    for item in staff_broken:
        if item[1] not in new_dict[item[0]]:
            new_dict[item[0]].append(item[1])
        else:
            continue
    return "\n".join([f"{key}: {', '.join(sorted(new_dict[key]))}" for key in sorted(new_dict)])

def wins(pairs):
    new_dict = defaultdict(set)
    for pair in pairs:
        new_dict[pair[0]].add(pair[1])
    return new_dict

def flip_dict(dict_of_lists):
    new_dict = defaultdict(list)
    for key in dict_of_lists.keys():
        for item in dict_of_lists[key]:
            new_dict[item].append(key)
    return new_dict

def best_sender(messages, senders):
    new_dict = defaultdict(int)
    for i in range(len(senders)):
        new_dict[senders[i]] += len(messages[i].split())
    return sorted(new_dict.items(), key=lambda line: (line[1], line[0]), reverse=True)[0][0]




