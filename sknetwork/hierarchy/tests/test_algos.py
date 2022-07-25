#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 2020
@author: Quentin Lutz <qlutz@enst.fr>
@author: Thomas Bonald <tbonald@enst.fr>
"""

import unittest

from sknetwork.data.test_graphs import *
from sknetwork.embedding import Spectral
from sknetwork.hierarchy import LouvainHierarchy, LouvainIteration, Paris


class TestLouvainIteration(unittest.TestCase):

    def test(self):
        louvain_iteration = LouvainIteration()
        louvain_iteration_options = LouvainIteration(resolution=2, depth=1)
        louvain_hierarchy = LouvainHierarchy()
        louvain_hierarchy_options = LouvainHierarchy(resolution=2, depth=1)
        paris = Paris()
        paris_options = Paris(weights='uniform', reorder=False)
        for algo in [louvain_iteration, louvain_iteration_options, louvain_hierarchy, louvain_hierarchy_options, paris, paris_options]:
            for input_matrix in [test_graph(), test_digraph(), test_bigraph()]:
                dendrogram = algo.fit_transform(input_matrix)
                self.assertEqual(dendrogram.shape, (input_matrix.shape[0] - 1, 4))
                if algo.bipartite:
                    self.assertEqual(algo.dendrogram_full_.shape, (sum(input_matrix.shape) - 1, 4))
