class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = [Elevator(bottom, top) for i in range(num_elevators)]

    def run_elevator(self, number, floor):
        self.elevators[number].go_to_floor(floor)

    def fire_alarm(self):
        print("\nFIRE ALARM\n")
        for i in self.elevators:
            i.go_to_floor(self.bottom)

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print("Elevator at floor:", self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print("Elevator at floor:", self.current_floor)

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

b = Building(0, 10, 2)
b.run_elevator(0, 6)
b.run_elevator(1, 9)

b.fire_alarm()
