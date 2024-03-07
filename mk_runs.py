#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-3"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["Core_41"] =  [ 112173, 112185,]

on["Core_42"] =  [ 112187, 112191,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["Core_41"] = ""
pars1["Core_42"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["Core_41"] = ""
pars2["Core_42"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
