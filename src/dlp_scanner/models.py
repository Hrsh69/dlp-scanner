"""Core data models shared across the scanner."""

import re
from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Location:
    """Where a piece of text came from."""

    source_type: str
    uri: str
    line: int | None = None
    column: int | None = None
    byte_offset: int | None = None
    table_name: str | None = None
    column_name: str | None = None
    sheet_name: str | None = None


@dataclass(frozen=True, slots=True)
class TextChunk:
    """Extracted text paired with its origin."""

    text: str
    location: Location


@dataclass(frozen=True, slots=True)
class DetectionRule:
    """A specification of what to look for."""

    rule_id: str
    rule_name: str
    pattern: re.Pattern[str]
    base_score: float
    context_keywords: list[str] = field(default_factory=list)
    validator: Callable[[str], bool] | None = None
    compliance_frameworks: list[str] = field(default_factory=list)


@dataclass(frozen=True, slots=True)
class DetectorMatch:
    """A result: what was found and where in the text."""

    rule_id: str
    rule_name: str
    start: int
    end: int
    matched_text: str
    score: float
    context_keywords: list[str] = field(default_factory=list)
    compliance_frameworks: list[str] = field(default_factory=list)
