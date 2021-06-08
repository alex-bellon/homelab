DIR=/home/alex/GitHub/brain

# Video 

REGEX='https://www.youtube.com/watch.*|https://youtu.be.*'

# I know this is so gross but I couldn't figure out how else to do this :'(
GREP=$(egrep -r $REGEX $DIR --include \*.md -o | sed 's/^[^:]*:/:/' | sed 's/).*//' | cut -c 2-)

for i in $GREP; do
    youtube-dl -o '/media/alex/Media/Backup/brain/youtube/%(title)s' "$i"
done

# Reddit

REGEX='(http://|https://)?(www.)?reddit.com/r/.*?/.*?/'

GREP=$(egrep -r $REGEX $DIR --include \*.md -o | sed 's/^[^:]*:/:/' | sed 's/).*//' | cut -c 2-)

for i in $GREP; do
    python3 -m bdfr clone /media/alex/Media/Backup/brain/reddit/ -l "$i"
done
