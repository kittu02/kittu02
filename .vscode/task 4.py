import datetime

def dateAndTime():
  now = datetime.datetime.now(datetime.timezone.utc)
  ist_now = now.astimezone(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
  return f"{ist_now.strftime('%A %B %d %H:%M:%S')} IST {ist_now.year}"

print(dateAndTime())