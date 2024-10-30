#Exercise 4.A Lab2
# List all variables
pay_rate = 25.50
hours_worked = 40
overtime_hours = 0
weekly_pay = 0

# Process all formulae
if hours_worked > 40 :
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

    

# Print all results


