

def fee_calculation(gbp_amount):
    if 0 < gbp_amount < 299:
        fee = gbp_amount * 0.035

    elif 300 < gbp_amount < 749:
        fee = gbp_amount * 0.03

    elif 750 < gbp_amount < 999:
        fee = gbp_amount * 0.025

    elif 1000 < gbp_amount < 1999:
        fee = gbp_amount * 0.02

    else:
        fee = gbp_amount * 0.015

    return round(fee, 2)


def converter(currency, gbp_amount):

    if currency == 1 or currency == "USD":
        result = gbp_amount * 1.4
        result = round(result, 2)
        response = f"Result in {currency} : {result}"

    elif currency == 2 or currency == "EUR":
        result = gbp_amount * 1.14
        result = round(result, 2)
        print("result in EUR: ", result)
        response = f"Result in {currency} : {result}"

    elif currency == 3 or currency == "BRL":
        result = gbp_amount * 4.77
        result = round(result, 2)
        print("result in BRL: ", result)
        response = f"Result in {currency} : {result}"

    elif currency == 4 or currency == "JPY":
        result = gbp_amount * 151.05
        result = round(result, 2)
        print("result in JPY: ", result)
        response = f"Result in {currency} : {result}"

    elif currency == 5 or currency == "TRL":
        result = gbp_amount * 5.68
        result = round(result, 2)
        print("result in TRL: ", result)
        response = f"Result in {currency} : {result}"

    else:
        response = "Error – Unknown currency"

    return response


def staff_verification(is_staff, fee, gbp_amount):
    if is_staff == "yes":
        tmp_result = gbp_amount * 0.05
        total = gbp_amount + fee - tmp_result
    else:
        total = gbp_amount + fee

    return total
