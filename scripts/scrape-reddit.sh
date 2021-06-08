DIR=/home/alex/GitHub/brain
REGEX='(http://|https://)?(www.)?reddit.com/r/.*?/.*?/'

# I know this is so gross but I couldn't figure out how else to do this :'(
GREP=$(egrep -r $REGEX $DIR --include \*.md -o | sed 's/^[^:]*:/:/' | sed 's/).*//' | cut -c 2-)

for i in $GREP; do
    echo "$i"
    python3 -m bdfr clone /media/alex/Media/Backup/brain/reddit/ -l "$i"
done
