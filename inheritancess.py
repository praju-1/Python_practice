class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name of the employee : ", self.name)
        print("Age of the employee : ", self.age)

# e = Employee("john", 21)
# e.info()

class Trainer(Employee):
    def __init__(self, name, age, job):
        Employee.__init__(self, name, age)
        self.job = job

    def info(self):
        Employee.info(self)
        print("Job role of employee is : ", self.job)

# t = Trainer("John", 21, "Trainer")
# t.info()

class Manager(Trainer):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age, job)
        self.salary = salary

    def info(self):
        print("Salary of manager : ", self.salary)
        return super().info()
    
m = Manager("John", 21, "Trainer", 400000)
m.info()