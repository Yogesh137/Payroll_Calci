from employee import Employee, EmployeeType
from payroll_processor import PayrollProcessor


def main():
    processor = PayrollProcessor()

    employees = {
        Employee(1, "Alice", EmployeeType.FULL_TIME, 4000, True, True): 0,
        Employee(2, "Bob", EmployeeType.FULL_TIME, 2500, False, False): 0,
        Employee(3, "Charlie", EmployeeType.PART_TIME, 20, True, False): 100,
        Employee(4, "David", EmployeeType.PART_TIME, 25, False, True): 80,
        Employee(5, "Eve", EmployeeType.CONTRACTOR, 300, True, True): 15,
        Employee(6, "Frank", EmployeeType.CONTRACTOR, 200, False, False): 18,
    }

    payslips = processor.process_monthly_payroll(employees)

    for slip in payslips:
        print(slip)


if __name__ == "__main__":
    main()