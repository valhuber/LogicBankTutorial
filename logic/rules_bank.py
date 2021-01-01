from logic_bank.logic_bank import Rule
from db.models import Customer, Order, Payment, PaymentAllocation


def declare_logic():
    """
    activate, then rules applied on commit

    automatically invoked, ordered and optimized
    """

    # rules go here.

