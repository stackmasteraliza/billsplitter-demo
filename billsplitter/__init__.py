"""billsplitter — split a restaurant bill fairly, with tip and rounding."""

from billsplitter.core import split_bill, format_currency, per_person_with_tip

__version__ = "0.1.0"

__all__ = ["split_bill", "format_currency", "per_person_with_tip"]
