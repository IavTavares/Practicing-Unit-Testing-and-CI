import sys
  
# adding data folder to the system path
pathname=r"src/data"
# do not break the string above with \ it will not work...

if not pathname in sys.path:
    sys.path.insert(0,pathname)
# append or insert will always add a path

import pytest
from Function import string_to_int,string_to_int_2


class TestStringToInt:
    def test_on_string_to_int(self):
        assert string_to_int("20.1")==20
    
    def test_on_first_print(self,capsys):
        assert string_to_int("asdol") is None
        captured = capsys.readouterr()
        assert captured.out ==("Variable is not convertible to a number\n")
    
    def test_on_second_print(self,capsys):
        assert string_to_int({"asdol"}) is None
        captured = capsys.readouterr()
        assert captured.out == "Wrong Type\n"
    
class TestStringToInt2:
    def test_on_string_to_int(self):
        assert string_to_int_2("20.1")==20
    
    def test_on_first_error_raised(self):
        with pytest.raises(ValueError) as value_info:
            string_to_int_2("asdol")
        assert value_info.match("Variable is not convertible to a number")
    
    def test_on_second_error_raised(self):
        with pytest.raises(TypeError) as type_info:
            string_to_int_2({"asdol"})
        assert type_info.match("Wrong Type")
        
    @pytest.mark.xfail(reason="Test-driven Dev") # we expect the next test to fail
    def test_expected_to_fail(self):
        assert string_to_int_2({"asdol"}) is None
    
    @pytest.mark.skipif(sys.version_info>=(3,9,6),
                        reason="requires Pytho 3.9.5 or lower") 
    # we expect the next test to not be run
    # on  Python 3.9.6 and higher
    def test_expected_to_skip(self):
        assert string_to_int_2({"asdol"}) is None
        
# !cd C:\path
# we always need ! to run shell commands in IPython console
