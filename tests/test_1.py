from my_App.unit_testing_pytest import add

# testing add function in my_App folder
def test_add_num():
    assert add(1,2)  == 3
    assert add(1,2) == 4

def test_add_str():
    assert add("one", "two") == "onetwo"


class TestSample:
    def test_sub_num(self):
        assert add(9, -2) == 7

# pytest is better bcoz of better ouptut(shows the error what's wrong)
# lesser boilerCode to write