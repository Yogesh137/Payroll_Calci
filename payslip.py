from typing import Dict
from employee import Employee


class PaySlip:
    """
    Represents a generated payslip for an employee.
    """

    def __init__(
        self,
        employee: Employee,
        gross_pay: float,
        tax_amount: float,
        deductions: Dict[str, float],
        net_pay: float,
    ):
        self.employee = employee
        self.gross_pay = gross_pay
        self.tax_amount = tax_amount
        self.deductions = deductions
        self.net_pay = net_pay

    def __str__(self) -> str:
        deduction_lines = "\n".join(
            f"  {name}: ${amount:.2f}"
            for name, amount in self.deductions.items()
        )

        return (
            f"\n--- Payslip for {self.employee.name} ---\n"
            f"Employee ID: {self.employee.id}\n"
            f"Type: {self.employee.employee_type.value}\n"
            f"Gross Pay: ${self.gross_pay:.2f}\n"
            f"Tax: ${self.tax_amount:.2f}\n"
            f"Deductions:\n{deduction_lines if deduction_lines else '  None'}\n"
            f"Net Pay: ${self.net_pay:.2f}\n"
        )