# currency.py

# Fixed conversion rates (example rates — update as needed)
RUPEE_TO_DOLLAR = 0.012
RUPEE_TO_EURO = 0.011
RUPEE_TO_POUND = 0.0095
RUPEE_TO_YEN = 1.80


def toDollar(rupees):
    """
    Convert Rupees to US Dollars
    """
    return rupees * RUPEE_TO_DOLLAR


def toEuro(rupees):
    """
    Convert Rupees to Euro
    """
    return rupees * RUPEE_TO_EURO


def toPound(rupees):
    """
    Convert Rupees to British Pound
    """
    return rupees * RUPEE_TO_POUND


def ToYen(rupees):
    """
    Convert Rupees to Japanese Yen
    """
    return rupees * RUPEE_TO_YEN


    