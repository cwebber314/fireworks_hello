"""

Check that custom tasks can be found:

    lpad get_fws -i 1 -d all
"""
from fireworks import Firework, FWorker, LaunchPad, FWAction, FiretaskBase
from fireworks.core.rocket_launcher import launch_rocket
import random
import time

from CustomTasks import firetasks

# set up the LaunchPad and reset it
launchpad = LaunchPad()
# Or run this command to reset everything
# lpad reset
# launchpad.reset('', require_password=False)

# create the Firework consisting of a custom "Addition" task
i = 0
NJOBS = 10
while True:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f"Creating addition task: {a} + {b}")
    spec = {
        "mon": 'c:\\path\\to\\Monitor.mon',
        "con": 'c:\\path\\to\\Contingencies.con',
        "sub": 'c:\\path\\to\\Subsystem.sub',
        "case": f'c:\\path\\to\\MyModel_{i}.sub',
        }
    firework = Firework(firetasks.RunSim(), spec=spec)
    # store workflow and launch it locally
    launchpad.add_wf(firework)
    time.sleep(1)
    i += 1
    if i > NJOBS:
        break
        # pass
    # Launch it somewhere else
    #launch_rocket(launchpad, FWorker())