import re

record = "08/02/2019, 11:22 - Sender : text text"
# record = '1518-09-06 00:57 some-alphanumeric-charecter'
pattern_date_time = '[0-9]{2}/[0-9]{2}/[0-9]{4}, [0-9]{2}:[0-9]{2} - '
# pattern_date_time = "([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}) .+"
match = re.match(pattern_date_time, record)
if match is not None:
    print(match.end())
    group = match.group()
    print(group[0])
    print(record.split(group))
    print()
