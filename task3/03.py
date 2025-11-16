'''


Create a Clock class and initialize it with hours and minutes.

    Create a method add_time(), which should accept an argument – another Clock instance object – and adds it:

clock1 = Clock(23, 30)
clock2 = Clock(14, 20)
clock1.add(clock2)
print(clock1.hours, clock1.minutes)
>>> 13, 50

    Create a method display_time() which should print the time.
    Create a method display_total_minutes(). E.g.- (1 hr 2 min) should display 62 minutes.


'''
class Clock:
    def __init__(self, hours: int, minutes: int) -> None:
        if hours < 0 or minutes < 0:
            raise ValueError("cannot input negative number")

        total = hours * 60 + minutes
        total = total % (24 * 60)

        self.hours = total // 60          
        self.minutes = total % 60

    def add(self, other: "Clock") -> None:
        self.hours += other.hours
        self.minutes += other.minutes

        if self.minutes >= 60:
            extra_hours = self.minutes // 60
            self.minutes = self.minutes % 60
            self.hours += extra_hours

        self.hours = self.hours % 24


    def add_time(self, other: "Clock") -> None:
        self.add(other)

    def display_time(self) -> None:
        print(f"{self.hours:02d}:{self.minutes:02d}")

    def display_total_minutes(self) -> None:
        print(self.hours * 60 + self.minutes)
