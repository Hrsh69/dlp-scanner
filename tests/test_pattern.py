from dlp_scanner.detectors.pattern import PatternDetector
from dlp_scanner.detectors.rules.financial import RULES


def detect(text, allowlist=None):
    return list(PatternDetector(RULES, allowlist).detect(text))


def test_finds_valid_visa():
    matches = detect("card: 4539 1488 0343 6467 thanks")
    assert len(matches) == 1
    assert matches[0].rule_id == "FIN_CREDIT_CARD_VISA"
    assert matches[0].matched_text == "4539 1488 0343 6467"


def test_rejects_luhn_failure():
    assert detect("order id 4539148803436468") == []


def test_ignores_non_visa_prefix():
    assert detect("number 5539148803436467") == []


def test_allowlist_suppresses_match():
    text = "test card 4111111111111111"
    assert len(detect(text)) == 1
    assert detect(text, frozenset({"4111111111111111"})) == []


def test_match_offsets():
    text = "x 4111111111111111 y"
    m = detect(text)[0]
    assert text[m.start : m.end] == "4111111111111111"
