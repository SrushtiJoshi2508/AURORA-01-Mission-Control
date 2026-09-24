import datetime

event_log = []


def log_event(message):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    event = current_time + " - " + message
    event_log.append(event)


def get_event_log():
    return event_log


def clear_event_log():
    event_log.clear()