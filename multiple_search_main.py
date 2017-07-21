import argparse

from src import multi_search


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Look for authors in Web of Science.')
    parser.add_argument('infile', help='Input file (.csv)')
    parser.add_argument('outfile', help='Output file (db)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose')
    parser.add_argument('-r', '--results', type=int, default=100,
                        help='Number of results to be shown')
    parser.add_argument('-y', '--years', type=int, default=5,
                        help='Max age of shown papers')

    args = parser.parse_args()

    # Search the author
    multi_search.multiple_search(args.infile, args.outfile,
                                 args.years, args.results)


if __name__ == '__main__':
    main()
