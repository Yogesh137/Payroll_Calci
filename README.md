# Payroll_Calci
## Overview

This project implements a modular payroll processing system in Python.
It calculates monthly salaries for employees based on employment type, applies progressive tax brackets, and computes applicable deductions to generate detailed payslips.

The system is designed with clean separation of responsibilities and follows object-oriented design principles.

## Features

### Supports three employee types:

FULL_TIME (fixed monthly salary)

PART_TIME (hourly rate × hours worked, maximum 120 hours per month)

CONTRACTOR (daily rate × days worked)

### Progressive tax calculation:

$0 – $1000 → 0%

$1001 – $3000 → 10%

$3001 – $5000 → 20%

Above $5000 → 30%

### Deductions supported:

Health Insurance ($150, FULL_TIME only)

Retirement Contribution (5% of gross, optional)

Union Dues ($50, optional)

All monetary values rounded to 2 decimal places

Input validation for negative values and hour limits

Detailed payslip generation per employee

## Project Structure

Payroll_Calci/
│
├── employee.py
├── payslip.py
├── payroll_processor.py
└── main.py

### employee.py Defines:

EmployeeType (Enum)

Employee class (data model)

### payslip.py Defines:

PaySlip class representing calculated payroll results

### payroll_processor.py Contains:

Gross pay calculation

Progressive tax logic

Deduction computation

Payslip generation

Monthly payroll processing

### main.py

Demonstrates system usage with multiple employees covering:

All employee types

Different deduction combinations

## Design Decisions

### Progressive Tax

Tax is calculated progressively per bracket rather than applying a flat rate to total income. Each income portion is taxed according to its bracket.

### Separation of Concerns

Employee represents data only.

PayrollProcessor contains business logic.

PaySlip represents the result of calculations.

This ensures maintainability and easier future extension.

### Validation

Part-time employees cannot exceed 120 hours.

Negative hours or rates raise exceptions.

Rounding is centralized to maintain consistency.
