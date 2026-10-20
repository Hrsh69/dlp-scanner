"""Financial data detection rules."""

import re

from dlp_scanner.detectors.validators import luhn_ok
from dlp_scanner.models import DetectionRule

VISA = DetectionRule(
    rule_id="FIN_CREDIT_CARD_VISA",
    rule_name="Visa card number",
    pattern=re.compile(r"\b4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b"),
    base_score=0.6,
    context_keywords=["card", "visa", "cc", "payment", "credit"],
    validator=luhn_ok,
    compliance_frameworks=["PCI-DSS"],
)

RULES: list[DetectionRule] = [VISA]
