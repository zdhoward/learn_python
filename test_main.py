import main

def test_l_1():
    assert main.l_1() == "Hello World", "main() must return 'Hello World'"

def test_l_2():
    assert main.l_2(846, 936) == 846 + 936

def test_l_3():
    assert main.l_3([8576,4567,2543,7654,1856]) == 2543

def test_l_4():
    assert main.l_4(['Zz', 'Qq', 'Cc', 'Uu']) == ['Cc', 'Qq', 'Uu', 'Zz']

def test_l_5():
    assert main.l_5([1, 2, 3, 4]) == [1, 2, 3, 4, 'Hello']

def test_l_6():
    assert main.l_6({1: 'Data', 'Gremlin': 'Evil'})['Hello'] == 'World'

def test_l_7():
    dict = main.l_7()
    assert dict["One"] + dict["Two"] == dict["Three"]

def test_l_8():
    assert main.l_8([1,2,3,4,5,6]) == ['EIGHT','EIGHT','EIGHT','EIGHT','EIGHT','EIGHT']

def test_l_9():
    assert main.l_9([1,2,3,'Hello', 'World', 4, 'Not a digit']) == ['NINE', 'NINE', 'NINE', 'Hello', 'World', 'NINE', 'Not a digit']

def test_l_10():
    assert main.l_10(5, 2) == 1

def test_l_11():
    assert main.l_11([1,2,'Hello',4,5]) == [1,'Hello',5]

def test_l_12():
    assert main.l_12(['Afgd', 'Bfgd', 'Hello', 'World', 'Csda', 'asda', 'bsdfs', 'cadas']) == ['Hello', 'World']

def test_l_13():
    from datetime import date
    assert main.l_13() == date.today()

def test_l_14():
    from datetime import date
    assert main.l_14() == date.today().strftime("%A %d, %B %Y")

def test_l_15():
    from os.path import dirname, abspath
    assert main.l_15() == dirname(abspath(__file__))

def test_l_16():
    from os.path import dirname, abspath
    from os import listdir
    assert main.l_16() == listdir(dirname(abspath(__file__)))

def test_l_17():
    assert main.l_17('all,of,these,commas') == ['all', 'of', 'these', 'commas']
