"""Regex matching with checksum validation and allowlist filtering."""

from collections.abc import Iterator

from dlp_scanner.models import DetectionRule, DetectorMatch


class PatternDetector:
    def __init__(
        self,
        rules: list[DetectionRule],
        allowlist: frozenset[str] | None = None,
    ) -> None:
        self._rules = rules
        self._allowlist = allowlist or frozenset()

    def detect(self, text: str) -> Iterator[DetectorMatch]:
        for rule in self._rules:
            for m in rule.pattern.finditer(text):
                value = m.group()
                if value in self._allowlist:
                    continue
                if rule.validator is not None and not rule.validator(value):
                    continue
                yield DetectorMatch(
                    rule_id=rule.rule_id,
                    rule_name=rule.rule_name,
                    start=m.start(),
                    end=m.end(),
                    matched_text=value,
                    score=rule.base_score,
                    context_keywords=rule.context_keywords,
                    compliance_frameworks=rule.compliance_frameworks,
                )
