print("What's the amount borrowed: " , end = "")
p = int(input())
print("What's the annual interest rate: " , end = "")
r = float(input()) / 100 / 12
print("What's the payback period (in years): " , end = "")
n= int(input()) * 12
mortgageMontlyPayment = (p * (1 + r) ** n * r) / ((1 + r) ** n - 1)
print(f"Monthly payment (calculated output): ${mortgageMontlyPayment:.2f}") #.2f 1470.11 after . 11
totalPayment = mortgageMontlyPayment * n
#print(f"Total payment $: {totalPayment:.2f}")







