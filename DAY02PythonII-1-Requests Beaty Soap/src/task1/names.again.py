# Допиши класс Student
# В классе два поля: name, surname
# И два метода: __init__, get_full_name
class Student:
    
    # Инициализируй поля name и surname (НО сначала опиши их в классе)
    def __init__(self, name, surname):
         self.name = name
         self.surname = surname
         
    # Метод должен возвращать строку следующего вида
    # "name surname"
    # пробел обязателен!
    def get_full_name(self):
        return f'{self.name} {self.surname}'

# Считай имена из файла names.txt
# И создай на каждую строку по объекту класса Student
student_objects = []

with open('../../materials/task1/names.txt', 'r') as file:
    for row in file:
        line = row.split()
        student_objects.append(Student(line[0], line[1]))
    # line_count = sum(1 for line in file)
    
    # for i 
    # ne.strip())
    #     student_objects[i] = Student(line[0], line[1])
    # print(student_objects)  
        
new_list = [i.get_full_name() for i in student_objects]

# Отсортируй студентов в алфавитном порядке
# Запиши в файл sorted_names.txt
with open('../../src/task1/sorted_names.txt', 'w') as file:
    new_list.sort()
    for i in new_list:
        print(f"{i}", file=file)
        
new_dict= {i:new_list.count(i) for i in new_list}

# Создай словарь: ключ - Имя, значение - сколько раз встречается в файле names.txt
