import logging
from leave_cal import leave_calc

# Basic logging setup: prints to console with level, time, and message
logging.basicConfig(
    level=logging.INFO,  # change to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def salary_calc(designation, base_salary):

    """Salary calculator"""
    sal_cut = float(leave_calc(base_salary))
    salary = base_salary
    if designation == "coder":
        salary += (base_salary*0.1)
        logging.info("Designation: coder. Bonus: %.2f", base_salary*0.1)
    elif designation == "designer":
        salary += (base_salary*0.15)
        logging.info("Designation: designer. Bonus: %.2f", base_salary*0.1)
    elif designation == "manager":
        salary += (base_salary*0.05)
        logging.info("Designation: manager. Bonus: %.2f", base_salary*0.1)
    else:
        logging.warning("Wrong designation given: %s.", designation)
    return salary - sal_cut
