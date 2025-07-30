# Maykin Back-end Case
An implementation of the back-end case for a job application at Maykin.

## Development setup
Create a virtual environment for Python (Python 3.12 was used for development,
older versions might work as well) and install the requirements listed in
`requirements.txt`. Then run `python manage.py migrate` from the `src` folder.

## Usage
To import hotel data, run `python manage.py updatehotels`
from the `src` folder. To run the development server, run
`python manage.py runserver` from the `src` folder.

## Documentation
Documentation can be found in the `docs` folder. Starting at the
[overview](docs/overview.md) is strongly suggested.
