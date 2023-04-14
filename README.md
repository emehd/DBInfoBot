# DBInfoBot
DB Traininfo Pushover Bot

The application sends information about specified trains to the user via Pushover notification.

The trains are defined by their departure times using the evaNo (https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV).

_Installation_

1. pip install requirements.txt
2. Create a .env file with the following content:
- DBCLIENTID=XXXXXXXXXX
- DBAPIKEY=XXXXXXXXXXX
- PUSHOVERTOKEN=XXXXXXXXX
- PUSHOVERUSER=XXXXXXXXXXX
- EVANO=XXXXXX

3. Define the trains in main.py:
- trains=[(hours,minutes), ...]

4. Run main.py.

_Procedure_

Query all information from the destination train station.
Search the information for the specified trains.
Send the information to the specified recipients.
