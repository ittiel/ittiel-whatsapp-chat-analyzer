from datetime import datetime

records = ["08/02/2019, 11:22 - Sender : text 1",  "08/03/2019, 11:22 - Sender : text 2",
           "08/02/2019, 11:23 - Sender : text 3", "08/02/2019, 11:21 - Sender : text 4"]

start_chat = {}
for rec in records:
    full_date = rec.split(" - ")[0]
    date = rec.split(", ")[0]
    print(date)
    full_date_time = datetime.strptime(full_date, "%d/%m/%Y, %H:%M")
    date_time = datetime.strptime(date, "%d/%m/%Y")
    print(date_time.month)
    print(date_time.day)
    print(date_time.hour)
    print(date_time.minute)
    existing = start_chat.get(date)
    if existing:
        existing_rec = existing[0].split(" - ")[0]
        existing_time = datetime.strptime(existing_rec, "%d/%m/%Y, %H:%M")
        if full_date_time < existing_time:
            start_chat.update({date :[rec, rec]})
    else:
        start_chat.update({date: [rec, rec]})
    # hour_time =
    print(start_chat)

