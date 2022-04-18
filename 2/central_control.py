# This node will be responsible for taking in all new queries for acceptance, 
# directing it to the least dense node for processing, verification, and admittance

# If any new node is admitted into the network, the assigner has to generate a key and share it with
# this node, so that the new node verifies its admittance by relaying the key for cross verification.

# This is the genesis node, the first node of the network

import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
import numpy as np
import calendar

deployment_port_number = '5000'

deployment_url = '127.0.0.1'

deployment_link = 'http://' + deployment_url + ':' + deployment_port_number

node_def = [('url','S500'),('key','S64'),('node-density','i8'),('birth-time','datetime64[s]')]

active_requests_def  = [('time_sent','datetime64[s]'),('requester','s500'),('handler','s500')]

class Network:

    def __init__(self):
        
        #stores the details of all nodes within the network
        self.nodes = np.zeros((1), dtype = node_def)

        #storing the entry of the first node of the network
        present_date = calendar.timegm(datetime.datetime.now().timetuple())
        hashed = hashlib.sha256(deployment_link.encode()).hexdigest()
        self.nodes[0] = (deployment_link,hashed,0,present_date)

        #stores the requests pending in the network, waiting for their results
        self.active_requests = np.zeros((0), dtype = active_requests_def)

    def get_least_congested_node(self):
        nodes_new = self.nodes['node-density']
        print(nodes_new)
        min_node_index = np.where(nodes_new == np.min(nodes_new))
        print(min_node_index[0])
        return self.nodes[min_node_index[0][0]]

    def add_active_requests(self,requester_info):
        sender_array = self.active_requests['requester']
        already_requested = np.where(sender_array == requester_info['url'])
        if len(already_requested[0]) == 0:
            sender_info = self.get_least_congested_node()
            new_active_request = np.zeros((1), dtype = active_requests_def)
            new_active_request[0] = ()
            self.active_requests = np.append(self.active_requests, )
        else:
            #already requested admission, donot allow
            print('Already requested entry, referendum ongoing')


network = Network()

print(network.get_least_congested_node())

