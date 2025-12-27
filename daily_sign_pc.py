import os
import requests

cookie = os.environ.get("JD_COOKIE_PC")

import requests
cookies = {
    '^__jdv': '76161171^|direct^|-^|none^|-^|1766802930564',
    '__jdu': '17668029305631544393914',
    'areaId': '1',
    'ipLoc-djd': '1-2805-0-0',
    'PCSYCityID': 'CN_110000_110100_0',
    'shshshfpa': '62008d77-6091-ea92-f81d-315f5ac6b9f1-1766802936',
    'shshshfpx': '62008d77-6091-ea92-f81d-315f5ac6b9f1-1766802936',
    'jcap_dvzw_fp': 'xSovnXGl_ZvBCvEIUFflnODfZR3i9_ec_HqhVzf7laL5QSoJdWNf-sLwQCSJz-at0z9r7atoLVY6gBClGyxVCWXP4XY=',
    'whwswswws': '',
    'commonAddress': '4551928385',
    'regionAddress': '1^%^2C72^%^2C2819^%^2C0',
    'b_webp': '1',
    'b_avif': '1',
    'autoOpenApp_downCloseDate_auto': '1766807397666_1800000',
    'autoOpenApp_downCloseDate_jd_homePage': '1766821711058_1',
    'warehistory': '^\\^10135446986182,^\\^',
    'b_dw': '375',
    'b_dh': '667',
    'b_dpr': '2.000000013623918',
    'pt_st': '1_T_ebGKZnFE7fp62QLvkcDbQa7NepD5NQgCQ3ttt4lcW8HL4-3SNejAcOlppci7oKyc39NH8241IPD7BOh9_PY4_XRov9cbebS_feBW5mLIDIAUkriNOMfRznNB11i3k1UWQzc8DQnBmxR_0b5qEvWeNtxQAddWj7vvUFLhYcgAzdqDnYuBQziA4CkGqFelekTI2sxNFpx0k_xTdxMi004bLW1ScHl9uUmU7CEGK*',
    'TrackID': '1oIUJhUYjIncBKEvDbAQBWVdq2CWXe4SZ41CmcXq4euR7q74Xv1EfTuvQc1yTfH3sURIcxYnLYZJ3eB8mwjq0X5zpgIdEnHOwl2LRt9yP_rk',
    'thor': '9F78F5CB4FCD0C7DCCD66CEE8C5B28B427E4B00F6A0E2C713A957D1E266A2CE8DB85DB96F8A0CDC742C3F9C1D58FD52D208C55247A6AADD1EFCCA4AAA5559F5BF2677B0ECBEEC5925D8E4CCC34335A345BC539AA268174FDE6568BD832B2429ECF269800AEDAABC6A033D3FC632A9D64FFEC370A5FD73C5923E53B15B8D19B4157B8F4C0A731459B9795E9F15E8AB11186CC84D2C9F41F8A9C8667FD83860D25',
    'light_key': 'AASBKE7rOxgWQziEhC_QY6yaQGruGa0jfiOTAjG1ax3WNSZgCBYN6HaEX1IoICNtkWYfUfUz',
    'pinId': '12uPPepjUqw5xAPgfccTpA',
    'pin': 'jd_bFyOzGKCBbrj',
    'unick': 'u_5to9xq1ipqvl',
    'ceshi3.com': '000',
    '_tp': '7uCzlC0AWm2^%^2BV4fNUZVFpQ^%^3D^%^3D',
    '_pst': 'jd_bFyOzGKCBbrj',
    'wlfstk_smdl': 'w06bnossgs9i3i7aofbzhjafl1qgzarw',
    'mail_times': '4^%^2C1^%^2C1766823285998',
    'umc_count': '1',
    'source': 'PC',
    'platform': 'pc',
    'shshshfpb': 'BApXWpzviXf5A3-9S2wQjYKeA6Zc7xzzPXTTV_qzo9xJ1MkV-Uo-25BYDQg',
    'joyya': '1766823996.1766824027.29.1ckfhr9',
    '3AB9D23F7A4B3CSS': 'jdd03SWJPTXSPNC3YLWZEDIPA7YYXE55CHIHNYNII32REDFKHGUHXBPRHFGTNWPTIP3VIGEXNDKG47N5A6EBVWADELEDJ6EAAAAM3L4QCZYAAAAAACLACKEGW2JCP3MX',
    'flash': '3_fPTOf2Iqf7aeusW2QMF-gWn4qwRf_1JOBXoKwbfTEkXeP1UpuhhPRGBUuqc1hn-pEjjkqscF2NLwqX5mMc5B-zZuFmGCUyYxUp5YUoGe219w5DtSDfmsBQs65d5qm93a3sZ9fhtY5yxjCrrLb1O3nB8N8XP1uYjoC83Wzys-CDaPPq9Z49vs',
    '3AB9D23F7A4B3C9B': 'SWJPTXSPNC3YLWZEDIPA7YYXE55CHIHNYNII32REDFKHGUHXBPRHFGTNWPTIP3VIGEXNDKG47N5A6EBVWADELEDJ6E',
    '__jda': '76161171.17668029305631544393914.1766802931.1766821710.1766827503.4',
    '__jdc': '76161171',
    '__jdb': '76161171.4.17668029305631544393914^|4.1766827503^',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://bean.jd.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bean.jd.com/myJingBean/list?spmTag=YTAyMTkuYjAwMjM1Ni5jMDAwMDY0NTMuZG91',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'Cookie': cookie
}

