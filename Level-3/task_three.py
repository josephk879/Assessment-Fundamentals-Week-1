"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    """Generates a VAT invoice."""
    receipt_line_list = receipt_string.splitlines()
    vat_receipt = "VAT RECEIPT" + "\n" + "\n"

    for line in receipt_line_list[:-1]:
        item_before_vat = format((float(line[-4:]) * 0.8), ".2f")

        vat_receipt += line.replace(line[-5:], "£" +
                                    str(item_before_vat)) + "\n"

    total_before_vat = format((float(receipt_line_list[-1][-4:]) * 0.8), ".2f")

    vat = format(
        float(receipt_line_list[-1][-4:]) - float(total_before_vat), ".2f")

    vat_receipt += "\n" + "Total: £" + \
        str(total_before_vat) + "\n" + "VAT: " + "£" + str(vat) + \
        "\n" + "Total inc VAT: " + receipt_line_list[-1][-5:]

    return vat_receipt  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
