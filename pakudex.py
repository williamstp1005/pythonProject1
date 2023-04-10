from pakuri import Pakuri


class Pakudex:
    species_type = ""  # here i made a class object so that it may stay constant for calling Pakuri. maybe unnecessary

    def __init__(self, capacity=20):  # initializing objects, with default max capacity being 20 with =20 on the arg
        self.capacity = capacity
        self.list = []
        self.spec_list = []

    def get_size(self):  # a little redundant, but i ensure that the size is an integer
        self.size = int(len(self.list))
        return self.size

    def get_capacity(self):  # even more redundant, but here it is
        capacity = self.capacity
        return capacity

    def get_species_array(self):
        if not self.list:  # if there's nothing there, it returns none and then passes the rest of the function
            return None
            pass

        # cool for loop that puts all items in the list into a numbered list
        print("Pakuri In Pakudex:")
        for i in range(0, self.get_size()):
            print(f"{(i + 1)}. {self.list[i]}")

        return self.list

    def get_stats(self, species):
        exists = False  # guilty until proven innocent

        # checks for a match. when it finds it, the pakuri species is named, and the loop is then broken
        for i in range(0, len(self.list)):
            if self.list[i] == species:
                exists = True
                self.species_type = self.spec_list[i]
                break
            else:
                exists = False

    # if it goes through that oop without finding a match, it must not have been added yet. pass the rest of the func
        if exists is False:
            print("Error: No such Pakuri!\n")
            return None
            pass
        else:
            print(f"\nSpecies: {self.species_type.get_species()}")
            print(f"Attack: {self.species_type.get_attack()}")
            print(f"Defense: {self.species_type.get_defense()}")
            print(f"Speed: {self.species_type.get_speed()}\n")
    # ^^ if it's true, then it shall list all of the stats of the pakuri

    def sort_pakuri(self):  # could have just used the sort function built-in but it's cool
        self.list.sort()

    def add_pakuri(self, species):
        success = True  # success is assumed to be true; innocent until proven guilty

        for x in self.list:  # if a match is found, then clearly the pakuri has been added before
            if x == species:
                print("Error: Pakudex already contains this species!\n")
                success = False  # then it becomes false and passes through the rest of the if statements

        '''if success is True:  # if still true, it's ready to be added
            if self.get_size() == int(self.capacity):
                success = False
                print("Error: Pakudex is full!")'''

        if success is True:  # if it got this far, then the addition process can be done
            self.species_type = Pakuri(species)
            self.list.append(self.species_type.species)
            self.spec_list.append(self.species_type)
            print(f"Pakuri species {self.species_type.species} successfully added!\n")

        success = True
        # as previously explained, if the pakudex already contains the species, then the next if statements can be
        # skipped. however, this declaration of success being true makes sure that the success checker in the
        # pakuri_program.py function can still allow pakuri to be added.

        if success is True:
            if self.get_size() == int(self.capacity):
                success = False

        # this last if statement turns the success variable into a sort of fullness checker. this value will get
        # returned, and the main function in pakuri_program.py will automatically know that the pakudex is full
        # without having to put in a species name

        return success

    def evolve_species(self, species):
        # pretty much identical to get_stats, except instead of displaying stats it evolves the pakuri

        exists = False  # guilty until proven innocent

        for i in range(0, len(self.list)):  # same logic as get_stats() (i used the same exact code too)
            if self.list[i] == species:
                exists = True
                self.species_type = self.spec_list[i]
                break
            else:
                exists = False

        if exists is False:
            print("Error: No such Pakuri!\n")
            return False
            pass
        else:
            self.species_type.evolve()
            print(f"{self.species_type.species} has evolved!\n")
            return True
