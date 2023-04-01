def has_required_skills(person, skills):
    return all(skill 
               in person['skills'] 
               for skill in skills)


john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

required_skills = ['Python', 'JavaScript']

print(has_required_skills(john, required_skills)) 
print(has_required_skills(jane, required_skills))