import pytest

from dlp_scanner.detectors.validators import luhn_ok


@pytest.mark.parametrize(
    "value",
    ["4539148803436467", "4539 1488 0343 6467", "4111-1111-1111-1111"],
)
def test_luhn_valid(value):
    assert luhn_ok(value) is True


@pytest.mark.parametrize(
    "value",
    ["4539148803436468", "1234567812345678", "", "7"],
)
def test_luhn_invalid(value):
    assert luhn_ok(value) is False
