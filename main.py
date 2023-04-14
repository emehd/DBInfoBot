import time
from dotenv import load_dotenv
import CheckTrain
import DB_Timetable_API
import Pushover_API

load_dotenv()


def mainDB():
    DB_Timetable_API.DB_delay()
    trains = [(7, 6), (17, 6)]
    for i in range(len(trains)):
        message = CheckTrain.check_train_info(departure_hour=trains[i][0], departure_minute=trains[i][1])
        if message != "0":
            Pushover_API.send_infos(message)


if __name__ == '__main__':
    mainDB()
    time.sleep(30)
