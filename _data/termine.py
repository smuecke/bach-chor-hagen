import requests
from argparse    import ArgumentParser
from collections import namedtuple
from datetime    import date, timedelta
from operator    import attrgetter

DATE_FMT = '%d.%m.%Y'

date_range = namedtuple('date_range', ['name', 'start', 'end'])


def erster_mittwoch_im_monat(d: date) -> bool:
    first = d.replace(day=1)
    first_wed = first + timedelta(days=(2-first.weekday())%7)
    return d == first_wed


def main():
    p = ArgumentParser()
    p.add_argument('--year', type=int, default=None)
    args = p.parse_args()
    year = args.year or date.today().year
    
    FERIEN_API = f'https://ferien-api.de/api/v1/holidays/NW/{year}'
    FEIERTAGE_API = f'https://get.api-feiertage.de?states=nw&years={year}'

    special_days = []

    # hole alle Ferienzeiten
    resp = requests.get(FERIEN_API)
    if resp.status_code == 200:
        for obj in resp.json():
            special_days.append(date_range(
                obj['name'].split()[0].title(),
                date.fromisoformat(obj['start']),
                date.fromisoformat(obj['end'])))

    # hole alle Feiertage
    resp = requests.get(FEIERTAGE_API)
    if resp.status_code == 200:
        for obj in resp.json()['feiertage']:
            date_ = date.fromisoformat(obj['date'])
            special_days.append(date_range(obj['fname'], date_, date_))

    # sortiere nach Start-Datum
    special_days.sort(key=attrgetter('start'))

    # erster Mittwoch im Jahr
    probe = date(year=year, month=1, day=1)
    probe += timedelta(days=(2-probe.weekday())%7)
    
    weihnachten = date(year=year, month=12, day=24)

    # erstelle yml-Einträge
    yml = []
    while probe < weihnachten:
        special = False
        yml.extend([
            f'- date: "{probe.strftime(DATE_FMT)}"',
             '  time: "19:30"',
             '  weekday: Mittwoch'
        ])
        
        pizza = '🍕 ' if erster_mittwoch_im_monat(probe) else ''
        for name, date_start, date_end in special_days:
            if date_start <= probe <= date_end:
                yml.append(f'  notes: "{pizza}{name}"')
                special = True
            elif date_start > probe:
                break
        if pizza and not special:
            yml.append(f'  notes: "{pizza}"')

        probe += timedelta(days=7)
    
    for line in yml:
        print(line)


if __name__ == '__main__':
    main()
