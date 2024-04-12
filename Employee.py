
"""Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.
class Employee:
    def __init__(self, emp_id, name, position, salary):
        if not isinstance(emp_id, int) or emp_id <= 0:
            raise ValueError("Invalid employee ID")
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid employee name")
        if not isinstance(position, str) or not position:
            raise ValueError("Invalid employee position")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Invalid salary")

        self._emp_id = emp_id
        self._name = name
        self._position = position
        self._salary = salary
        self._tasks = []

    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, emp_id):
        if not isinstance(emp_id, int) or emp_id <= 0:
            raise ValueError("Invalid employee ID")
        self._emp_id = emp_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid employee name")
        self._name = name

    def get_position(self):
        return self._position

    def set_position(self, position):
        if not isinstance(position, str) or not position:
            raise ValueError("Invalid employee position")
        self._position = position

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Invalid salary")
        self._salary = salary

    def get_tasks(self):
        return self._tasks

    def add_task(self, task):
        self._tasks.append(task)

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)

    def __str__(self):
        return f"Employee ID: {self._emp_id}, Name: {self._name}, Position: {self._position}, Salary: ${self._salary}, Tasks: {', '.join(self._tasks)}"






def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
