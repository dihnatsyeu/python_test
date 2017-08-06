import pytest

class TestMyFunc(object):
    def test_my_site(self):
        with pytest.allure.step("MyStep"):
            print("mybad")
        with pytest.allure.step("AnotherStep"):
            print "Ups i did it again"