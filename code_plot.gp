set term png size 1900,1000 enhanced font "Terminal,10"
set grid
set auto x
set key left top
set multiplot layout 2, 2 rowsfirst
set key out
set pointsize 0.5
set yrange[0:5]
set title "strategie en fonction de la variation avec l'algorithme ucb"
set ylabel "strategie"
set xlabel "packet"
set datafile separator ";"
plot "strat.dat" u 2:xtic(1) with linespoints




