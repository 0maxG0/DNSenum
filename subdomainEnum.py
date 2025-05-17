import json
import threading
import os

#jsonデータの読み取り
json_data = '{"target_domain":"example.com","wordlist":"n0kovo_subdomains_small.txt"}'
data = json.loads(json_data)

#目的:あるドメインのサブドメインを列挙する

#ターゲットドメイン名の取得
target_domain = data["target_domain"]

#マルチスレッドの作成
# t1 = threading.Thread(target, args)
# t2 = threading.Thread(target, args)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


#ワードリストの読み込み(zone tranferが失敗した場合)
with open('n0kovo_subdomains/n0kovo_subdomains_tiny.txt','r') as file:
    while True:
        line = file.readline()
        os.system(f'dig {line}.{target_domain}')
        if not line:
            break



#結果をファイル出力する


