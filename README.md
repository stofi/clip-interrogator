# clip-interrogator

fork of https://github.com/pharmapsychotic/clip-interrogator
ported to python to run in the terminal
added batch processing feature

## Setup
  Setup:
  ```bash 
  python setup.py 
  ```

## Usage
  Run:
  
  ```bash 
    python cli.py -i https://i.ytimg.com/vi/0k1xU4Kp5Go/maxresdefault.jpg
  ```

  Options:
  `-i` URL or path to image to interrogate
  `-f` File with a list of images to interrogate
  `-o` Output file to save prompts to, defaults to stdout
  `-h, --help` show this help message and exit


