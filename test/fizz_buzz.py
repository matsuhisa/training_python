class FizzBuzz:

    def run(self, number):
        if number > 0:
            if (number % 5) == 0 and (number % 3) == 0:
                return "FizzBuzz"
            elif (number % 5) == 0:
                return "Buzz"
            elif (number % 3) == 0:
                return "Fizz"
        return number

# f = FizzBuzz()
# print(f.run(1))
# print(f.run(3))
# print(f.run(5))
# print(f.run(15))
