import logging

# Basic logging setup: prints to console with level, time, and message
logging.basicConfig(
    level=logging.INFO,  # change to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def leave_calc(base_salary):

    """Leave calculator"""
    leaves = float(input("no of leaves taken:"))
    sal_cut = 0
    if leaves >= 15:
        per_day = base_salary / 30

        sal_cut = per_day * (leaves - 15)

        logging.info(
            "Leaves taken: %.1f (>= 15). Per day: %.2f. Deduction: %.2f",
            leaves, per_day, sal_cut
        )

    return sal_cut
