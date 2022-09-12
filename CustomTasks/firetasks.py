"""Make sure your python environment can find this
"""
from fireworks import Firework, FWorker, LaunchPad, FWAction, FiretaskBase
import random
import time
from fireworks.utilities.fw_utilities import explicit_serialize
import shutil
import os
import pdb

@explicit_serialize
class MyTask(FiretaskBase):
    # The explicit_serialize is the only way I can get custom tasks to be found
    # _fw_name = "My Task"

    def run_task(self, fw_spec):
        input_array = fw_spec['input_array']
        m_sum = sum(input_array)

        processing_time = random.randint(1, 30)
        print(f"[2]sleep: {processing_time}")
        time.sleep(processing_time)

        print(f"[2]The sum of {input_array} is: {m_sum}")
        return FWAction(stored_data={'sum': m_sum}, mod_spec=[{'_push': {'input_array': m_sum}}])

@explicit_serialize
class RunSim(FiretaskBase):
    # The explicit_serialize is the only way I can get custom tasks to be found
    # _fw_name = "My Task"

    def run_task(self, fw_spec):
        mon = fw_spec['mon']
        con = fw_spec['con']
        sub = fw_spec['sub']
        case = fw_spec['case']

        # TODO: Sanity check inputs
        # TODO: Copy files

        cmd = f'c:\\path\\to\\simulator.exe {case}'
        print(cmd)

        retval = 0
        msg = 'Sim completed without errors'
        # os.system(cmd)

        # processing_time = 2
        processing_time = random.randint(10, 300)
        print(f"sleep: {processing_time}")
        time.sleep(processing_time)
        return FWAction(stored_data={'retval': retval, 'msg': msg})
