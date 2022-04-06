import time
import pandas
import psycopg2
from slugify import slugify

conn_db = 'postgres://postgres:postgres@db/postgres'

db = psycopg2.connect(conn_db)

dfAthlete = pandas.read_csv('dataset/athlete_events.csv')

def normalizeDataFrame():
    setup_timer = time.time()

    athletes = dfAthlete.loc[:, ['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC']].drop_duplicates(subset=['ID'])
    athletes.to_csv('dataset/athletes.csv', index=False)
    
    games = dfAthlete.loc[:, ['Year', 'Season', 'City', 'Games']].drop_duplicates(subset=['Games'])
    games['Slug'] = games.Games.apply(slugify)
    games.to_csv('dataset/games.csv', index=False)
    
    events = dfAthlete.loc[:, ['Event', 'Sport']].drop_duplicates(subset=['Event'])
    events['Slug'] = events.Event.apply(slugify)
    events.to_csv('dataset/events.csv', index=False)
    
    medals = dfAthlete.loc[:, ['Medal', 'ID', 'Event', 'Games']]
    medals['Event'] = medals.Event.apply(slugify)
    medals['Games'] = medals.Games.apply(slugify)
    medals.to_csv('dataset/medals.csv', index=False)
    
    # print(athletes)
    # print(games)
    # print(events)
    # print(medals)

    return print("Time for Setup: {}".format(time.time() - setup_timer))

def createNoc():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE noc_noc RESTART IDENTITY CASCADE')
    sql = '''
    COPY noc_noc (name, region, notes)
    FROM '/dataset/noc_regions.csv'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()    

    return print("Time for Copy Nations: {}".format(time.time() - setup_timer))

def createAthlete():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE athlete_athlete RESTART IDENTITY CASCADE')
    sql = '''
    COPY athlete_athlete (id, name, sex, age, height, weight, team, noc_id)
    FROM '/dataset/athletes.csv'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return print("Time for Copy Athlete: {}".format(time.time() - setup_timer))

def createGames():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE games_games RESTART IDENTITY CASCADE')
    sql = '''
    COPY games_games (year, season, city, name, slug)
    FROM '/dataset/games.csv'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return print("Time for Copy Games: {}".format(time.time() - setup_timer))

def createEvents():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE event_event RESTART IDENTITY CASCADE')
    sql = '''
    COPY event_event (name, sport, slug)
    FROM '/dataset/events.csv'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return print("Time for Copy Events: {}".format(time.time() - setup_timer))

def createMedals():
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE medal_medal RESTART IDENTITY CASCADE')
    sql = '''
    COPY medal_medal (medal, athlete_id, event_id, games_id)
    FROM '/dataset/medals.csv'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return print("Time for Copy Medals: {}".format(time.time() - setup_timer))

def __main__():
    print(normalizeDataFrame())
    print(createNoc())
    print(createGames())
    print(createAthlete())
    print(createEvents())
    print(createMedals())

__main__()
    

# for row in games.values:
#     print(row[0:4])
