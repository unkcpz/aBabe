# coding: utf-8
# Distributed under the terms of the MIT License.
from ..phase_diagram import PhaseDiagramPlotter, PhaseDiagram, PhaseDiagramUnit
import unittest

module_dir = os.path.dirname(os.path.abspath(__file__))

class TestPDUnit(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        pass

    def test_from_csv(self):
        pass


class TestPDClass(unittest.TestCase):

    def setUp(self):
        pddatas = PhaseDiagramUnit.from_csv(os.path.join(
            module_dir, "pddata.csv"))
        self.pd = PhaseDiagram(pddatas)

    def test_init(self):
        pass


class TestPDPlotter(unittest.TestCase):

    def setUp(self):
        pddatas_tern = PhaseDiagramUnit.from_csv(os.path.join(
            module_dir, "pddata.csv"))
        self.pd_tern = PhaseDiagram(pddatas)
        self.plotter_tern = PhaseDiagramPlotter(self.pd_tern)

        # pddatas_bin = PhaseDiagramUnit.from_csv(os.path.join(
        #     module_dir, "data_bin.csv"))
        # self.pd_bin = PhaseDiagram(pddatas_bin)
        # self.plotter_bin = PhaseDiagramPlotter(self.pd_bin)

    def test_get_plot(self):
        # Only test if the method are callable
        self.plotter._get_tern_hull_plot()
        # self.plotter._get_tern_pd_plot()

        # self.plotter_bin ._get_bin_hull_plot()
