# encoding: utf-8
# Distributed under the terms of the MIT License.

import unittest

from ababe.stru.buckyball import Structure
from ababe.stru.element import Specie

class testBuckyballStructure(unittest.TestCase):

    def setUp(self):
        self.bucky = Structure([6]*60)
        self.speckle = Specie("B")

    def test_a(self):
        pass

    def test_all_speckle_gen(self):
        # all_nondup_structure = Structure.all_speckle_gen(self.bucky, 3, self.speckle)
        # self.assertIn(a, all_nondup_structure)
        pass

if __name__ == "__main__":
    import nose2
    nose2.main()