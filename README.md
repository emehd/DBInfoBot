# DBInfoBot
DB Traininfo Poshover Bot

The application sends information about specified trains to the user via Pushover notification.

The trains are defined by their departure times using the evaNo (https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV).

Installation

pip install requirements.txt
Create a .env file with the following content:
DBCLIENTID=XXXXXXXXXX
DBAPIKEY=XXXXXXXXXXX
PUSHOVERTOKEN=XXXXXXXXX
PUSHOVERUSER=XXXXXXXXXXX
EVANO=XXXXXX

Define the trains in main.py:
-trains=[(hours,minutes), ...]

Run main.py.
Procedure

Query all information from the destination train station.
Search the information for the specified trains.
Send the information to the specified recipients.
