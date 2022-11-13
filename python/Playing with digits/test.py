import codewars_test as test
from solution import dig_pow


@test.describe("Fixed tests")
def fixed_test():
    @test.it("Samples")
    def sample_tests():
        test.assert_equals(dig_pow(89, 1), 1)
        test.assert_equals(dig_pow(92, 1), -1)
        test.assert_equals(dig_pow(46288, 3), 51)
