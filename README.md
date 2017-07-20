# wos-cli
Simple command line interface for querying wos

## Installation
Download the repository
```bash
git clone https://github.com/marcorosa/CC-Botnet-in-Python
cd CC-Botnet-in-Python
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
There is also the possibility to specify the timespan and the number of pubblications:
* `-y YEARS` (default 5)
* `-r RESULTS` (default 100)
* `-A AFFILIATION` (see note below)
```bash
python start.py "Surname Name" -y 10 -r 25
```

## Nota Bene (from `webofknowledge.com`)
- AFFILIATION:
  When entering full names, do not use articles (a, an, the) and prepositions
  (of, in, for) in the name. For example, entering UNIV Pennsyvania is OK but
  entering University of Pennsylvania results in an error message.
- AUTHOR:
  Enter the last name first followed by a space and the author's name (or
  initials).
