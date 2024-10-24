# Years To Double: 72 / Expected Rate of Return

# To calculate the time period an investment will double, divide the integer 72 by the expected rate of return. 
# The formula relies on a single average rate over the life of the investment. 
# The findings hold true for fractional results, as all decimals represent an additional portion of a year.
# R * t = 72 , R = 72 / t , t = 72 / R
import math

IR = 005.45698 # % per annum
X = 15735.342 #Amount in savings
X2 = X*2 #doubled amount of savings
Years = 72/int(IR)

print("At a " + format(IR,".3") + " interest rate, your savings account will be worth " + format(str(X2), ".8") + "$ in " + format(str(Years), '.4') + ' Years')


#++ ASK BESS about format issue 
