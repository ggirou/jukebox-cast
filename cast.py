#!/usr/bin/python3

import config

import time
import pychromecast
from pychromecast.controllers.youtube import YouTubeController
import click

previous_key=''
while True:
  chromecasts = pychromecast.get_chromecasts()
  cast = next(cc for cc in chromecasts if cc.device.friendly_name == config.chromecast_name)
  cast.wait()
  yt = YouTubeController()
  cast.register_handler(yt)
  print('Ready')
  key = click.getchar().lower()
  if key in config.videos and previous_key != key:
    previous_key=key
    video_id=config.videos[key]
    print("Starting " + video_id)
    yt.play_video(video_id)
    print("Playing " + video_id)
    time.sleep(1)
