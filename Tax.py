from flask import Flask, render_template, request
app = Flask(__name__)

def calculate_tax(income):
    exemption = 75000.0
    taxable_income = max(income - exemption, 0)

    if taxable_income <= 1200000:
        return 0

    tax = 0

    if taxable_income > 400000:
        slab = min(taxable_income, 800000) - 400000
        tax += slab * 0.05
    if taxable_income > 800000:
        slab = min(taxable_income, 1200000) - 800000
        tax += slab * 0.10
    if taxable_income > 1200000:
        slab = min(taxable_income, 1600000) - 1200000
        tax += slab * 0.15
    if taxable_income > 1600000:
        slab = min(taxable_income, 2000000) - 1600000
        tax += slab * 0.20
    if taxable_income > 2000000:
        slab = min(taxable_income, 2400000) - 2000000
        tax += slab * 0.25
    if taxable_income > 2400000:
        slab = taxable_income - 2400000
        tax += slab * 0.30

    return tax


def main():
    income = float(input("Enter the income: "))
    
    tax = calculate_tax(income)
    taxable_income = max(income - 75000, 0)  # Ensure non-negative taxable income
    effective_tax_rate = round((tax / income) * 100, 2) if income > 0 else 0  # Avoid division by zero

    print("\nIncome: Rs {:.2f}".format(income))
    print("Standard Exemption: Rs 75,000")
    # print(f"DEBUG: Taxable Income Before Print: {taxable_income}")  # Debugging Line
    print("Taxable Income: Rs {:.2f}".format(taxable_income))  
    print("Tax Payable: Rs {:.2f}".format(tax))
    print("Effective Tax Rate: {:.2f}%".format(effective_tax_rate))


if __name__ == "__main__":
    main()
