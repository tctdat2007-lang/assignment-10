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


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, floor):
        self.elevators[number].go_to_floor(floor)

b = Building(0, 10, 2)
b.run_elevator(0, 7)
b.run_elevator(1, 4)
