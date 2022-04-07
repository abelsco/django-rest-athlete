import time
import pandas
import psycopg2
from slugify import slugify
from django.utils.timezone import datetime

conn_db = 'postgres://postgres:postgres@db/postgres'

db = psycopg2.connect(conn_db)

dfAthlete = pandas.read_csv('dataset/athlete_events.csv')
dfNocs = pandas.read_csv('dataset/noc_regions.csv', keep_default_na=False)

files_formated = {
    'nocs': 'dataset/formated/nocs.csv',
    'athletes': 'dataset/formated/athletes.csv',
    'games': 'dataset/formated/games.csv',
    'events': 'dataset/formated/events.csv',
    'medals': 'dataset/formated/medals.csv',
}
    
    

def normalizeDataFrame():
    setup_timer = time.time()

    nocs = dfNocs.loc[:, ['NOC', 'region', 'notes']].drop_duplicates(subset=['NOC'])
    nocs['created'] = datetime.now()
    nocs['updated'] = nocs['created']
    nocs.to_csv(files_formated['nocs'], index=False)

    athletes = dfAthlete.loc[:, ['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC']].drop_duplicates(subset=['ID'])
    athletes['created'] = datetime.now()
    athletes['updated'] = athletes['created']
    athletes.to_csv(files_formated['athletes'], index=False)
    
    games = dfAthlete.loc[:, ['Year', 'Season', 'City', 'Games']].drop_duplicates(subset=['Games'])
    games['Slug'] = games.Games.apply(slugify)
    games['created'] = datetime.now()
    games['updated'] = games['created']
    games.to_csv(files_formated['games'], index=False)
    
    events = dfAthlete.loc[:, ['Event', 'Sport']].drop_duplicates(subset=['Event'])
    events['Slug'] = events.Event.apply(slugify)
    events['created'] = datetime.now()
    events['updated'] = events['created']
    events.to_csv(files_formated['events'], index=False)
    
    medals = dfAthlete.loc[:, ['Medal', 'ID', 'Event', 'Games']]
    medals['Event'] = medals.Event.apply(slugify)
    medals['Games'] = medals.Games.apply(slugify)
    medals['created'] = datetime.now()
    medals['updated'] = medals['created']
    medals.to_csv(files_formated['medals'], index=False)
    
    # print(athletes)
    # print(games)
    # print(events)
    # print(medals)

    return "Time for Setup: {}".format(time.time() - setup_timer)

def createNoc():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE noc_noc RESTART IDENTITY CASCADE')
    sql = '''
    COPY noc_noc (name, region, notes, created, updated)
    FROM '{}'
    DELIMITER ',' CSV header;
    '''.format('/'+files_formated['nocs'])
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return "Time for Copy Nations: {}".format(time.time() - setup_timer)

def createAthlete():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE athlete_athlete RESTART IDENTITY CASCADE')
    sql = '''
    COPY athlete_athlete (id, name, sex, age, height, weight, team, noc_id, created, updated)
    FROM '{}'
    DELIMITER ',' CSV header;
    '''.format('/'+files_formated['athletes'])
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return "Time for Copy Athlete: {}".format(time.time() - setup_timer)

def createGames():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE games_games RESTART IDENTITY CASCADE')
    sql = '''
    COPY games_games (year, season, city, name, slug, created, updated)
    FROM '{}'
    DELIMITER ',' CSV header;
    '''.format('/'+files_formated['games'])
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return "Time for Copy Games: {}".format(time.time() - setup_timer)

def createEvents():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE event_event RESTART IDENTITY CASCADE')
    sql = '''
    COPY event_event (name, sport, slug, created, updated)
    FROM '{}'
    DELIMITER ',' CSV header;
    '''.format('/'+files_formated['events'])
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return "Time for Copy Events: {}".format(time.time() - setup_timer)

def createMedals():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE medal_medal RESTART IDENTITY CASCADE')
    sql = '''
    COPY medal_medal (medal, athlete_id, event_id, games_id, created, updated)
    FROM '{}'
    DELIMITER ',' CSV header;
    '''.format('/'+files_formated['medals'])
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return "Time for Copy Medals: {}".format(time.time() - setup_timer)

def syncAthleteNextValSequence():
    sql = '''
    BEGIN;
    LOCK TABLE athlete_athlete IN EXCLUSIVE MODE;
    SELECT setval('athlete_athlete_id_seq', COALESCE((SELECT MAX(id)+1 FROM athlete_athlete), 1), false);
    '''
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()

def __main__():
    
    setup_timer = time.time()
    print(normalizeDataFrame())
    print(createNoc())
    print(createGames())
    print(createAthlete())
    print(createEvents())
    print(createMedals())
    syncAthleteNextValSequence()
    print("Total time: {}".format(time.time() - setup_timer))

if __name__ == "__main__":
    __main__()
    

# for row in games.values:
#     print(row[0:4])
