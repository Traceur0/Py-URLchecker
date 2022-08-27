from requests import get
import os
import time
from collections import Counter

from message import err_no_address, err_all_site_down, done, waiting_input



websites = []
status_col = []


def check_n_print():
    os.system('cls')
    print("Checking url...\n")
    res_code = "" # ONLINE or UNAVAILABLE
    for url in websites:
        # exception
        res = ""
        try:
            res_code = get(url, timeout=1, verify=False).status_code # option : allow_redirects=False timeout=1, verify=False
        except:
            res_code = "UNAVAILABLE"
        
        # if res_code == 200:
        #     res = "ONLINE"
        # else:
        #     res = "UNAVAILABLE"
        status_col.append(res_code)
        print(f"website : {url}\nstatus : {res_code}\n")
        time.sleep(0.8)

    stat_counter = Counter(status_col)
    # print(stat_counter["UNAVAILABLE"], len(status_col))
    if stat_counter["UNAVAILABLE"] == len(status_col):
        if len(status_col) == 0:
            os.system('cls')
            count_sec = countdown(5)
            err_no_address(count_sec)
            input_address()
        else:
            err_all_site_down()
    else:
        done()


def input_address():
    while True:
        # gate
        time.sleep(0.5)
        os.system('cls')
        input_msg = waiting_input()
        website = input(input_msg)
        # conditions
        if website == "":
            break
        elif website.startswith("https://") or website.startswith("http://"):
            websites.append(website)
        else:
            website = f"https://{website}"
            websites.append(website)
    check_n_print()


def countdown(secs):
    for sec in range(secs):
        print(f"\rreturn to previous page in '{(secs+1)-(sec+1)}' sec...", end="")
        time.sleep(1)