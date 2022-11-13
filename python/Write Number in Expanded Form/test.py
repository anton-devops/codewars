import codewars_test as test
from solution import expanded_form


@test.describe('Walk Validator - fixed tests')
def sample_tests():
    test.assert_equals(expanded_form(12), '10 + 2')
    test.assert_equals(expanded_form(42), '40 + 2')
    test.assert_equals(expanded_form(70304), '70000 + 300 + 4')
