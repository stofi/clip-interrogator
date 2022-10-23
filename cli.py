#!/usr/bin/env python

# Usage: python cli.py [-i URL]|[-f FILE] [options] [-o OUTPUT]
# Options:
#   -i      URL or path to image to interrogate
#   -f      File with a list of images to interrogate
#   -o      Output file to save prompts to, defaults to stdout
#   -h, --help            show this help message and exit


import clip_interrogator

import sys
import requests
import argparse
from PIL import Image

if not __name__ == '__main__':
    print("This is a command-line program. Please run it from the command line.")
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--image', help='URL or path to image to interrogate')
parser.add_argument(
    '-f', '--file', help='File with a list of images to interrogate')
parser.add_argument(
    '-o', '--output', help='Output file to save prompts to, defaults to stdout')


args = parser.parse_args()

# Print help if no arguments are given or if the hlp flag is given
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()


# exit if no file or image is provided
if not args.image and not args.file:
    print("Please provide an image or file")
    sys.exit()


def setupOutputFile():
    if args.output:
        try:
            output = open(args.output, 'w')
        except:
            print("Could not open output file")
            sys.exit()
    else:
        output = sys.stdout
    return output


def appendPromptToFile(prompt, output):
    # add \n to the end of the prompt
    if not prompt.endswith('\n'):
        prompt += '\n'
    output.write(prompt)


def interrogate(image_url, log=False):
    if log:
        print()
        print("Interrogating...")
    if str(image_url).startswith('http://') or str(image_url).startswith('https://'):
        image = Image.open(requests.get(
            image_url, stream=True).raw).convert('RGB')
    else:
        if log:
            print("Invalid URL")
        image = Image.open(image_url).convert('RGB')

    prompt = clip_interrogator.interrogate(image)
    if log:
        print()
        print("Prompt:")
    return prompt



output = setupOutputFile()
enable_log = args.output is None
# Interrogate a single image
if args.image:
    prompt = interrogate(args.image, enable_log)
    appendPromptToFile(prompt, output)
# Interrogate a list of images
elif args.file:
    try:
        with open(args.file) as f:
            lines = f.readlines()
    except:
        print("Could not open file")
        sys.exit()
    for image_url in lines:
        # remove whitespace characters like `\n` at the end of each line
        image_url = image_url.strip()
        # image_url could be file path or url
        prompt = interrogate(image_url)
        appendPromptToFile(prompt, output)
