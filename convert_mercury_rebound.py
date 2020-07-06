# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + Collapsed="false"
#!/usr/bin/env python3

'''
Convert mercury6 output into a REBOUND simulation archive.
'''

# + Collapsed="false"
import os, sys
import re

# + Collapsed="false"
from rebound import Simulation


# + Collapsed="false"
def main():
    args = sys.argv[1:]
    from argparse import ArgumentParser
    psr = ArgumentParser(description="Convert Mercury6 output into REBOUND archive.")
    psr.add_argument('input_dir', type=str, help='Simulation directory')
    args = psr.parse_args(args)
    indir = args.input_dir
    
    sim_name = os.path.basename(os.path.normpath(indir))

# Get surviving planets from element.out
    try:
        el_out = open(os.path.join(indir, 'element.out'), 'r')
        pl_remain = []
        plan_re = re.compile(r'^\s*(plan\d+)')
        for l in el_out:
            match = re.search(plan_re, l)
            if match:
                pl_remain.append(match.group(1))
    except:
        print("Could not find element.out. Run element6.for.")
        raise
    
    # Create simulation
    sim = Simulation()
    sim.units = ('day', 'AU', 'Msun')
    # Add central star
    sim.add(m=1)
    # Add planets
    for pl in pl_remain:
        # Read last line of appropriate file
        pl_file = os.path.join(indir, pl+'.aei')
        with open(pl_file, 'rb') as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            final = f.readline().decode()
            # Assume Cartesian positions and velocities.
            t, x, y, z, u, v, w, m = [float(s) for s in final.split()]
            sim.add(m=m, x=x, y=y, z=z, vx=u, vy=v, vz=w)

    sim.save(os.path.join(os.getcwd(), 'rebsims/'+sim_name+'.bin'))
    return


# + Collapsed="false"
if __name__ == '__main__':
    main()

# + Collapsed="false"

