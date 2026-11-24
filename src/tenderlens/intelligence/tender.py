
from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    field_validator,
    model_validator,
)


class TenderStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    CANCELLED = "cancelled"
    AWARDED = "awarded"
    UNKNOWN = "unknown"


class Tender(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    id: UUID = Field(default_factory=uuid4)

    reference_number: str = Field(min_length=1, max_length=150)
    title: str = Field(min_length=5, max_length=500)
    organisation: str = Field(min_length=2, max_length=250)
    location: str | None = None

    published_at: datetime | None = None
    submission_deadline: datetime | None = None

    estimated_value: Decimal | None = Field(default=None, ge=0)
    emd_amount: Decimal | None = Field(default=None, ge=0)
    currency: str = Field(default="INR", pattern=r"^[A-Z]{3}$")

    status: TenderStatus = TenderStatus.UNKNOWN
    source_url: HttpUrl | None = None

    @field_validator("reference_number", "title", "organisation")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        normalized = value.strip()

        if not normalized:
            raise ValueError("This field cannot be empty or whitespace.")

        return normalized

    @field_validator("published_at", "submission_deadline")
    @classmethod
    def validate_timezone(cls, value: datetime | None) -> datetime | None:
        if value is not None and (
            value.tzinfo is None or value.utcoffset() is None
        ):
            raise ValueError("Datetime values must include a timezone.")

        return value

    @model_validator(mode="after")
    def validate_tender_dates(self):
        if (
            self.published_at is not None
            and self.submission_deadline is not None
            and self.submission_deadline <= self.published_at
        ):
            raise ValueError(
                "Submission deadline must be after publication."
            )

        return self