data = {
  'h5st': '20251227161533986;zawg36w9ghd6j3j8;73c2f;tk03w95f11bdd18nP6OHNogas8TOtvO4PE0QRAEKLKvzM-Y9-nqjufqUCPusrt1C8i1PqgTGJxTH9KnFZN8nUpOtR5cL;fc803181e69deb79ca4f016ce51761a0;5.2;1766823328986;fZRCXZfT3U_HrRbH68uErVuIqc7D-h-T-h6I-hfZXxfTB5_ZzUrJ-hfZXx-ZwZuV9YOVpJeI-Y7IxJOT7geVwNuV88eVwZLUq9eTsJ_ZB5_ZxIdG6YLIqYfZB5hW-VbIvReVpFuJ-EeUtJLJrFeIrJOVpZOTsNLJvRuJwNOI-h-T-VKJroLJ_YfZB5hW-h_ZB5_ZtN6J-hfZXx-Zrp-VzN_ECMbG4IrKsB7ZB5_ZrYfZB5hW-FtPNo9Qv9MVZc9ZB5_Z0kbIzc7F-hfZXx-ZvV_G4E8ZB5_Z7g6ZBh-f1taZB5BZ0I9ZB5_ZudOE-YfZBhfZXx-VB5_ZwdOE-YfZBhfZXxfUwh-T-hOVsY7ZBhfZB5hWptfZnZ-VwN6J-hfZBh-f1ZPVK4cUvl7LwQ6ZB5_Z0kbIzc7F-hfZBh-f1heZnZfTsY7ZBhfZB5hWxh-T-FOE-YfZBhfZXx-Vvh-T-JOE-YfZBhfZXxfVB5_ZsN6J-hfZBh-f1heZnZfUsY7ZBhfZB5hWsZeZnZvVsY7ZBhfZB5hW-R_WwpfV-h-T-dOE-YfZBhfZXxfVB5_Z2E6ZBhfZB5hWsh-T-VaG-hfZBh-f1heZnZfG-hfZBh-f1heZnZfIqYfZBhfZX1aZnZfIzMbEpM7ZBh-f1taZB5BZ3Y6JfUtPa4qOoI9JCQ7H-h-T-ZeF-hfZBh-fmg-T-haF-hfZXx-ZtJeDB1eUrpLHKgvTxpfVwhfMTgvFqkbIz8rM-h-T-dLEuYfZB5xD;e422ebdf86af94a49519d9074d7d8c80;gRaW989Gy8bE_oLE7w-Gy8rFvM7MtoLI4wrJ1R6G88bG_wPD9k7J1RLHxgKJ',
  'uuid': '17668029305631544393914',
  'loginType': '3',
  'appid': 'asset-h5',
  'clientVersion': '1.0.0',
  'client': 'pc',
  't': '1766823328983',
  'body': '{"type":5,"eaId":"4KpUNjgQZtanUeeqbhMYjT47b9Fo","itemId":"1","extraType":"sign"}',
  'functionId': 'pc_interact_sign_execute',
  'x-api-eid-token': 'jdd03SWJPTXSPNC3YLWZEDIPA7YYXE55CHIHNYNII32REDFKHGUHXBPRHFGTNWPTIP3VIGEXNDKG47N5A6EBVWADELEDJ6EAAAAM3L3PMKVQAAAAACDNU33VUTT2RHUX',
  'area': '1_2805_0_0'
}

response = requests.post('https://api.m.jd.com/', headers=headers, data=data)

print("PC签到结果："+response.text)
