set terminal png

set yrange [0:100]

plot 'demo.txt' using 1:2 title "males" with lines, \
	 'demo.txt' using 1:3 title "females" with lines 
	 
