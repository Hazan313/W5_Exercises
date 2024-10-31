# List all variables
pay_rate = 75
#pay_rate = (input(f'What is your hourly pay rate? Pay rate: $'))
hours_worked = 37.5
#hours_worked = int(input(f'Generally, how many hours do you work in a week? Hours worked:'))
overtime_hours = 0
weekly_pay = 0
filing_status = (input(f'Is your filing status single or joint? Filing status:'))
tax_rate = 0
tax_witheld = 0
rem_weekly_pay = 0

# Process all formulae

# Old code from pay_rules
#if hours_worked > 119:
#    print(f'Invalid number of hours. Please try again')
#elif hours_worked > 40 :
#    overtime_hours = hours_worked - 40
#    overtime_pay = overtime_hours * (1.5 * pay_rate)
#    weekly_pay = ((hours_worked - overtime_hours) * (pay_rate)) + (overtime_pay)
#    print(f"Your weekly pay comes out to a total ${round(weekly_pay, 2)}, \nwith ${round(overtime_pay, 2)} for {overtime_hours} hours worth of overtime pay.") 
#elif hours_worked < 40:
#    weekly_pay = hours_worked * pay_rate
#    print(f"Your weekly pay comes out to a total of ${weekly_pay},\nReason being hours worked is {hours_worked}.")
#elif hours_worked == 40 :
#    weekly_pay = pay_rate * hours_worked
#    print(f"Your weekly pay comes out to {weekly_pay},\nand hours worked are exactly {hours_worked}.")

weekly_pay = hours_worked * pay_rate

yearly_pay = 52 * weekly_pay


if filing_status == 'single':
    if int(yearly_pay) < 12000:
        tax_rate = 0.05
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1 - tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status},
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
    elif 12000 <= int(yearly_pay) < 24999.99 :
        tax_rate = 0.1
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1-tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status},
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
    elif 25000 <= int(yearly_pay) < 74999.99 :
        tax_rate = 0.15 
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1-tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status}
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
    elif int(yearly_pay) >= 75000:
        tax_rate = 0.20
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1- tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status}, 
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
        
elif filing_status == 'joint' :
    if int(yearly_pay) < 12000:
        tax_rate = 0.00
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1- tax_rate) * weekly_pay
        print(f'''You worked {format(float(hours_worked * 52.143),'.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status}, 
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
    elif 12000 <= (yearly_pay) < 24999.99 :
        tax_rate = 0.06
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1 - tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status},
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
    elif 25000 <= int(yearly_pay) < 74999.99 :
        tax_rate = 0.11 
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1-tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status}
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')
    elif int(yearly_pay) >= 75000:
        tax_rate = 0.20
        tax_witheld = tax_rate * weekly_pay
        rem_weekly_pay = (1- tax_rate) * weekly_pay
        print(f'''You worked {format((hours_worked * 52.143), '.5')} hours this year/period.
Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(weekly_pay, '.2f')}
Your filing status is {filing_status}, 
Your tax witholding for the week is ${format(str(tax_witheld),'.5')}
Your net pay for the week is ${format(rem_weekly_pay, '.2f')}
Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}''')

elif filing_status != 'single' or filing_status != 'joint' :
        print(f"Incorrect input! Please try again. Disregard the following incorrect results")


# Print all results

#print(f'Your yearly pay is ${format(yearly_pay, '.2f')}\nAnd your yearly net pay comes down to ${format(int(rem_weekly_pay * 52), '.2f')}')