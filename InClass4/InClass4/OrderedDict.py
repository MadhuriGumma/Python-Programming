import collections
student = [("Student_name", "Madhuri"),
        ("ID", 7),
        ("Class", 'Python prog'),
           ("College",'UMKC'),
        ("City",'Kansas city'),
        ("State", 'Missouri'),
        ("Country", 'USA')]

student = collections.OrderedDict(student)
print(student)