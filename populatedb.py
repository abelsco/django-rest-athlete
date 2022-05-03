"""_summary_

    Returns:
        _type_: _description_
    """
import time
import pandas
import psycopg2
from slugify import slugify
from django.utils.timezone import datetime

CONN_DB = 'postgres://postgres:postgres@db/postgres'

db = psycopg2.connect(CONN_DB)

dfAthlete = pandas.read_csv('dataset/athlete_events.csv')
dfNocs = pandas.read_csv('dataset/noc_regions.csv', keep_default_na=False)

files_formated = {
    'nocs': 'dataset/formated/nocs.csv',
    'athletes': 'dataset/formated/athletes.csv',
    'games': 'dataset/formated/games.csv',
    'events': 'dataset/formated/events.csv',
    'medals': 'dataset/formated/medals.csv',
}


def normalize_data_frame():
    """_summary_

    Returns:
        _type_: _description_
    """
    setup_timer = time.time()

    nocs = dfNocs.loc[:, ['NOC', 'region', 'notes']].drop_duplicates(subset=[
                                                                     'NOC'])
    nocs['created'] = datetime.now()
    nocs['updated'] = nocs['created']
    nocs.to_csv(files_formated['nocs'], index=False)

    athletes = dfAthlete.loc[:, ['ID', 'Name', 'Sex', 'Age', 'Height',
                                 'Weight', 'Team', 'NOC']].drop_duplicates(subset=['ID'])
    athletes['created'] = datetime.now()
    athletes['updated'] = athletes['created']
    athletes.to_csv(files_formated['athletes'], index=False)

    games = dfAthlete.loc[:, ['Year', 'Season', 'City',
                              'Games']].drop_duplicates(subset=['Games'])
    games['Slug'] = games.Games.apply(slugify)
    games['created'] = datetime.now()
    games['updated'] = games['created']
    games.to_csv(files_formated['games'], index=False)

    events = dfAthlete.loc[:, ['Event', 'Sport']].drop_duplicates(subset=[
                                                                  'Event'])
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

    return f"Time for Setup: {time.time() - setup_timer}"


def create_noc():
    """_summary_

    Returns:
        _type_: _description_
    """
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE noc_noc RESTART IDENTITY CASCADE')
    sql = f'''
    COPY noc_noc (name, region, notes, created, updated)
    FROM '/{files_formated['nocs']}'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return f"Time for Copy Nations: {time.time() - setup_timer}"


def create_athlete():
    """_summary_

    Returns:
        _type_: _description_
    """
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE athlete_athlete RESTART IDENTITY CASCADE')
    sql = f'''
    COPY athlete_athlete (id, name, sex, age, height, weight, team, noc_id, created, updated)
    FROM '/{files_formated['athletes']}'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return f"Time for Copy Athlete: {time.time() - setup_timer}"


def create_games():
    """_summary_

    Returns:
        _type_: _description_
    """
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE games_games RESTART IDENTITY CASCADE')
    sql = f'''
    COPY games_games (year, season, city, name, slug, created, updated)
    FROM '/{files_formated['games']}'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return f"Time for Copy Games: {time.time() - setup_timer}"


def create_events():
    """_summary_

    Returns:
        _type_: _description_
    """
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE event_event RESTART IDENTITY CASCADE')
    sql = f'''
    COPY event_event (name, sport, slug, created, updated)
    FROM '/{files_formated['events']}'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return f"Time for Copy Events: {time.time() - setup_timer}"


def create_medals():
    """_summary_

    Returns:
        _type_: _description_
    """
    setup_timer = time.time()
    cursor = db.cursor()
    cursor.execute('TRUNCATE TABLE medal_medal RESTART IDENTITY CASCADE')
    sql = f'''
    COPY medal_medal (medal, athlete_id, event_id, games_id, created, updated)
    FROM '/{files_formated['medals']}'
    DELIMITER ',' CSV header;
    '''
    cursor.execute(sql)
    db.commit()
    cursor.close()

    return f"Time for Copy Medals: {time.time() - setup_timer}"


def sync_athlete_next_val_sequence():
    """_summary_
    """
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
    print(normalize_data_frame())
    print(create_noc())
    print(create_games())
    print(create_athlete())
    print(create_events())
    print(create_medals())
    sync_athlete_next_val_sequence()
    print(f"Total time: {time.time() - setup_timer}")


if __name__ == "__main__":
    __main__()


# for row in games.values:
#     print(row[0:4])
