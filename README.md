# clip-interrogator

This is a fork of https://github.com/pharmapsychotic/clip-interrogator that has been ported to python and can be run in the terminal. It has also been given the ability to process batches of images.

## Setup
  ```bash 
  python setup.py 
  ```

## Usage
  ### Run:
  
  ```bash 
    python cli.py -i https://i.ytimg.com/vi/0k1xU4Kp5Go/maxresdefault.jpg
  ```

  ### Options:
  - `-i` URL or path to image to interrogate
  - `-f` File with a list of images to interrogate
  - `-o` Output file to save prompts to, defaults to stdout
  - `-h, --help` show this help message and exit


