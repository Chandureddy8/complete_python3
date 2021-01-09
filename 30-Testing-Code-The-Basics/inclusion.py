import unittest

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        # self.assertTrue("k" in "king")

        self.assertIn("k", "king")
        self.assertIn(1, [1, 2, 3])
        self.assertIn(5, (6, 5, 7))
        self.assertIn("a", { "a": 1, "b": 2})
        self.assertIn("a", { "a": 1, "b": 2}.keys())
        self.assertIn(2, { "a": 1, "b": 2}.values())
        self.assertIn(55, range(50, 59))

    def test_non_inclusion(self):
        self.assertNotIn("w", "king")
        self.assertNotIn(10, [1, 2, 3])
        self.assertNotIn(15, (6, 5, 7))
        self.assertNotIn("c", { "a": 1, "b": 2})
        self.assertNotIn("c", { "a": 1, "b": 2}.keys())
        self.assertNotIn(5, { "a": 1, "b": 2}.values())
        self.assertNotIn(65, range(50, 59))

if __name__ == "__main__":
    unittest.main()