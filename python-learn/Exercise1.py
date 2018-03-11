""" Sample Learning Exercise """


class ExerciseOne:

    def __init__(self, lesson):
        self.lesson = lesson

    def display_lesson(self):
        print(self.lesson)

    def check_digit(self, entry):
        if entry.isdigit():
            print("You entered", entry)
        else:
            print("Sorry only number is accepted")

    def is_number(self, entry):
        return entry.isdigit()


if __name__ == '__main__':
    demo = ExerciseOne(lesson="Exercise 1")
    demo.display_lesson()

    number = input("Enter a number:")
    demo.check_digit(number)
    print('The entered value is a number ? : ', demo.is_number(number))
