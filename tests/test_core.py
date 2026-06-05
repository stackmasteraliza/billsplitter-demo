"""Tests for billsplitter core math."""

import pytest

from billsplitter import split_bill, format_currency, per_person_with_tip


def test_format_currency():
    assert format_currency(12.5) == "$12.50"
    assert format_currency(0) == "$0.00"


def test_split_no_tip():
    # $100 split 4 ways, no tip -> $25 each
    assert split_bill(100, 4, tip_percent=0) == 25.00


def test_split_with_tip():
    # $100 split 4 ways with a 20% tip -> $120 total -> $30 each
    assert split_bill(100, 4, tip_percent=20) == 30.00


def test_per_person_includes_tip():
    # $50, 2 people, 10% tip -> $55 total -> $27.50 each
    assert per_person_with_tip(50, 2, 10) == 27.50


def test_invalid_people():
    with pytest.raises(ValueError):
        split_bill(100, 0)
