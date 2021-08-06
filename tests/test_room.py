from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room
from project.appliances.fridge import Fridge


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("Test", 100, 2)

    def test_init(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_set_expenses_negative_number_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -2
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_set_expenses_positive_number(self):
        self.room.expenses = 3
        self.assertEqual(3, self.room.expenses)

    def test_calculate_expenses(self):
        self.assertEqual(0, self.room.expenses)
        c1 = Child(5, 4, 1)
        expected = 300
        self.room.calculate_expenses([c1])
        self.assertEqual(expected, self.room.expenses)



if __name__ == "__main__":
    main()