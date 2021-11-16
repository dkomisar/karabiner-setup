#!/usr/bin/env python

import sys
import json

with open(sys.argv[1]) as input:
    y = json.load(input)

    for rule in y["rules"]:
        for manip in rule["manipulators"]:
            if "conditions" in manip.keys():
                for cond in manip["conditions"]:
                    if cond["type"] == "frontmost_application_unless":
                        cond["bundle_identifiers"].append("^com\\.microsoft\\.VSCode$")
    print(json.dumps(y, indent=2))