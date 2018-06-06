from fizz_buzz import FizzBuzz

def test_run():
    f = FizzBuzz()
    assert f.run(1) == 1

def test_run3():
    f = FizzBuzz()
    assert f.run(3) == "Fizz"

def test_run5():
    f = FizzBuzz()
    assert f.run(5) == "Buzz"

def test_run15():
    f = FizzBuzz()
    assert f.run(15) == "FizzBuzz"

def test_run0():
    f = FizzBuzz()
    assert f.run(0) == 0
