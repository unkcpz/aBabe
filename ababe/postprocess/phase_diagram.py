# coding: utf-8
# Distributed under the terms of the MIT License.

######################################################################
## Most algorithom refer to pymatgen/pymatgen/analysis/tests/

# Shyue Ping Ong, William Davidson Richards, Anubhav Jain, Geoffroy Hautier,
# Michael Kocher, Shreyas Cholia, Dan Gunter, Vincent Chevrier, Kristin A.
# Persson, Gerbrand Ceder. Python Materials Genomics (pymatgen) : A Robust,
# Open-Source Python Library for Materials Analysis. Computational
# Materials Science, 2013, 68, 314–319. doi:10.1016/j.commatsci.2012.10.028
######################################################################


class PhaseDiagramUnit(object):
    """
        The instance of class is a specific entry of the calculated
        structure.
        The class also contains the method to convey the csv data to the
        list of phase diagram data entries.
    """

    def __init__(self, formula, energy):
        self.formula = formula
        self.energy = energy


class PhaseDiagram(object):

    def __init__(self, pdunits, elements):
        """
            pdunits is a list of PhaseDiagramUnit()
            elements is a list of elements
        """
        dim = len(elements)


class PhaseDiagramPlotter(object):
    """
        Plot phase diagrams
    """

    def __init__(self, phasediagram):
        self._pd = phasediagram
        self._dim = self._pd.dim
        if self._dim > 3:
            raise ValueError("Only 1-3 components supported!")

    @property
    def pd_plot_data(self):
        """
        Plot data for phase diagram.

        Return:(lines, dstables, dunstables)
        lines is a list of point-point pairs can be connected as
        hull or phasediagram
        dstables and dunstables are two dict contain
        point position and its H-Energy
        """
        pd = self._pd
        return lines, dstables, dunstables

    def get_plot(self):
        if self._dim == 4:
            plt = self._get_3d_plot()
        else:
            plt = self._get_2d_plot()

        return plt

    def show(self, *args, **kwargs):
        """
            Args are passed to get_plot()
        """
        self.get_plot(*args, **kwargs).show()

    def _get_bin_hull_plot(self):
        import matplotlib.pyplot as plt

        (lines, dstables, dunstables) = self.pd_plot_data
        stable_ratio = list(dstables.keys())
        stable_h = list(dstables.values())
        unstable_ratio = list(dunstables.keys())
        unstable_h = list(dunstables.values())

        ax = fig.add_subplot(111)
        ax.scatter(stable_ratio, stable_h)
        ax.scatter(unstable_ratio, unstable_h)

        for pa, pb in lines:
            ax.plot([pa[0], pb[0]], [pa[1], pb[1]], "k-", linewidth=3)

        return plt

    def _get_tern_hull_plot(self):
        import matplotlib.pyplot as plt
        from mpl_toolkets.mplot3d import Axes3D

        (lines, dstables, dunstables) = self.pd_plot_data
        stable_ratio = list(dstables.keys())
        stable_h = list(dstables.values())
        unstable_ratio = list(dunstables.keys())
        unstable_h = list(dunstables.values())

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(stable_ratio[0], stable_ratio[1], stable_h)
        ax.scatter(unstable_ratio[0], unstable_ratio[1], unstable_h)

        for pa, pb in lines:
            ax.plot([pa[0], pb[0]], [pa[1], pb[1]], [pa[2], pb[2]], "k-", linewidth=3)

        return plt

    def _get_tern_pd_plot(self):
        import matplotlib.pyplot as plt

        (lines, dstables, dunstables) = self.pd_plot_data
        stable_ratio = list(dstables.keys())

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(stable_ratio[0], stable_ratio[1])

        for pa, pb in lines:
            ax.plot([pa[0], pb[0]], [pa[1], pb[1]], "k-", linewidth=3)

        return plt
