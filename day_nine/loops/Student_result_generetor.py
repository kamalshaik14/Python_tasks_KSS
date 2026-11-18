#7. Student Result Generator (Method Overloading Concept)
#A school system calculates student results differently depending on available data.
#Create a Result class where a method can calculate the result using either two subjects or three subjects


class Result:
    def calculate(self, mark1, mark2, mark3=None):
        if mark3 is None:
            average = (mark1 + mark2) / 2
        else:
            average = (mark1 + mark2 + mark3) / 3

        print("Average:", average)


result = Result()
result.calculate(80, 90)       # Two subjects
result.calculate(80, 90, 70)  # Three subjects
