from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC","Dhaka")

eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim",eight)
karim = Student("Karim",nine)
fahim = Student("Fahim",ten)
hamim = Student("Hamim",ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

abul = Teacher("Abul khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

bangla = Subject("Bangla",abul)
physics = Subject("Physics",babul)
chemistry = Subject("Chemistry",kabul)
biology = Subject("Biology",kabul)

eight.add_subj(bangla)
eight.add_subj(physics)
eight.add_subj(chemistry)
nine.add_subj(biology)
nine.add_subj(physics)
nine.add_subj(chemistry)
ten.add_subj(chemistry)
ten.add_subj(physics)
ten.add_subj(bangla)
ten.add_subj(biology)

eight.take_sem_final()
nine.take_sem_final()
ten.take_sem_final()
print(school)