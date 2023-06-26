#!/usr/bin/env python3
import unittest
from app.contact import Contact


class TestContact(unittest.TestCase):

    def foo(self):
        contact = Contact("O", "1")


if __name__ == "__main__":
    unittest.main()
