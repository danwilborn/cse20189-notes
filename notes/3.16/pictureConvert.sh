for image in $(ls /usr/share/pixmaps/*.png); do
	convert $image -resize 25% thumbnail- $(basename $image)
done
