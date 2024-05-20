#!/usr/bin/env python3

# assert(1 == 2)
# lib/an_assertion_error.py

def test_values():
    assert(1 == 2), "Assertion failed: 1 is not equal to 2"

try:
    test_values()
except AssertionError as e:
    print(e)  # This will print "Assertion failed: 1 is not equal to 2"
