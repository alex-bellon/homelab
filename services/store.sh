#! /bin/bash

for f in *.service; do
  echo $f
  sudo ln "$f" /lib/systemd/system
done
