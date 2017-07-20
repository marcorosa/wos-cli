import argparse

from six import print_
from src import search, dbconn


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Look for an author in Web of Science.')
    parser.add_argument('author', help='Surname and name of the author')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose')
    parser.add_argument('-r', '--results', type=int, default=100,
                        help='Number of results to be shown')
    parser.add_argument('-y', '--years', type=int, default=5,
                        help='Max age of shown papers')
    parser.add_argument('-A', '--affiliation', help='Affiliation of the author')
    parser.add_argument('--save', action='store_true', help='save results in a db')

    args = parser.parse_args()

    # Search the author
    results = search.search(args.author, args.years, args.results, args.affiliation)
    if args.save:
        # Save in db
        print_('Save records in db')
        dbconn.save(args.author.lower(), results)
        print_('Completed!')


if __name__ == '__main__':
    main()
