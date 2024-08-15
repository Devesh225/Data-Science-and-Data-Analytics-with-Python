person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    middle_skill = skills_list[middle_index]
    print(f"Middle skill: {middle_skill}")

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

skills = set(person['skills'])
if {'JavaScript', 'React'}.issubset(skills):
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print('He is a fullstack developer')
else:
    print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
