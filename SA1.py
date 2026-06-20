class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = ["Empty"] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

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


# MAIN PROGRAM
parking = CircularQueue(5)

parking.park_car("TN01A1234")
parking.park_car("TN10B5678")
parking.park_car("TN20C9876")

print(parking.queue)


