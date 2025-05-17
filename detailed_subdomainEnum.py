# -*- coding: utf-8 -*-
# required Amass and httpx

import json
import os

json_data = '{"target_domain":"google.com"}'
data = json.loads(json_data)

target_domain = data["target_domain"]

# create active/accessible domain lists
os.system(
    f"amass enum -d {target_domain} -active | grep -v aaaa_record | grep -v ASN | grep -v : | cut -d' ' -f1 | sed -E 's/::.*$//; s/\/[0-9]+$/ > cleaned.txt")
os.system("httpx -l cleaned.txt -status-code -title -tech-detect -o httpx_results.txt")
