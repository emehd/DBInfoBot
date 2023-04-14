import json
from datetime import datetime


def check_train_info(departure_hour, departure_minute):
    with open("data.json", "r") as file:
        data = json.load(file)
    delay = 0
    train_info = ""
    try:
        for event in data["timetable"]["s"]:
            departure = event.get("dp")
            if departure:
                try:
                    for message in departure["m"]:
                        if message["@t"] == "d":
                            delay = message["@c"]
                except TypeError as e:
                    print(e)
                departure_timestamp = departure["@ct"]
                departure_time = datetime.strptime(departure_timestamp, "%y%m%d%H%M")

                if departure_time.hour == departure_hour and (departure_time.minute - int(delay)) == departure_minute:
                    delay_message = ""
                    track_change_message = ""
                    cancel_message = ""
                    try:
                        if "m" in departure:
                            for message in departure["m"]:
                                if message["@t"] == "d":
                                    delay_message = f"Der Zug hat eine Verspätung von {message['@c']} Minuten."
                                elif message["@t"] == "q":
                                    track_change_message = f"Der Zug fährt von Gleis {message['@c']} ab."
                                elif message["@t"] == "c":
                                    cancel_message = f"Der Zug Fällt aus"
                    except TypeError:
                        message = departure["m"]
                        if message["@t"] == "d":
                            delay_message = f"Der Zug hat eine Verspätung von {message['@c']} Minuten."
                        elif message["@t"] == "q":
                            track_change_message = f"Der Zug fährt von Gleis {message['@c']} ab."
                        elif message["@t"] == "c":
                            cancel_message = f"Der Zug Fällt aus"

                    train_info = f"Infos für den Zug um 07:06 Uhr: {delay_message} {track_change_message} {cancel_message}".strip()
                    break
    except Exception as e:
        print(e)
    return train_info
