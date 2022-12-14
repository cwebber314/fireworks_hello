from fireworks import Firework, Workflow, LaunchPad, ScriptTask
from fireworks.core.rocket_launcher import rapidfire

# set up the LaunchPad and reset it
launchpad = LaunchPad()
launchpad.reset('', require_password=False)

# create the individual FireWorks and Workflow

# Method1: define dependency/parent in Workflow creation
#fw1 = Firework(ScriptTask.from_str('echo "hello"'), name="hello")
#fw2 = Firework(ScriptTask.from_str('echo "goodbye"'), name="goodbye")
#wf = Workflow([fw1, fw2], {fw1:fw2}, name="test workflow")

# Method2: define dependency/parent in task creation
fw1 = Firework(ScriptTask.from_str('echo "hello"'), name="hello")
fw2 = Firework(ScriptTask.from_str('echo "goodbye"'), name="goodbye", parents=[fw1])
wf = Workflow([fw1, fw2], name="test workflow")

# store workflow and launch it locally
launchpad.add_wf(wf)
rapidfire(launchpad)