from pakudex import Pakudex


def main():
    valid_input = False
    option = 0      # need to put these here for later use; i put a lot of the methods within pakudex.py, not here
    success_add = True

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while valid_input is False:

        """here, i implemented try and except to catch a value error, forgetting that negative numbers are also invalid,
    but will not raise a value error. i forgot that i could raise my own exception until too late, plus it would
    not be consistent with the rest of my code, so I instead just put another if, else statement after the try except"""

        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
        except ValueError:
            print("Please enter a valid size.")
            continue

        if max_capacity <= 0:
            print("Please enter a valid size.")
        else:
            pakudex = Pakudex(max_capacity)
            print(f"The Pakudex can hold {max_capacity} species of Pakuri.\n")
            valid_input = True

    while option != 6:
        print(
            "Pakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n"
            "5. Sort Pakuri\n6. Exit\n"
        )
        # i just preferred the way this print statement looked when doing the parenthesis differently and using \n
        try:
            option = int(input("What would you like to do? "))

        except ValueError:  # since it must be an integer, try/except. again, forgot about negative numbers. else covers
            print("Unrecognized menu selection!\n")
            continue

        if option == 1:
            # calling the function inside the if statement still runs the method while checking if there are no pakuri
            if pakudex.get_species_array() is None:
                print("No Pakuri in Pakudex yet!\n")
                continue
            print()

        elif option == 2:  # like i said, lots of the processes were done inside of pakudex.py for me
            existing_species = input("Enter the name of the species to display: ")
            pakudex.get_stats(existing_species)

        elif option == 3:
            if success_add is False:  # at the end of add_pakuri(), the function checks for if the max capacity is full,
                # returning False for success, denoting that the list is full without having to name a pakuri to add
                print("Error: Pakudex is full!\n")
                continue

            new_species = input("Enter the name of the species to add: ")
            success_add = pakudex.add_pakuri(new_species)

        elif option == 4:  # again, just runs the function and prints the statement
            species_evolve = input("Enter the name of the species to evolve: ")
            pakudex.evolve_species(species_evolve)

        elif option == 5:  # same soup reheated
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!\n")

        elif option == 6:  # have to explicitly name option 6 because:
            print("Thanks for using Pakudex! Bye!")

        else:  # i had to cover myself for negative numbers as an option :(
            print("Unrecognized menu selection!\n")


if __name__ == "__main__":
    main()
