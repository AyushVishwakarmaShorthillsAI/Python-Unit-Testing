import unittest

# can't directly write a test function 
# need to make a test class before writing a test function

# all the unit tets classes must be derived from "unittest.TestCase" class
class learnTest(unittest.TestCase):

    # NOTE : Naming Convention : all the test cases should start with "test..." (no underscore needed, but may use)   
    def test_fun_1(self):
        pass
    
    def test_f2(self):
        pass

    # below function is not considered as a test case :     
    def my_fun(self):
        pass

class anotherTest(unittest.TestCase):
    # starts with 'test' => a test case
    def test3(self):
        pass

    # same function name in different class : is counted as new test case ?
    def test_f2(self):
        pass


def sum(a,b):
    return a+b

# no convention for class naming here !!
class SumTest(unittest.TestCase):
    
    def setUp(self):
        print("Setup Called ...")
        self.a=10
        self.b=20
    
    def tearDown(self):
        print("Tear down called")

    def test_sum_fun_1(self):
        print("Test Funciton 1 called ...")
        # #arrange
        # a=10
        # b=20

        #act
        result=sum(self.a, self.b)

        # Assert
        self.assertEqual(result, self.a+ self.b)
    
    def test_sum_fun_2(self):
        print("Test Function 2 called ...")
        # a=10
        # b=20

        #act
        result=sum(self.b, self.a)

        # Assert
        self.assertEqual(result, self.a+ self.b)

    # we can arrange the varaible in a function called setUp
    # this setup function is being called before each and every test function -> see the print
    # similar to setup function there is "TearDown function" which is called after every test function is executed

# to invoke the unittest framework,
# below line will invoke all the test in the file or the imports
if __name__=='__main__':
    unittest.main()

