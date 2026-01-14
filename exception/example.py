
"""ATM example showing a simple global balance with validation."""

BALANCE = 5000.0


def withdraw_money(amount: float) -> float:
    """Withdraw amount from the global BALANCE and return the new balance.

    Raises:
        ValueError: If amount is not greater than zero.
        RuntimeError: If amount exceeds available balance.
    """
    global BALANCE
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > BALANCE:
        raise RuntimeError("Insufficient balance.")
    BALANCE -= amount
    return BALANCE


def main() -> None:
    """Run an ATM-like withdrawal flow using global BALANCE."""
    print("Welcome to the ATM")
    try:
        user_input = input("Enter the amount: ")
        requested_amount = float(user_input)

        remaining_bal = withdraw_money(requested_amount)
        print("Withdrawal successful")
        print(f"Remaining balance: ${remaining_bal:.2f}")

    except ValueError as ve:
        print("Input Error:", ve)

    except RuntimeError as re:
        print("Transaction Error:", re)

    else:
        print("Transaction completed without errors.")

    finally:
        print("\n--- SESSION CLOSED ---")
        print("Thank you for using the ATM!")


if __name__ == "__main__":
    main()
