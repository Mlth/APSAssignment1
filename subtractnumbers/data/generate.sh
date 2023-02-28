#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution answer.py              # Use ../submissions/accepted/js_100.cpp to generate answer files

compile generate_random.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1

tc  random1 generate_random
tc  random2 generate_random
tc  random3 generate_random
tc  edge1 generate_explicit 0 0
tc  edge2 generate_explicit -1 -1
tc  edge3 generate_explicit 1 -1
tc  edge4 generate_explicit 40 1
tc  edge-huge generate_explicit 400 1
tc  edge-huge-neg generate_explicit -999 -999
tc  edge-huge-pos generate_explicit 999 999