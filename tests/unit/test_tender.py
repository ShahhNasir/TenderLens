
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from pydantic import ValidationError

from tenderlens.intelligence.tender import (
    Tender,
    TenderStatus,
)


def test_create_valid_tender():

    tender = Tender(
        reference_number="NIC/2026/IT/1042",
        title="Enterprise Document Management System",
        organisation="National Informatics Centre",
        published_at=datetime(
            2026, 11, 20, 10, 0,
            tzinfo=timezone.utc,
        ),
        submission_deadline=datetime(
            2026, 12, 15, 17, 0,
            tzinfo=timezone.utc,
        ),
        estimated_value=Decimal("5000000"),
        emd_amount=Decimal("100000"),
        status=TenderStatus.ACTIVE,
    )

    assert tender.reference_number == "NIC/2026/IT/1042"

    assert tender.status == TenderStatus.ACTIVE

    assert tender.estimated_value == Decimal("5000000")

    assert tender.id is not None


def test_tender_rejects_negative_value():

    with pytest.raises(ValidationError):

        Tender(
            reference_number="NIC-001",
            title="Enterprise Software Development",
            organisation="National Informatics Centre",
            estimated_value=Decimal("-500"),
        )


def test_tender_rejects_invalid_status():

    with pytest.raises(ValidationError):

        Tender(
            reference_number="NIC-001",
            title="Enterprise Software Development",
            organisation="National Informatics Centre",
            status="banana",
        )


def test_tender_rejects_deadline_before_publication():

    with pytest.raises(ValidationError):

        Tender(
            reference_number="NIC-001",
            title="Enterprise Software Development",
            organisation="National Informatics Centre",
            published_at=datetime(
                2026, 12, 15,
                tzinfo=timezone.utc,
            ),
            submission_deadline=datetime(
                2026, 12, 10,
                tzinfo=timezone.utc,
            ),
        )


def test_tender_rejects_naive_datetime():

    with pytest.raises(ValidationError):

        Tender(
            reference_number="NIC-001",
            title="Enterprise Software Development",
            organisation="National Informatics Centre",
            published_at=datetime(2026, 11, 20),
            submission_deadline=datetime(
                2026, 12, 15,
                tzinfo=timezone.utc,
            ),
        )


def test_tender_strips_whitespace():

    tender = Tender(
        reference_number="  NIC-001  ",
        title="  Enterprise Software Development  ",
        organisation="  National Informatics Centre  ",
    )

    assert tender.reference_number == "NIC-001"

    assert tender.title == "Enterprise Software Development"

    assert tender.organisation == "National Informatics Centre"
