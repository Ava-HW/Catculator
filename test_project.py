from project import calculate_age
from project import calculate_size
from project import calculate_bmi

def test_age():
    assert calculate_age(6)==39
    assert calculate_age(17)==84
    assert calculate_age(3)==20

def test_size():
    assert calculate_size(16, 3)==6
    assert calculate_size(32, 5)==5
    assert calculate_size(10, 2)==6.4

def test_bmi():
    assert calculate_bmi(50, 30)==[14.56, "underweight"]
    assert calculate_bmi(40, 20)==[20.02, "normal weight"]
    assert calculate_bmi(40, 10)==[40.94, "overweight"]
    assert calculate_bmi(50, 10)==[56.41, "obese"]
