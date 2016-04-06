set terminal png

set xrange [2012:2016]
set yrange [0:100]
set grid
set style data histogram
set style fill solid border
set boxwidth 0.95 relative

plot 'demo.txt' using 1:2 title "males" with boxes
