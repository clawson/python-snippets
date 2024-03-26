""" Dates and Times

    I needed to understand more about converting a specific timestamp string
    to a Python datetime, then do some date arithmetic.  So, this snippet
    runs through some examples.  It's very "chatty," but I'm OK with that.
    
"""

from zoneinfo import ZoneInfo
from datetime import datetime, timezone, timedelta, tzinfo

print("\n---=== Dates and Times ===---\n")

print("NOW()")

d1 = datetime.now(timezone.utc)
print("Is this a datetime object? ", isinstance(d1, datetime))
print("What is the tzinfo?  Is is 'aware?'", d1.tzinfo)
print("Datetime: ", d1)

print("\n----")
print('Given a string such as "2021-10-27T02:35:08.209Z":')

d2 = datetime.strptime("2021-10-27T02:35:08.209Z", "%Y-%m-%dT%H:%M:%S.%fZ")
print("Datetime object 'd2': ", d2)
print("Is 'd2' a datetime object? ", isinstance(d2, datetime))
print("What is the tzinfo for 'd2?'  Is is 'aware?'", d2.tzinfo)

d2 = d2.replace(tzinfo=timezone.utc)
print("What is the tzinfo for 'd2' now?  Is is 'aware' now?", d2.tzinfo)
print("Datetime object 'd2': ", d2)


print("\n---=== Datetime Arithmetic ===---\n")

print("NOW() minus 2021-10-27T02:35:08.209Z = ")

# NOTE: Both datetimes must be naive or both must be aware for subtraction.
# Also, beware of time zones.  Subtraction will take the tz into consideration.
# I am good here since both are UTC.

time_difference = d1 - d2
print(time_difference)
print("Is this a timedelta object? ", isinstance(time_difference, timedelta))

print("\n----")
print("Convert to a string so that I can lop off the seconds and milliseconds")
time_diff_str = str(time_difference)[:-10] + " hh:mm"
print(time_diff_str)
print("Is 'time_diff_str' a String? ", isinstance(time_diff_str, str))

print("\n")

print("\n---=== Datetime Time Zones ===---\n")

print("TZ name and offset?")
print("'d1': ", d1.tzname(), d1.utcoffset())
print("'d2': ", d2.tzname(), d2.utcoffset())

print("\n----")
print("Convert to MDT:")

mountain_tz = ZoneInfo("US/Arizona")
dz1 = d1.astimezone(mountain_tz)
print("Is 'dz1' a datetime object? ", isinstance(dz1, datetime))
print("What is the tzinfo for 'dz1?'  Is is 'aware?'", dz1.tzinfo)
print("Datetime object 'dz1': ", dz1)

print()
print(" 'd1' UTC: ", d1)
print("'dz1' MDT: ", dz1)

print()
print("TZ name and offset?")
print("'dz1': ", dz1.tzname(), dz1.utcoffset())
