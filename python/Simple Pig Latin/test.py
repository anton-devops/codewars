import codewars_test as test
from solution import pig_it


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        test.assert_equals(pig_it('This is my string'), 'hisTay siay ymay tringsay')
        test.assert_equals(pig_it('O tempora o mores !'), 'Oay emporatay oay oresmay !')
