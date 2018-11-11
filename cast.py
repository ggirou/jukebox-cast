#!/usr/bin/python3

import config

import time
import pychromecast
from pychromecast.controllers.youtube import YouTubeController
import click

chromecasts = pychromecast.get_chromecasts()
print(chromecasts)
print([cc.device.friendly_name for cc in chromecasts])

cast = next(cc for cc in chromecasts if cc.device.friendly_name == config.chromecast_name)
# Wait for cast device to be ready
cast.wait()
print(cast.device)

print(cast.status)

yt = YouTubeController()
cast.register_handler(yt)

while True:
  print('Ready')
  key = click.getchar().lower()
  if key in config.videos:
    print("Playing " + config.videos[key])
    yt.play_video(config.videos[key])
