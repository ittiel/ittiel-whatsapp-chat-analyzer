import re
from datetime import datetime
from tabulate import tabulate


class ChatLine:
    """
    Class to represent the chat message object
    """
    def __init__(self, date, sender, content):
        self.date = date
        self.sender = sender
        self.content = content

    def __repr__(self):
        return "ChatLine()"

    def __str__(self):
        return "Date: {} \nSender: {} \nContent:{}".format(self.date, self.sender, self.content)


def parse_line(message):
    """
    Parse chat message to
    [0]: Date
    [1]: Sender name
    [3]: Content
    :param message: current chat message
    :return: ChatLine object
    # :return: list of Date, Sender, Content
    """
    try:
        splitted_line = message.split(' - ', 1)
        date = splitted_line[0]
        msg = splitted_line[1].split(": ", 1)
        sender = msg[0]
        content = msg[1]
    except Exception as e:
        # print(("Failed to parse chat line: '{}'").format(str))
        return -1
    return ChatLine(date, sender, content)
    # return [date, sender, content]


def count_senders(senders, parsed_line):
    """
    count the amount of messages sent by sender
    :param senders: dictionary of senders {Senders: Amount of sent messages}
    :param parsed_line: Parsed line object of Date, Sender, Content
    :return: senders dict
    """
    curr = senders.get(parsed_line.sender)
    if not curr:
        curr = 0
    senders.update({parsed_line.sender: curr + 1})
    return senders


def count_words(words_per_sender, parsed_line):
    """
    MS3: Features #1 and #2 — count the total number of messages and total number of words
    Count the number of messages you and your friend have exchanged.
    Then, count each of your individual share — both according to the number of messages and the number of words.

    Count number of words in a chat message
    :param words_per_sender: dictionary {Sender: Amount of words}
    :param parsed_line: Parsed line object of Date, Sender, Content
    :return: words_per_sender dict
    """
    curr = words_per_sender.get(parsed_line.sender)
    if not curr:
        curr = 0
    words = len(parsed_line.content.split())
    words_per_sender.update({parsed_line.sender: curr + words})
    return words_per_sender


def get_avg_length_of_message(avg_words_per_message, senders, words_per_sender):
    """
    MS4: Feature #3 — calculate the average length of messages sent by each party
    :param avg_words_per_message: dictionary of senders {Senders: Average amount of words per message}
    :param senders: dictionary of senders {Senders: Amount of sent messages}
    :param words_per_sender: dictionary {Sender: Amount of words}
    :return: avg_words_per_message dictionary
    """
    for sender in senders:
        number_of_chats = senders.get(sender)
        number_of_words = words_per_sender.get(sender)
        avg_words_per_message.update({sender: number_of_words/number_of_chats})
    return avg_words_per_message


def is_valid_line(line):
    """
    Validate that the chat message is valid ( Date - Sender: Content)
    As chat message can spread over multiple lines, we validate that the readline() from file
    contains the whole chat message
    :param line: Current chat line to validate
    :return: True if line is valid
    """
    pattern_date_time = '[0-9]{2}/[0-9]{2}/[0-9]{4}, [0-9]{2}:[0-9]{2} - '
    # pattern_date_time = "([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}) .+"
    return re.match(pattern_date_time, line)


def get_first_chat_of_the_day(current_chat_line, start_chat):
    """
    MS5: Feature #4 — count number of first texts
    :param current_chat_line: Parsed line object of Date, Sender, Content
    :param start_chat: dictionary containing the first chat of each day
    Date (dd/mm/yyyy): [Sender, [current_chat_line]]
    :return: start_chat dictionary
    """
    full_date = current_chat_line.date
    full_date_time = datetime.strptime(full_date, "%d/%m/%Y, %H:%M")

    date = current_chat_line.date.split(", ")[0]

    existing = start_chat.get(date)
    if existing:
        existing_rec = existing[1].date
        existing_time = datetime.strptime(existing_rec, "%d/%m/%Y, %H:%M")
        if full_date_time < existing_time:
            start_chat.update({date: [current_chat_line.date, current_chat_line]})
    else:
        start_chat.update({date: [current_chat_line.date, current_chat_line]})
    return start_chat


