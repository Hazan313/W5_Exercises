# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?
import math
Xaop = 38
Cv = 15
AoV = Xaop / Cv
Vc = 250 * math.ceil(AoV)
Cpp = Vc / Xaop
print(AoV)
print(f'{math.ceil(AoV)} vans needed')
print(f"The vans will cost {Vc: .2f}$")
print(f"{Cpp:.2f}$ is the cost per person")