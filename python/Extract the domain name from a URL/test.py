import codewars_test as test
from solution import domain_name


@test.describe('url Validator - fixed tests')
def sample_tests():
    test.assert_equals(domain_name("http://google.com"), "google")
    test.assert_equals(domain_name("http://google.co.jp"), "google")
    test.assert_equals(domain_name("www.xakep.ru"), "xakep")
    test.assert_equals(domain_name("https://youtube.com"), "youtube")
