import copy
import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    v = Vector([1, 2, 3])
    w = Vector([4, 5, 6])

    def test_str(self):
        self.assertEqual(str(self.v), "[1, 2, 3]", "should be = [1, 2, 3]")

    def test_len(self):
        self.assertEqual(len(self.v), 3, "should be = 3")

    def test_lt(self):
        self.assertTrue(self.v < self.w, "v should be less than w")

    def test_le(self):
        self.assertTrue(
            (self.v <= self.v) == (self.v <= self.w),
            "v should be less than equal to v and less than equal to w",
        )

    def test_getitem(self):
        for i in range(1, 4):
            self.assertEqual(self.v[i - 1], i)

    def test_setitem(self):
        # shallow copy still affect the class variable v
        v_copy = copy.deepcopy(self.v)
        v_copy[0] = 10
        self.assertEqual(v_copy, Vector([10, 2, 3]), "should be [10, 2, 3]")

    def test_magnitude(self):
        self.assertAlmostEqual(self.v.magnitude(), 3.741657387)

    def test_normalized(self):
        mag = 3.741657387
        other = Vector([1 / mag, 2 / mag, 3 / mag])
        for first, second in zip(self.v.normalized().components, other.components):
            self.assertAlmostEqual(first, second)

    def test_dot(self):
        self.assertEqual(self.v.dot(self.w), 32, "should be = 32")

    def test_angle(self):
        theta = 12.933154491899105
        self.assertAlmostEqual(self.v.angle(self.w), theta)

    def test_rotation(self):
        a = Vector([2, 4])
        print(a.rotate(90))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVector)
    unittest.TextTestRunner(verbosity=2).run(suite)
