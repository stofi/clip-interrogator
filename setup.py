#!/usr/bin/env python

import subprocess

def setup():
    install_cmds = [
        ['pip', 'install', 'ftfy', 'regex', 'tqdm', 'transformers==4.21.2', 'timm', 'fairscale', 'requests'],
        ['pip', 'install', '-e', 'git+https://github.com/openai/CLIP.git@main#egg=clip'],
        ['pip', 'install', '-e', 'git+https://github.com/pharmapsychotic/BLIP.git@main#egg=blip'],
  
    ]
    for cmd in install_cmds:
        print(subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8'))

if __name__ == '__main__':
    setup()
