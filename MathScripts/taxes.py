# 

import math

Yx = 75733.345
X = Yx/12
Fxamount = 0.23 * X
Fxamount = round(Fxamount,2)
print("The amount of money witheld for taxes is $" + str(Fxamount))

# Ask Bess about round formula within string error:  round(str(Fxamount),'.2'))
#                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: type str doesn't define __round__ method