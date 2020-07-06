#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for force atlas2 embeddings"""
import unittest

import numpy as np

from sknetwork.embedding.force_atlas import ForceAtlas2
from sknetwork.data.test_graphs import test_graph, test_digraph


class TestEmbeddings(unittest.TestCase):

    def test_options(self):
        for adjacency in [test_graph(), test_digraph()]:
            n = adjacency.shape[0]

            force_atlas = ForceAtlas2()
            layout = force_atlas.fit_transform(adjacency)
            self.assertEqual((n, 2), layout.shape)

            force_atlas = ForceAtlas2(lin_log=True)
            layout = force_atlas.fit_transform(adjacency)
            self.assertEqual((n, 2), layout.shape)

            force_atlas = ForceAtlas2(no_hubs=True)
            layout = force_atlas.fit_transform(adjacency)
            self.assertEqual((n, 2), layout.shape)

            force_atlas = ForceAtlas2(no_overlapping=True)
            layout = force_atlas.fit_transform(adjacency)
            self.assertEqual((n, 2), layout.shape)

            force_atlas = ForceAtlas2(barnes_hut=True)
            layout = force_atlas.fit_transform(adjacency)
            self.assertEqual((n, 2), layout.shape)

            force_atlas = ForceAtlas2(strong_gravity=True)
            layout = force_atlas.fit_transform(adjacency)
            self.assertEqual((n, 2), layout.shape)
            force_atlas.fit(adjacency, pos_init=layout, n_iter=1)

    def test_errors(self):
        adjacency = test_graph()
        with self.assertRaises(ValueError):
            ForceAtlas2(n_components=3, barnes_hut=True)
        with self.assertRaises(ValueError):
            ForceAtlas2().fit(adjacency, pos_init=np.ones((5, 7)))