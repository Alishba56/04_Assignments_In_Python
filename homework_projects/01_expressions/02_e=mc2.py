def main():
    C = 299792458  
    
    while True:
        mass = float(input("Enter kilos of mass: "))

        energy = mass * C**2
        
        print("\nE = m * C^2...\n")
        print("m = {:.1f} kg".format(mass))
        print("C = {} m/s".format(C))
        print("{:.1e} joules of energy!".format(energy))

if __name__ == "__main__":
    main()
