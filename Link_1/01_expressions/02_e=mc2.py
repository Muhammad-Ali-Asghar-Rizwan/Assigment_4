C = 299792458 # speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter mass in kg: ")) 
    
    
    energy_in_joules: float = mass_in_kg * (C ** 2)
    
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
