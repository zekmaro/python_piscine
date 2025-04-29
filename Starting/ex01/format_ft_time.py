import time

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

seconds = time.time()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")

current_month = time.localtime(seconds).tm_mon
current_day = time.localtime(seconds).tm_mday
current_year = time.localtime(seconds).tm_year

month_name = months[current_month - 1]

print(f"{month_name} {current_day} {current_year}")