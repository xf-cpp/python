class Student():
    def __init__(self, name,number):
        self.name = name
        self.number = number
        self.grade = {'语文': 0, '英语': 0, '数学': 0}
    def set_attribute(self, name, number, grade_of_chinese, grade_of_english, grade_of_math):
        self.name = name
        self.number = number
        self.grade['语文'] = grade_of_chinese
        self.grade['数学'] = grade_of_math
        self.grade['英语'] = grade_of_english
    def show_attribute(self):
        print(f'学生姓名为：{self.name}\n, 学号为:{self.number}\n, 成绩为:{self.grade}')

if __name__ == '__main__':
    student1 = Student('xiaoming', '202100000001')
    print(student1.grade)
    student1.show_attribute()
    student1.set_attribute('lili', 1, 90, 90, 90)
    student1.show_attribute()







