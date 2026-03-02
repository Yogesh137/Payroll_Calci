from typing import List, Dict
from employee import Employee, EmployeeType
from payslip import PaySlip


class PayrollProcessor:
    """
    Handles payroll calculations including gross pay, tax,
    deductions, and payslip generation.
    """

    MAX_PART_TIME_HOURS = 120
    HEALTH_INSURANCE = 150.0
    UNION_DUES = 50.0
    RETIREMENT_RATE = 0.05

    @staticmethod
    def _round(value: float) -> float:
        return round(value, 2)

    def calculate_gross_pay(self, employee: Employee, units: float) -> float:
        """
        Calculates gross pay based on employee type.
        units = hours (PART_TIME) or days (CONTRACTOR)
        ignored for FULL_TIME
        """

        if units < 0:
            raise ValueError("Hours/Days worked cannot be negative.")

        if employee.employee_type == EmployeeType.FULL_TIME:
            gross = employee.pay_rate

        elif employee.employee_type == EmployeeType.PART_TIME:
            if units > self.MAX_PART_TIME_HOURS:
                raise ValueError("Part-time employee cannot exceed 120 hours.")
            gross = employee.pay_rate * units

        elif employee.employee_type == EmployeeType.CONTRACTOR:
            gross = employee.pay_rate * units

        else:
            raise ValueError("Invalid employee type.")

        return self._round(gross)

    def calculate_tax(self, gross_pay: float) -> float:
        """
        Progressive tax calculation.
        """

        tax = 0.0

        brackets = [
            (1000, 0.00),
            (3000, 0.10),
            (5000, 0.20),
            (float("inf"), 0.30),
        ]

        previous_limit = 0

        for limit, rate in brackets:
            if gross_pay > previous_limit:
                taxable_amount = min(gross_pay, limit) - previous_limit
                tax += taxable_amount * rate
                previous_limit = limit
            else:
                break

        return self._round(tax)

    def calculate_deductions(
        self, employee: Employee, gross_pay: float
    ) -> Dict[str, float]:

        deductions = {}

        if employee.employee_type == EmployeeType.FULL_TIME:
            deductions["Health Insurance"] = self.HEALTH_INSURANCE

        if employee.has_retirement:
            deductions["Retirement Contribution"] = self._round(
                gross_pay * self.RETIREMENT_RATE
            )

        if employee.is_union_member:
            deductions["Union Dues"] = self.UNION_DUES

        return deductions

    def generate_payslip(self, employee: Employee, units: float) -> PaySlip:
        gross = self.calculate_gross_pay(employee, units)
        tax = self.calculate_tax(gross)
        deductions = self.calculate_deductions(employee, gross)

        total_deductions = sum(deductions.values())
        net = gross - tax - total_deductions

        return PaySlip(
            employee=employee,
            gross_pay=gross,
            tax_amount=tax,
            deductions=deductions,
            net_pay=self._round(net),
        )

    def process_monthly_payroll(
        self, employee_units_map: Dict[Employee, float]
    ) -> List[PaySlip]:

        if not employee_units_map:
            raise ValueError("Employee list cannot be empty.")

        payslips = []

        for employee, units in employee_units_map.items():
            payslip = self.generate_payslip(employee, units)
            payslips.append(payslip)

        return payslips