import random

def get_vehicle_value(vin, year, make, model, mileage):
    # Placeholder logic until data providers are wired up.
    base_value = random.randint(5000, 45000)
    confidence = round(random.uniform(0.6, 0.95), 2)

    return {
        "vin": vin,
        "vehicle": f"{year or 'Unknown'} {make or ''} {model or ''}".strip(),
        "mileage": mileage,
        "estimated_value": base_value,
        "confidence": confidence,
        "summary": f"Estimated value ${base_value:,} with confidence {int(confidence*100)}%"
    }
