# wos-cli
Simple command line interface for querying wos

## Installation
Download the repository
```bash
git clone https://github.com/marcorosa/wos-cli
cd wos-cli
```
Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration
Edit file `src/config.py` adding your username and password for Web of Science

## Usage
Launch the main file
```bash
python start.py "Surname Name"
```
There is also the possibility to specify the query:
* `-y YEARS` (default 5): time interval to take into consideration
* `-r RESULTS` (default 100): max number of records to show
* `-A AFFILIATION` (see note below): affiliation of the author
* `--save`: save results in a database
```bash
python start.py "Surname Name" -y 10 -r 25
```

## Example
```bash
$ python main.py 'knuth donald' -y 10 -A stanford
Authenticated (SID: xxxxxxxxx)
Found 2 papers
+-------+---------------------------------------------------------+----------------------+
| Year  |                          Title                          |        ID WOS        |
+=======+=========================================================+======================+
| 2016  | A Twisted Enumeration of the Positive Integers          | WOS:000370069600012  |
+-------+---------------------------------------------------------+----------------------+
| 2011  | Mathematical Vanity Plates                              | WOS:000287850200007  |
+-------+---------------------------------------------------------+----------------------+
```

## Nota Bene (from `webofknowledge.com`)
- AFFILIATION:
  When entering full names, do not use articles (a, an, the) and prepositions
  (of, in, for) in the name. For example, entering UNIV Pennsyvania is OK but
  entering University of Pennsylvania results in an error message.
- AUTHOR:
  Enter the last name first followed by a space and the author's name (or
  initials).
