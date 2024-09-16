import time
from datetime import datetime

epoch_seconds = time.time()

print(f"Seconds since January 1, 1970: {epoch_seconds:,.4f} or {epoch_seconds:.2e} in scientific notation")

now = datetime.now()
formatted_date = now.strftime("%b %d %Y")

print(formatted_date)
