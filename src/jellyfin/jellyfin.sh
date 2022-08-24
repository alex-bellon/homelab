#! /bin/bash

docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media/alex/Media:/media --net=host jellyfin/jellyfin:latest
