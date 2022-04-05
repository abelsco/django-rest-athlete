import pandas
import psycopg2


conn_db = 'postgres://postgres:postgres@0.0.0.0/postgres'

db = psycopg2.connect(conn_db)

dfAthlete = pandas.read_csv('dataset/athlete_events.csv')

def createNoc():
    nocs = pandas.read_csv('dataset/noc_regions.csv')
    print(nocs)
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE noc_noc')
    sql = '''
    COPY noc_noc
    FROM '/dataset/noc_regions.csv'
    DELIMITER ',' CSV;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()    

    return

def createAthlete():
    athletes = dfAthlete.loc[:, ['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC']].drop_duplicates(subset=['ID'])
    print(athletes)
    athletes.to_csv('dataset/formated/athletes.csv')
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE athlete_athlete')
    sql = '''
    COPY athlete_athlete
    FROM '/dataset/formated/athletes.csv'
    DELIMITER ',' CSV;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return

def createGames():
    games = dfAthlete.loc[:, ['Games', 'Year', 'City']].drop_duplicates(subset=['Games'])
    games.to_csv('dataset/formated/games.csv')
    print(games)
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE games_games')
    sql = '''
    COPY games_games
    FROM '/dataset/formated/games.csv'
    DELIMITER ',' CSV;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return

def createEvents():
    events = dfAthlete.loc[:, ['Event', 'Sport', 'Games']].drop_duplicates(subset=['Event'])
    print(events)
    events.to_csv('dataset/formated/events.csv')
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE event_event')
    sql = '''
    COPY event_event
    FROM '/dataset/formated/event.csv'
    DELIMITER ',' CSV;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return

def createMedals():
    medals = dfAthlete.loc[:, ['Event', 'ID', 'Medal']]
    print(medals)
    medals.to_csv('dataset/formated/medals.csv')
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE medal_medal')
    sql = '''
    COPY medal_medal
    FROM '/dataset/formated/medal.csv'
    DELIMITER ',' CSV;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return

# for row in games.values:
#     print(row[0:4])
