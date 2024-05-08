#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-3"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["Core_131"] = [ 115030, 116477,]

on["Core_41"] =  [ 112173, 112185,]

on["Core_42"] =  [ 112187, 112191,]

on["Core_43"] =  [ 113275, 113277,]

on["Core_56"] =  [ 113281, 113283,]

on["Core_59"] =  [ 113416, 113418,]

on["Core_62"] =  [ 113422, 113424,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["Core_131"] = ""
pars1["Core_41"] = ""
pars1["Core_42"] = ""
pars1["Core_43"] = ""
pars1["Core_56"] = ""
pars1["Core_59"] = ""
pars1["Core_62"] = ""



#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["Core_131"] = ""
pars2["Core_41"] = ""
pars2["Core_42"] = ""
pars2["Core_43"] = ""
pars2["Core_56"] = ""
pars2["Core_59"] = ""
pars2["Core_62"] = ""


pars3 = {}
pars3["Core_131"] = ""
pars3["Core_41"] = ""
pars3["Core_42"] = ""
pars3["Core_43"] = ""
pars3["Core_56"] = ""
pars3["Core_59"] = ""
pars3["Core_62"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
