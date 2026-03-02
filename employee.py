from enum import Enum


class EmployeeType(Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACTOR = "CONTRACTOR"


class Employee:
    """
    Represents an employee in the payroll system.
    """

    def __init__(
        self,
        employee_id: int,
        name: str,
        employee_type: EmployeeType,
        pay_rate: float,
        is_union_member: bool = False,
        has_retirement: bool = False,
    ):
        if pay_rate < 0:
            raise ValueError("Pay rate cannot be negative.")

        self.id = employee_id
        self.name = name
        self.employee_type = employee_type
        self.pay_rate = pay_rate
        self.is_union_member = is_union_member
        self.has_retirement = has_retirement

    def __repr__(self) -> str:
        return (
            f"Employee(id={self.id}, name='{self.name}', "
            f"type={self.employee_type.value}, pay_rate={self.pay_rate})"
        )