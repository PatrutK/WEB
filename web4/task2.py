import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50,
                    choices=[i for i in range(100 + 1)], help='like barbies')
parser.add_argument('--cars', type=int, default=50,
                    choices=[i for i in range(100 + 1)], help='like cars')
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other',
                    help='what kind of movies prefer')

args = parser.parse_args()
if args.movie == 'melodrama':
    movie = 0
elif args.movie == 'football':
    movie = 100
else:
    movie = 50

boy = int((100 - args.barbie + args.cars + movie) / 3)
girl = int((100 - boy))

print(f'boy: {boy}\ngirl: {girl}')
