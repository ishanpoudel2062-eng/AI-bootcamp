class Carrental:
    def __init__(self):
        self.car = []

    def add(self, car):
        if car in self.car:
            print("car already exists.")
        else:
            self.car.append(car)
            print("car added successfully.")

    def remove(self, car):
        if car in self.car:
            self.car.remove(car)
            print("car removed successfully.")
        else:
            print("car not found.")

    def search(self, car):
        if car in self.car:
            print(f"{car} is available.")
        else:
            print("car of entered brand is not available.")

    def display(self):
        if not self.car:
            print("no cars available.")
        else:
            print("available Cars:")
            for i in self.car:
                print(i)


c = Carrental()

while True:
    print("\n Car Rental System ")
    print("1. Add Car \n 2. Remove Car\n 3. Search Car \n 4. Display Cars \n 5. Exit ")
    ch = int(input("enter your choice: "))

    if ch == 1:
        car = input("enter car name: ")
        c.add(car)

    elif ch == 2:
        car = input("enter car name: ")
        c.remove(car)

    elif ch == 3:
        car = input("enter car name: ")
        c.search(car)

    elif ch == 4:
        c.display()

    elif ch == 5:
        print("Thank you for using Car Rental System.")
        break

    else:
        print("Invalid choice.")