## Description
Having a bunch of fotos all in a same directory? Do you want to organize them according to date (year and month). Then this repository is for you. Here you can find a script to organize fotos in year and month directories.

## Motivation
Need to organize thounds of fotos

## Dependencies

## Usage

Clone the rerpository 
```bash
    git clone https://github.com/yahuarlocro/fotorganizer.git
```

If not already installed, please install pipenv
```bash
    pip install pipenv
```

Install the dependencies
```bash
    pipenv install
```

Place all your pictures in the fotos directory and create a .env file (see .env_example)
```bash
    FOTOS_DIRECTORY=path/to/the/directory
    HOME_DIRECTORY=path/to/the/directory
    OUTPUT_DIRECTORY=path/to/the/directory
```

Execute the python script
```bash
    pipenv run python3 fotorganizer.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Maintainer
yahuarlocro -> https://github.com/yahuarlocro

## License
Use at your own risk