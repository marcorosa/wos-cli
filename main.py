import argparse


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Look for an author in the Web of Science.')
    parser.add_argument('author', help='Surname and name of the author')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose')
    parser.add_argument('-r', '--results', type=int, default=100,
                        help='Number of results to be shown')
    parser.add_argument('-y', '--years', type=int, default=5,
                        help='Max age of shown papers')
    parser.add_argument('-A', '--affiliation', help='Affiliation of the author')

    args = parser.parse_args()

    author = args.author
    years = args.years
    aff = args.affiliation
    results = args.results


if __name__ == '__main__':
    main()
