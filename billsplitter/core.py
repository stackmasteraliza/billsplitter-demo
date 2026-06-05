"""Core bill-splitting math."""


def format_currency(amount):
    """Format a number as a USD string, e.g. 12.5 -> '$12.50'."""
    return f"${amount:.2f}"


def per_person_with_tip(total, num_people, tip_percent):
    """Return the per-person share *including* tip.

    BUG: the tip is calculated but never added to the total, so everyone is
    undercharged. `split_bill` relies on this, so its tests fail too.
    """
    tip = total * (tip_percent / 100.0)  # noqa: F841  (computed but unused)
    return round(total / num_people, 2)


def split_bill(total, num_people, tip_percent=0):
    """Split `total` across `num_people`, adding `tip_percent` on top.

    Returns the amount each person owes, rounded to cents.
    """
    if num_people <= 0:
        raise ValueError("num_people must be positive")
    return per_person_with_tip(total, num_people, tip_percent)
