from __future__ import division, absolute_import

import cowrie.core.output
from cowrie.core.config import CONFIG

import redis
import json
import sys, os
# Add path to support external library
current_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(current_path)
from PyMISPWrapper.RedisToMISP import MISPItemToRedis

class Output(cowrie.core.output.Output):

    def __init__(self):
        cowrie.core.output.Output.__init__(self)

    def start(self):
        """
        Initialize helper
        """
        self.host = CONFIG.get('output_cowrieToRedis', 'host')
        self.port = CONFIG.get('output_cowrieToRedis', 'port')
        self.db = CONFIG.get('output_cowrieToRedis', 'db')
        self.keyname = CONFIG.get('output_cowrieToRedis', 'keyname')
        self.helper = MISPItemToRedis(self.keyname, host=self.host, port=self.port, db=self.db)

    def stop(self):
        pass

    def write(self, logentry):
        """
        Push to log entry to redis
        """
        # Add the entry to redis
        for i in list(logentry.keys()):
            # Remove twisted 15 legacy keys
            if i.startswith('log_'):
                del logentry[i]
            # Add object name to use the correct MISP object template
            logentry['name'] = 'cowrie'
        self.helper.push_object(logentry)
