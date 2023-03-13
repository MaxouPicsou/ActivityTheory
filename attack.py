import argparse
import snap7
from snap7.util import *
from snap7.types import *
from snap7.exceptions import *
import socket
import math
import time


PLC_connection = snap7.client.Client()
IP_ADDRESS = "192.168.101.11"
RACK = 0                          
SLOT = 2

PLC_connection.connect(IP_ADDRESS, RACK, SLOT)

if PLC_connection.get_connected():
    PLC_connection.plc_stop()
