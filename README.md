# screeningtest1
 # isprime
Steps to test is prime or not using pytest (internet connection required) on Pycharm terminal
1. pip - h
2. pip install virtualenv
3. virtualenv isprime (create directory)
4. cd isprime
5. cd Scripts
6. activate
7. pip install pytest
8. create 2 files inside isprime directory- isprime.py (for coding) & test_isprime.py (for testing)
9. run the files in terminal by typing any :a) pytest
			           	   b) pytest -q test_isprime.py

Test report 

(isprime) D:\pythonProject\pythonProject\isprime>pytest
===================================================================== test session starts =====================================================================
platform win32 -- Python 3.8.8, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: D:\pythonProject\pythonProject\isprime
collected 6 items                                                                                                                                              

test_isprime.py F..F..                                                                                                                                   [100%]

========================================================================== FAILURES ===========================================================================
________________________________________________________________________ test_isprime1 ________________________________________________________________________

    def test_isprime1():
>       assert isprime(1) == False
E       assert True == False
E        +  where True = isprime(1)

test_isprime.py:3: AssertionError
________________________________________________________________________ test_isprime4 ________________________________________________________________________

    def test_isprime4():
>       assert isprime(5)
E       assert False
E        +  where False = isprime(5)

test_isprime.py:12: AssertionError
=================================================================== short test summary info ===================================================================
FAILED test_isprime.py::test_isprime1 - assert True == False
FAILED test_isprime.py::test_isprime4 - assert False
================================================================= 2 failed, 4 passed in 1.40s =================================================================



(isprime) D:\pythonProject\pythonProject\isprime>pytest -q test_isprime.py
F..F..                                                                                                                                                   [100%]
========================================================================== FAILURES ===========================================================================
________________________________________________________________________ test_isprime1 ________________________________________________________________________

    def test_isprime1():
>       assert isprime(1) == False
E       assert True == False
E        +  where True = isprime(1)

test_isprime.py:3: AssertionError
________________________________________________________________________ test_isprime4 ________________________________________________________________________

    def test_isprime4():
>       assert isprime(5)
E       assert False
E        +  where False = isprime(5)

test_isprime.py:12: AssertionError
=================================================================== short test summary info ===================================================================
FAILED test_isprime.py::test_isprime1 - assert True == False
FAILED test_isprime.py::test_isprime4 - assert False
2 failed, 4 passed in 0.11s

(isprime) D:\pythonProject\pythonProject\isprime>

