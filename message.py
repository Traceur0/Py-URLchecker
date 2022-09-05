def err_no_address():
    print(f"""
+-------------------------------------------+
|                                           |     
|  ⚠ Error : type at least one address ⚠    |          
|                                           |
+-------------------------------------------+           
    """)


def err_all_site_down():
    print("""
+-------------------------------------------------------------------+
|                                                                   |
|   Expecting all website is down.                                  |
|   Please follow the instruction below if you need any solution.   |
|                                                                   |
|   1. Check your Network Online.                                   |
|       check your connection of LAN cable or Wi-Fi status.         |
|   2. de-activate custom Firewall setting.                         |
|   3. check your Proxy or VPN setting.                             |
|                                                                   |
+-------------------------------------------------------------------+
    """) 


def done():
    print("""
+-------------------+
|                   |
|   All-checked !   |
|                   |
+-------------------+
    """)


def waiting_input():
    return """
+---------------------------------------------------------------+
|                                                               |
|   Type your website address. e.g. https://www.blahblah.com    |
|                                                               |
|   If there's nothing to type in, just press ENTER button.     |
|                                                               |
+---------------------------------------------------------------+
>>>"""