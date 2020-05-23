#! /usr/local/bin/micropython

import argparse
import time
from pybricks import ev3brick as brick
from pybricks.parameters import (Button, Stop)
from pybricks.tools import print, wait, StopWatch
from ev3_simulation.run_loop import RunLoop

# Simulator Initialization
parser = argparse.ArgumentParser()
parser.add_argument("--simulate", help="Run program in local simulation.", action="store_true")
args = parser.parse_args()

if args.simulate:
    print("Engage the simulation")
    run_loop = RunLoop()
    run_loop.start_simulation()


# Clear the display
brick.display.clear()
print('Hello World')

start_time = time.time()

while time.time() < start_time + 3:
    print("MAIN PROCESS: Hello World")

if args.simulate:
    print("Cleanup the simulation")
    run_loop.stop_simulation()
