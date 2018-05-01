#!/bin/env python
"""
Copies best scoring files into a new directory called high_score
"""
from commands import getstatusoutput as run
# create best dictionary
best = {}
# populate dictionary with best scoring simulation for each phosphate
best["9_X"] = 19
best["10_Z"] = 338
best["1_W"] = 471
best['6_W'] = 254
best["5_Z"] = 490
best["4_Y"] = 336
best["8_Y"] = 7
best["9_Z"] = 257
best["8_W"] = 262
best["4_X"] = 302
best["2_X"] = 242
best["7_Y"] = 467
best["10_W"] = 253
best["2_W"] = 354
best["7_X"] = 115
best["9_Y"] = 268
best["8_X"] = 489
best["1_Z"] = 379
best["5_W"] = 172
best["5_X"] = 205
best["6_Y"] = 20
best["7_Z"] = 301
best["9_W"] = 69
best["4_Z"] = 194
best["6_X"] = 291
best["1_Y"] = 166
best["7_W"] = 372
best["4_W"] = 255

# Copy all the relevant files
for phosphate in sorted(best.keys()):
    cmd = "cp -v test%s/test%s_%i.pdb high_score/"%(phosphate,phosphate,best[phosphate])
    print run(cmd)
    cmd = "cp -v test%s/*.fasc high_score/"%(phosphate)
    print run(cmd)
    cmd = "rm -rfv test%s"%(phosphate)
    print run(cmd)[1]
