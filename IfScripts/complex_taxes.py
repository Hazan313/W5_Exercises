# List all variables
pay_rate = 25
#pay_rate = (input(f'What is your hourly pay rate? Pay rate: $'))
hours_worked = 1
#hours_worked = int(input(f'Generally, how many hours do you work in a week? Hours worked:'))
overtime_hours = 0
weekly_pay = 0
filing_status = str(input(f'Is your filing status single or joint? Filing status:'))
tax_rate = 0
tax_witheld = 0
rem_weekly_pay = 0

# Process all formulae
if hours_worked > 119:
    print(f'Invalid number of hours. Please try again')
elif hours_worked > 40 :
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (1.5 * pay_rate)
    weekly_pay = ((hours_worked - overtime_hours) * (pay_rate)) + (overtime_pay)
    print(f"Your weekly pay comes out to a total ${round(weekly_pay, 2)}, \nwith ${round(overtime_pay, 2)} for {overtime_hours} hours worth of overtime pay.") 
elif hours_worked < 40:
    weekly_pay = hours_worked * pay_rate
    print(f"Your weekly pay comes out to a total of ${weekly_pay},\nReason being hours worked is {hours_worked}.")
elif hours_worked == 40 :
    weekly_pay = pay_rate * hours_worked
    print(f"Your weekly pay comes out to {weekly_pay},\nand hours worked are exactly {hours_worked}.")

yearly_pay = 52 * weekly_pay

if filing_status == 'single':
    if int(yearly_pay) < 12000:
        tax_rate = 0.05
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1 - tax_rate) * weekly_pay
        print(f"You worked {format((hours_worked * 52.143), '.2f')} hours this year/period.\nBecause you earn ${pay_rate} per hour, your gross weekly pay is ${weekly_pay} .\nYour filing status is {filing_status},\nYour tax witholding for the week is ${tax_witheld,}\nYour net pay is ${format(yearly_pay, '.2f')}")







print(f'Your yearly pay comes down to ${format(yearly_pay, '.2f')}')

# Print all results