# src/rules.py

from datetime import date, timedelta
from holidays import is_bank_holiday

# =====================================================
# COLLECTION RULES
# =====================================================

# Monday=0 ... Sunday=6

BINS = [

    {
        "name": "Refuse Collection (General Rubbish)",
        "weekday": 4,  # Friday
        "interval_weeks": 3,
        "start_date": date(2026, 5, 15),
    },

    {
        "name": "Recycling Collection",
        "weekday": 4,  # Friday
        "interval_weeks": 3,
        "start_date": date(2026, 5, 8),
    },

    {
        "name": "Garden Waste Collection (Brown Bin)",
        "weekday": 2,  # Wednesday
        "interval_weeks": 3,
        "start_date": date(2026, 6, 3),
    },

    {
        "name": "Food Waste Collection",
        "weekday": 0,  # Monday
        "interval_weeks": 1,
        "start_date": date(2026, 6, 1),
    }

]

# =====================================================

def adjust_for_bank_holiday(d: date):

    if is_bank_holiday(d):
        return d + timedelta(days=1)

    return d

# =====================================================

def is_collection_day(bin_config, target_day):

    adjusted_day = adjust_for_bank_holiday(target_day)

    start = bin_config["start_date"]

    if adjusted_day.weekday() != bin_config["weekday"]:
        return False

    delta_days = (adjusted_day - start).days

    if delta_days < 0:
        return False

    weeks = delta_days // 7

    return weeks % bin_config["interval_weeks"] == 0

# =====================================================

def tomorrow_bins():

    tomorrow = date.today() + timedelta(days=1)

    result = []

    for b in BINS:

        if is_collection_day(b, tomorrow):

            result.append(b["name"])

    return result
