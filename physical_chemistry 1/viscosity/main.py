#data from user#

density = float(input('Give density of the compound '))
time_water = float(input('Give outflow time of H2O (in seconds) '))
time = float(input('Give outflow time of the other compound (in seconds) '))
molecular_weigh = float(input('Give molecular weight of the compound '))
m2 = float(input("Give the weight of conical flask when its filled with the compound and water "))
m1 = float(input("Give the weight of the conical flask when its filled only with water "))
m = float(input("Give the weigh of the conical flask when its empty "))
v1 = float(input("Give the volume of H2O "))
v2 = float(input("Give the volume of compound "))




#constants#

v_water = 0.89
density_water = 0.99707
molecular_weigh_water = 18.015
float(v_water)
float(density_water)
float(molecular_weigh_water)




#formulas#

v = v_water * (density /density_water)*(time/time_water)
print(v)

P = (molecular_weigh / density) * v**(1/8)
print(P)

relative_density = (m2-m)/(m1-m)

density_mix = density_water * relative_density
print(relative_density)
print(density_mix)


mole_fraction_water = ((v1*density_water)/molecular_weigh_water)/(((v1*density_water)/molecular_weigh_water)+((v2*density)/molecular_weigh))
print(mole_fraction_water)

mole_fraction_compound = ((v2*density)/molecular_weigh)/(((v1*density_water)/molecular_weigh_water)+((v2*density)/molecular_weigh))
print(mole_fraction_compound)

avg_molecular_weigh_mix = (mole_fraction_water*molecular_weigh_water) + (mole_fraction_compound*molecular_weigh)
print(avg_molecular_weigh_mix)
