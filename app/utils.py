import csv
from .models import db, Player

def read_csv_to_db(path):
    with open(path, 'rU', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            player = Player(
                ID=row['ID'],
                playerID=row['playerID'],
                birthYear=row['birthYear'],
                birthMonth=row['birthMonth'],
                birthDay=row['birthDay'],
                birthCity=row['birthCity'],
                birthCountry=row['birthCountry'],
                birthState=row['birthState'],
                deathYear=row['deathYear'],
                deathMonth=row['deathMonth'],
                deathDay=row['deathDay'],
                deathCountry=row['deathCountry'],
                deathState=row['deathState'],
                deathCity=row['deathCity'],
                nameFirst=row['nameFirst'],
                nameLast=row['nameLast'],
                nameGiven=row['nameGiven'],
                weight=row['weight'],
                height=row['height'],
                bats=row['bats'],
                throws=row['throws'],
                debut=row['debut'],
                bbrefID=row['bbrefID'],
                finalGame=row['finalGame'],
                retroID=row['retroID']
            )
            db.session.add(player)
        db.session.commit()
