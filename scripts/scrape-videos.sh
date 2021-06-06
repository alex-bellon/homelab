DIR=/home/alex/GitHub/brain
REGEX='https://www.youtube.com/watch.*|https://youtu.be.*'

# I know this is so gross but I couldn't figure out how else to do this :'(
GREP=$(egrep -r $REGEX $DIR --include \*.md -o | sed 's/^[^:]*:/:/' | sed 's/).*//' | cut -c 2-)

for i in $GREP; do
    youtube-dl -o '~/Videos/brain/%(title)s' "$i"
done
