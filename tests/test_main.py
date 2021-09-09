import app.fizzbuzz


class TestMain:

    def test_function(self):
        assert True

    def test_fizzbuzz_1(self):
        assert app.fizzbuzz.fizzbuzz(1) == [1]

    def test_fizzbuzz_2(self):
        assert app.fizzbuzz.fizzbuzz(2) == [1, 2]

    def test_fizzbuzz_3(self):
        assert app.fizzbuzz.fizzbuzz(3) == [1, 2, "Fizz"]

    def test_fizzbuzz_5(self):
        assert app.fizzbuzz.fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]

    def test_fizzbuzz_15(self):
        assert app.fizzbuzz.fizzbuzz(
            15) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

    def test_fizzbuzz_45(self):
        assert app.fizzbuzz.fizzbuzz(
            45
        ) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz']
