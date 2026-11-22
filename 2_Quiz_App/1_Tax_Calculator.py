# =====================================================================
#  PROJECT 1 (BASIC LEVEL): INCOME TAX CALCULATOR
#  Built with : Python + Streamlit
#  Tax rules  : India - New Tax Regime, FY 2026-27 (for salaried people)
#  How to run : streamlit run tax_calculator.py
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: IMPORT LIBRARIES
# ---------------------------------------------------------------------
# Streamlit turns a Python script into a web page.
# We give it a short name "st" so we can write st.title() instead of
# streamlit.title() every time.
import streamlit as st


# ---------------------------------------------------------------------
#  SECTION 2: CONSTANTS (fixed values that never change)
# ---------------------------------------------------------------------
# Writing constant names in CAPITAL letters is a Python habit.
# It tells anyone reading the code: "don't change this value inside
# the program". If the rules change next year, we update them here.

STANDARD_DEDUCTION = 75000      # Salaried people can subtract ₹75,000
REBATE_LIMIT = 1200000          # Taxable income up to ₹12 lakh -> tax is 0 (Sec 87A)
CESS_RATE = 0.04                # 4% Health & Education cess on the tax

# Tax slabs as a LIST of pairs (called "tuples").
# Each pair is: (upper limit of the slab, tax rate for that slab)
TAX_SLABS = [
    (400000, 0.00),             # 0       to 4 lakh  ->  0%
    (800000, 0.05),             # 4 lakh  to 8 lakh  ->  5%
    (1200000, 0.10),            # 8 lakh  to 12 lakh -> 10%
    (1600000, 0.15),            # 12 lakh to 16 lakh -> 15%
    (2000000, 0.20),            # 16 lakh to 20 lakh -> 20%
    (2400000, 0.25),            # 20 lakh to 24 lakh -> 25%
    (float("inf"), 0.30),       # above 24 lakh      -> 30%  (inf = no upper limit)
]


# ---------------------------------------------------------------------
#  SECTION 3: FUNCTION TO CALCULATE SLAB TAX
# ---------------------------------------------------------------------
# A function is a reusable block of code.
# Input  : taxable_income (a number)
# Output : the tax amount before rebate and cess
def calculate_slab_tax(taxable_income):
    tax = 0                     # start with zero tax
    previous_limit = 0          # where the current slab starts

    # Go through each slab one by one
    for limit, rate in TAX_SLABS:

        # Only tax this slab if the income reaches into it
        if taxable_income > previous_limit:

            # How much of the income falls inside THIS slab?
            # Example: income 10 lakh, slab 8-12 lakh
            #          min(10 lakh, 12 lakh) - 8 lakh = 2 lakh
            amount_in_slab = min(taxable_income, limit) - previous_limit

            # Add the tax for this slab to the running total
            tax += amount_in_slab * rate

        # The next slab starts where this one ended
        previous_limit = limit

    return tax                  # send the answer back


# ---------------------------------------------------------------------
#  SECTION 4: FUNCTION THAT DOES THE FULL CALCULATION
# ---------------------------------------------------------------------
# This function uses calculate_slab_tax() and then applies the
# standard deduction, the 87A rebate and the cess.
# It returns a DICTIONARY (key: value pairs) with every result,
# so the screen can show each one separately.
def calculate_total_tax(income):

    # Step A: subtract the standard deduction
    # max(..., 0) makes sure taxable income never goes below zero
    taxable_income = max(income - STANDARD_DEDUCTION, 0)

    # Step B: calculate tax using the slabs
    slab_tax = calculate_slab_tax(taxable_income)

    # Step C: apply the Section 87A rebate
    # If taxable income is ₹12 lakh or less, the full tax is cancelled
    if taxable_income <= REBATE_LIMIT:
        rebate = slab_tax
    else:
        rebate = 0

    tax_after_rebate = slab_tax - rebate

    # Step D: add 4% cess on the tax
    cess = tax_after_rebate * CESS_RATE

    # Step E: final tax to pay
    total_tax = tax_after_rebate + cess

    # Return all values together in one dictionary
    return {
        "taxable_income": taxable_income,
        "slab_tax": slab_tax,
        "rebate": rebate,
        "cess": cess,
        "total_tax": total_tax,
    }


# ---------------------------------------------------------------------
#  SECTION 5: PAGE SETUP AND HEADING (the screen starts here)
# ---------------------------------------------------------------------
# set_page_config must be the first Streamlit command on the page.
# It sets the browser tab title and icon.
st.set_page_config(page_title="Tax Calculator", page_icon="💰")

st.title("💰 Income Tax Calculator")             # big main heading
st.caption("New Tax Regime • FY 2026-27 • Salaried")  # small grey line


# ---------------------------------------------------------------------
#  SECTION 6: USER INPUT
# ---------------------------------------------------------------------
st.header("1. Enter Your Income")               # section heading

# number_input shows a box for numbers.
# min_value=0 -> no negative numbers allowed
# step=10000  -> the + / - buttons change the value by ₹10,000
income = st.number_input("Annual Income (₹)", min_value=0, step=10000)


# ---------------------------------------------------------------------
#  SECTION 7: CALCULATE AND SHOW RESULTS
# ---------------------------------------------------------------------
# The code inside this "if" runs only when the button is clicked.
if st.button("Calculate Tax"):

    # Call our function and store the dictionary it returns
    result = calculate_total_tax(income)

    st.header("2. Tax Breakdown")               # section heading

    # Show each value.  :,.0f means -> add commas, no decimal places
    st.write(f"Gross income: ₹{income:,.0f}")
    st.write(f"(-) Standard deduction: ₹{STANDARD_DEDUCTION:,.0f}")
    st.write(f"Taxable income: ₹{result['taxable_income']:,.0f}")
    st.write(f"Tax as per slabs: ₹{result['slab_tax']:,.0f}")
    st.write(f"(-) 87A rebate: ₹{result['rebate']:,.0f}")
    st.write(f"(+) Cess (4%): ₹{result['cess']:,.0f}")

    st.header("3. Final Result")                # section heading

    # Show a green box if no tax, otherwise a blue info box
    if result["total_tax"] == 0:
        st.success("🎉 No tax to pay!")
    else:
        st.info(f"Total tax to pay: ₹{result['total_tax']:,.0f}")

        # Extra: tax per month, useful for salaried people
        monthly_tax = result["total_tax"] / 12
        st.write(f"That is about ₹{monthly_tax:,.0f} per month.")