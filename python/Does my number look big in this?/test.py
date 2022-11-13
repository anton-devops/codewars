import codewars_test as test
from solution import narcissistic


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(narcissistic(7), True, '7 is narcissistic');
        test.assert_equals(narcissistic(371), True, '371 is narcissistic');
        test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
        test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
