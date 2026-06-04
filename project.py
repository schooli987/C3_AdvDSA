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

    def add_ride(self, ride_id):

        if self.is_full():
            print("Ride Queue Full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = ride_id
        print(f"{ride_id} added successfully")

    def complete_ride(self):

        if self.is_empty():
            print("Ride Queue Empty")
            return

        completed = self.queue[self.front]
        self.queue[self.front] = "Empty"

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"{completed} completed")

    def display_rides(self):

        print("\n----- CURRENT RIDE QUEUE -----")

        for i in range(self.size):
            print(f"Slot {i+1}: {self.queue[i]}")


# MAIN PROGRAM

rides = CircularQueue(5)

rides.add_ride("Ride101")
rides.add_ride("Ride102")
rides.add_ride("Ride103")

rides.display_rides()

rides.complete_ride()

rides.display_rides()