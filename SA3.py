# ---------------- CIRCULAR QUEUE ---------------- #
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = ["Empty"] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def park_car(self, car_number):

        if self.is_full():
            print("Parking Full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = car_number
        print(f"{car_number} parked successfully")

    def remove_car(self):

        if self.is_empty():
            print("Parking Empty")
            return

        removed = self.queue[self.front]
        self.queue[self.front] = "Empty"

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"{removed} exited parking")

    # SENSOR DISPLAY
    def display_slots(self):

        print("\n------ PARKING STATUS ------")

        for i in range(self.size):

            if self.queue[i] == "Empty":
                sensor = "GREEN LED ON | Slot Empty"
            else:
                sensor = "RED LED ON | Car Detected"

            print(f"Slot {i+1} : {self.queue[i]} --> {sensor}")


# ---------------- MAIN PROGRAM ---------------- #
parking = CircularQueue(5)

parking.park_car("TN01A1234")
parking.park_car("TN10B5678")

parking.display_slots()

parking.remove_car()

parking.display_slots()