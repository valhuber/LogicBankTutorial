from logic_bank.logic_bank import Rule
from db.models import Customer, Order, Payment, PaymentAllocation


def declare_logic():
    """
    rules applied on commit

    automatically invoked, ordered and optimized
    """

    Rule.constraint(validate=Customer,
                    error_msg="balance ({row.Balance}) exceeds 2000)",
                    as_condition=lambda row: row.Balance <= 2000)

    Rule.sum(derive=Customer.Balance, as_sum_of=Order.AmountOwed)
