# FireWorks

[FireWorks](https://materialsproject.github.io/fireworks/) is an open-source code for
defining, managing, and executing complext workflows.  This repo contains a couple simple 
examples I'm using to learn about the tools.

## Simulation Mockup

This example simulates launching a long running anylsis.  

First add this directory to the PYTHONPATH so the `CustomTasks` can be found.

Start by queueing up some long-running tasks:
```
python producer_sim.py
```

Nothing will happen until you start the workers. You can launch the workers on
the local box or multiple remote boxes:
```
rlaunch rapidfire --nlaunches infinite
```

## Tutorial

Start clean:
```
lpad reset
```

Add a two step workflow:
```
lpad add_scripts "echo hello" "echo goodbye" -n hello goodbye -w test_workflow
```

Make sure it's added:
```
lpad get_wflows -n test_workflow -d more
```

Launch jobs:
```
rlaunch --silencer rapidfire
```

## Custom Tasks and Multiple workers

Make sure you add the `CustomTasks` to `PYTHONPATH`:
```
SET PYTHONPATH=c:\cwebber\fireworks_hello
```

Queue up some jobs:
```
python producer.py
```

To check that the jobs are submitted:
```
lpad get_fws
```

or:
```
lpad webgui
```

To run the top job:
```
rlaunch singleshot
```

or run it forever:
```
rlaunch rapidfire --nlaunches infinite
```



## Dashboard

Run:
```
lpad webgui
```

Or open it on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)