def get_chatting_time_patterns(parsed_line, hour_of_day_stats, day_of_week_stats, monthly_stats):
    """
    MS6: Feature #5 — chatting time patterns (hourly, daily, and monthly)
    Now, its time to find out your usual chatting patterns.
    * What hour of the day do you chat the most? What about the rest of the hours?
    * Which day of the week do you usually chat the most? What about the rest of the days?
    * Which month have you chatted the most? What about the rest?
    :param parsed_line:  Parsed line object of Date, Sender, Content
    :param hour_of_day_stats: Dictionary of hours stats {hour: amount of chats}
    :param day_of_week_stats: Dictionary of days of week stats {day of week: amount of chats}
    :param monthly_stats: Dictionary of monthly stats {month: amount of chats}
    :return:
    """
    full_date = parsed_line.date
    date = datetime.strptime(full_date, "%d/%m/%Y, %H:%M")
    hour = date.hour
    day = date.weekday()
    month = date.month
    hour_of_day_stats.update({hour: hour_of_day_stats.get(hour, 0) + 1})
    day_of_week_stats.update({day: day_of_week_stats.get(day, 0) + 1})
    monthly_stats.update({month: monthly_stats.get(month, 0) + 1})
    return hour_of_day_stats, day_of_week_stats, monthly_stats


def get_words_stats(parsed_line, words_stats):
    """
    MS8: Feature #8 — most common words
    :param parsed_line: Parsed line object of Date, Sender, Content
    :param words_stats: Dictionary of words stats {word: appearance amount}
    :return: words_stats dict
    """
    words = parsed_line.content.split(" ")
    for word in words:
        words_stats.update({word: words_stats.get(word, 0) + 1})
    return words_stats


def pretty_print(senders, words_per_sender, avg_words_per_message, hour_of_day_stats, day_of_week_stats, monthly_stats,
                 words_stats):
    """
    Prints the data to tables using tabulate
    :param senders
    :param words_per_sender
    :param avg_words_per_message
    :param hour_of_day_stats:
    :param day_of_week_stats:
    :param monthly_stats:
    :param words_stats:
    """
    print(tabulate(sorted(senders.items()), headers=["Name", "Amount of chats"]))
    print("\n")
    print(tabulate(sorted(words_per_sender.items()  ), headers=["Name", "Total Words"]))
    print("\n")
    print(tabulate(sorted(avg_words_per_message.items()), headers=["Name", "Average words per message"]))
    print("\n")
    print(tabulate(sorted(hour_of_day_stats.items()), headers=["Hour", "Amount of chats"]))
    print("\n")
    print(tabulate(sorted(day_of_week_stats.items()), headers=["Days of week", "Amount of chats"]))
    print("\n")
    print(tabulate(sorted(monthly_stats.items()), headers=["Month", "Amount of chats"]))
    print("\n")
    print(tabulate(sorted(words_stats.items()), headers=["Word", "Amount"]))


def main():
    # todo: optimize the data structures or use database
    senders = {}
    words_per_sender = {}
    avg_words_per_message = {}
    start_chat = {}
    hour_of_day_stats = {}
    day_of_week_stats = {}
    monthly_stats = {}
    words_stats = {}
    # todo: automate chat export (requires WhatsApp authentication)
    # todo: get the chat file from env variable? input?
    filename = "../chat.txt"
    tmp = ""
    # MS2: Read your chat file using your Python program
    # read file backwards to find multi lines messages
    for line in reversed(list(open(filename))):
        line = line.rstrip('\n')
        if tmp != "":
            line += tmp
        if not is_valid_line(line):
            tmp = line
        else:
            tmp = ""
            parsed_line = parse_line(line)
            # print(("{}:{}").format(line_num,  parsed_line))
            senders = count_senders(senders, parsed_line)
            words_per_sender = count_words(words_per_sender, parsed_line)
            avg_words_per_message = get_avg_length_of_message(avg_words_per_message, senders, words_per_sender)
            start_chat = get_first_chat_of_the_day(parsed_line, start_chat)
            hour_of_day_stats, day_of_week_stats, monthly_stats = get_chatting_time_patterns(
                parsed_line, hour_of_day_stats, day_of_week_stats, monthly_stats)
            words_stats = get_words_stats(parsed_line, words_stats)
    pretty_print(senders, words_per_sender, avg_words_per_message, hour_of_day_stats, day_of_week_stats,
                 monthly_stats, words_stats)


if __name__ == "__main__":
    main()
