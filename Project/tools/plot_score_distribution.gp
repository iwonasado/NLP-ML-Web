#script to plot the distribution of scores against the counts for that score.

# try to fit f1 function
f1(x) = a/(b+x**2) + c
a = 10000
b = 10
c = -1
fit [1:1000] f1(x) "../results/data exploration/score-distribution.dat" via a,b,c
set boxwidth 0.5
set style fill solid
set xlabel "Scores"
set ylabel "# of instances"
plot "../results/data exploration/score-distribution.dat" with boxes, f1(x)