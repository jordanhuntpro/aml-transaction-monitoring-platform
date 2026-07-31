"""Generate synthetic customer and account data for the AML portfolio project."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path
from random import Random

import numpy as np
import pandas as pd
from faker import Faker


SEED = 42
NUM_CUSTOMERS = 1_000
OUTPUT_DIRECTORY = Path("data/generated")

CUSTOMER_TYPES = ("Individual", "Business")
RISK_RATINGS = ("Low", "Medium", "High")
COUNTRIES = ("United States", "Canada", "United Kingdom")
STATES = (
    "Virginia",
    "Maryland",
    "North Carolina",
    "South Carolina",
    "New Jersey",
    "Delaware",
    "Maine",
    "Florida",
    "Massachusetts",
    "New York",
)
INDUSTRIES = (
    "Technology",
    "Healthcare",
    "Retail",
    "Construction",
    "Transportation",
    "Professional Services",
    "Hospitality",
    "Manufacturing",
    "Real Estate",
    "Financial Services",
)


def create_random_date(
    rng: Random,
    start_date: date,
    end_date: date,
) -> date:
    """Return a reproducible random date within the supplied date range."""
    day_range = (end_date - start_date).days
    return start_date + timedelta(days=rng.randint(0, day_range))


def generate_customers(
    number_of_customers: int = NUM_CUSTOMERS,
    seed: int = SEED,
) -> pd.DataFrame:
    """Generate a reproducible synthetic customer dataset."""
    rng = Random(seed)
    faker = Faker("en_US")
    Faker.seed(seed)
    np.random.seed(seed)

    today = date.today()
    earliest_relationship_date = today - timedelta(days=15 * 365)

    customer_records: list[dict[str, object]] = []

    for customer_number in range(1, number_of_customers + 1):
        customer_type = rng.choices(
            CUSTOMER_TYPES,
            weights=(0.82, 0.18),
            k=1,
        )[0]

        risk_rating = rng.choices(
            RISK_RATINGS,
            weights=(0.70, 0.23, 0.07),
            k=1,
        )[0]

        country = rng.choices(
            COUNTRIES,
            weights=(0.90, 0.06, 0.04),
            k=1,
        )[0]

        state = rng.choice(STATES) if country == "United States" else ""

        if customer_type == "Individual":
            customer_name = faker.name()
            occupation_or_industry = faker.job()
            expected_monthly_volume = round(
                max(500.0, rng.lognormvariate(8.0, 0.75)),
                2,
            )
            expected_transaction_count = rng.randint(8, 75)
        else:
            customer_name = faker.company()
            occupation_or_industry = rng.choice(INDUSTRIES)
            expected_monthly_volume = round(
                max(5_000.0, rng.lognormvariate(10.0, 0.85)),
                2,
            )
            expected_transaction_count = rng.randint(35, 250)

        customer_records.append(
            {
                "customer_id": f"CUST{customer_number:06d}",
                "customer_name": customer_name,
                "customer_type": customer_type,
                "customer_risk_rating": risk_rating,
                "country": country,
                "state": state,
                "occupation_or_industry": occupation_or_industry,
                "customer_since": create_random_date(
                    rng,
                    earliest_relationship_date,
                    today,
                ),
                "expected_monthly_volume": expected_monthly_volume,
                "expected_transaction_count": expected_transaction_count,
                "is_pep": rng.random() < 0.01,
                "adverse_media_flag": rng.random() < 0.02,
                "sanctions_flag": rng.random() < 0.002,
            }
        )

    return pd.DataFrame(customer_records)


def save_dataframe(
    dataframe: pd.DataFrame,
    filename: str,
) -> Path:
    """Save a dataframe as a CSV file and return the output path."""
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIRECTORY / filename
    dataframe.to_csv(output_path, index=False)
    return output_path


def main() -> None:
    """Generate and save the initial synthetic customer dataset."""
    customers = generate_customers()
    output_path = save_dataframe(customers, "customers.csv")

    print(f"Generated {len(customers):,} synthetic customers.")
    print(f"Saved customer data to: {output_path}")
    print()
    print("Customer risk distribution:")
    print(customers["customer_risk_rating"].value_counts())
    print()
    print("Customer type distribution:")
    print(customers["customer_type"].value_counts())


if __name__ == "__main__":
    main()