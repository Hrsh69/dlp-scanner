"""Checksum validators used to confirm regex candidates."""


def luhn_ok(value: str) -> bool:
    """Return True if the digits in `value` pass the Luhn checksum."""
    digits = [int(c) for c in value if c.isdigit()]
    if len(digits) < 2:
        return False
    total = 0
    for i, n in enumerate(reversed(digits)):
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
