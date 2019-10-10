from computations import *


def test_0():
    end_result = step_4(step_3(step_2(step_1(0))))
    assert computeNewNumber(0) == end_result


def test_1():
    end_result = step_4(step_3(step_2(step_1(1))))
    assert computeNewNumber(1) == end_result


def test_step_1():
    assert step_1(1) == 40


def test_step_2():
    assert step_2(2) == 0


def test_step_3():
    assert step_3(2) == 0.03125


def test_step_4():
    assert step_4(2) == 18
