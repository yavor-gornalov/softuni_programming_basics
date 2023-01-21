# https://judge.softuni.org/Contests/Practice/Index/1063#0

def print_receipt_header():
    print("CASH RECEIPT\n"
          "------------------------------")


def print_receipt_body():
    print("Charged to____________________\n"
          "Received by___________________")


def print_receipt_footer():
    print("------------------------------\n"
          "(c) SoftUni")


def print_receipt():
    print_receipt_header()
    print_receipt_body()
    print_receipt_footer()


print_receipt()
