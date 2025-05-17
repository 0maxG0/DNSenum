# -*- coding: utf-8 -*-
#Quick simple subdomain enum
#Use amass together

import json
import os

#jsonデータの読み取り
json_data = '{"target_domain":"example.com","wordlist":"n0kovo_subdomains_small.txt"}'
data = json.loads(json_data)

#ターゲットドメイン名の取得
target_domain = data["target_domain"]

#ワードリストの読み込み(zone tranferが失敗した場合)
with open('n0kovo_subdomains/n0kovo_subdomains_tiny.txt', 'r') as file:
    while True:
        line = file.readline()
        line = line.strip()
        os.system(f'dig {line}.{target_domain} | grep -A 10 "ANSWER SECTION" | grep "IN" | grep -e A -e CNAME -e TXT >> result.txt')
        if not line:
            break

#cat amass.txt | grep -v aaaa_record | grep -v ASN | grep -v : | cut -d' ' -f1 | sed -E 's/::.*$//; s/\/[0-9]+$//'

