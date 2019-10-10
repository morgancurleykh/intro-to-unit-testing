from computations import computeNewNumber


def test_0():
    assert computeNewNumber(0) == 27613.874975264072


def test_1():
    assert computeNewNumber(1) == 2.185471534729004


def test_2():
    assert computeNewNumber(2) == 5.574462890625


def test_3():
    assert computeNewNumber(3) == 26.23446750640869


def test_5():
    assert computeNewNumber(5) == 206.4285593032837


def test_7000():
    assert computeNewNumber(7000) == 15.204422950744629
