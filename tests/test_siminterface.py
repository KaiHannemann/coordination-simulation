# -*- coding: utf-8 -*-
"""
Simulator interface tests
"""
from unittest import TestCase

from rlsp.simulator_interface import SimulatorInterface, SimulatorAction, SimulatorState

NETWORK_FILE = "/mnt/d/SWC/coordination-simulation/params/networks/Abilene.graphml"
SERVICE_FUNCTIONS_FILE = "/mnt/d/SWC/coordination-simulation/params/placements/Abilene.yaml"

SIMULATOR_MODULE_NAME = "siminterface.simulator"
SIMULATOR_CLS_NAME = "Simulator"
SIMULATOR_MODULE = __import__(SIMULATOR_MODULE_NAME)
SIMULATOR_CLS = getattr(SIMULATOR_MODULE, SIMULATOR_CLS_NAME)


class TestSimulatorInterface(TestCase):

    simulator = None  # type: SimulatorInterface

    def setUp(self):
        """
        create simulator for test cases
        """
        # TODO: replace SimulatorInterface with implementation
        self.simulator = SIMULATOR_CLS()
        self.simulator.init(NETWORK_FILE, SERVICE_FUNCTIONS_FILE, 0)

    def test_apply(self):

        placement = {
            'pop0': ['a', 'b', 'c'],
            'pop1': ['a', 'b', 'c'],
            'pop2': ['a', 'b', 'c'],

        }

        flow_schedule = {
            'pop0': {
                'a': {'pop0': 0.4, 'pop1': 0.6, 'pop2': 0},
                'b': {'pop0': 0.6, 'pop1': 0.2, 'pop2': 0.2},
                'c': {'pop0': 0.6, 'pop1': 0.2, 'pop2': 0.2}},
            'pop1': {
                'a': {'pop0': 0.3, 'pop1': 0.6, 'pop2': 0.1},
                'b': {'pop0': 0.6, 'pop1': 0.2, 'pop2': 0.2},
                'c': {'pop0': 0.6, 'pop1': 0.2, 'pop2': 0.2}},
            'pop2': {
                'a': {'pop0': 0.1, 'pop1': 0.6, 'pop2': 0.3},
                'b': {'pop0': 0.6, 'pop1': 0.2, 'pop2': 0.2},
                'c': {'pop0': 0.6, 'pop1': 0.2, 'pop2': 0.2}}}

        action = SimulatorAction(placement=placement,
                                 scheduling=flow_schedule)
        simulator_state = self.simulator.apply(action)
        self.assertIsInstance(simulator_state, SimulatorState)

# network
        """
        simulator_state.network =
            'nodes': [{
                'id': str,
                'resource': [float],
                'used_resources': [float]
            }],
            'edges': [{
                'src': str,
                'dst': str,
                'delay': int( in ns or ms?),
                'data_rate': int(unit?),
                'used_data_rate': int(unit?),
            }],
        """
        nw_nodes = simulator_state.network['nodes']
        self.assertIs(len(nw_nodes), 3)

        nw_edges = simulator_state.network['edges']
        self.assertIs(len(nw_edges), 3)

# sfcs
        """
        sfcs : list
            [{
                'id': str,
                'functions': list
                    ['id': str]
            }],
        """
        sfcs = simulator_state.sfcs
        self.assertIs(len(sfcs), 3)

# service_functions
        """
        service_functions : list
            [{
                'id': str,
                'processing_delay': int
            }],
        """
        service_functions = simulator_state.service_functions
        self.assertIs(len(service_functions), 3)

# traffic
        # TODO: test traffic

# network_stats
        """
        network_stats : dict
            {
                'total_flows' : int,
                'successful_flows' : int,
                'dropped_flows' : int,
                'in_network_flows' : int,
                 'avg_end_2_end_delay' : int
            }
        """
        network_stats = simulator_state.network_stats
        self.assertIs(len(network_stats), 5)
        self.assertIn('total_flows', network_stats)
        self.assertIn('successful_flows', network_stats)
        self.assertIn('dropped_flows', network_stats)
        self.assertIn('in_network_flows', network_stats)
        self.assertIn('avg_end_2_end_delay', network_stats)