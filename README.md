# Listings App (looking for a new name!)
Simple Django app that displays a list of curated cafes/spaces to meetup and work in London

# Content

1. [Description](#description)
4. [Setup](#setup)
5. [Contributing](#contributing)


# Description

## Tech
- Backend: Python & Django
- Front-end: SASS/HTML5/JavaScript
- Hosting: Heroku
- Storage: AWS S3 

## Team
- [Lili](https://github.com/lili2311)

- [Dan](https://github.com/snowkuma)

# Setup
## Tools
1. **Terminal**: [iTerm2](https://www.iterm2.com/) (MacOSX), [Terminator](http://gnometerminator.blogspot.co.uk/p/introduction.html) (Linux) or use your preferred one.
2. **Text Editor**: [Sublime Text](http://www.sublimetext.com/) or you preferred one.

## Dev Enviroment Setup
1. [Setup](https://github.com/PolyglotDevsLondon/setup/wiki)
2. Clone the repo: `git@github.com:PolyglotDevsLondon/listings-app.git`
3. Create a new virtual environment with virtualenvwrapper: `mkvirtualenv -a listings-app listings-app`
4. `cd` into the `listings-app` folder
5. Install all the dependencies: `pip install -r requirements.txt`
6. Apply the initial database migrations: `python manage.py migrate`

## Running the project locally
0. If not already active, activate the virtual environment: `workon listings-app`
1. Run `python manage.py runserver`
2. Open your browser at http://localhost:8000/


## Front End changes
_todo_

# Contributing
Please follow the [Contributing Guidelines](CONTRIBUTING.md)


