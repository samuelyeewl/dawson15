This is the Eh set of 500 simulations from Dawson et al 2015 (correlations of giant impacts...)

Have to recompile element6.for to set up linker paths etc correctly.
Moved all files needed to compile into data/ (mercury.inc swift.inc)
Compile with

gfortran element6.for -std=legacy -o element6

then copy that binary into each sim folder to run

Sam Y wrote a 

./gen_sims.sh sim3

which goes into the arg folder and saves a rebound simulation of final state  into rebsims folder. The  python file it calls needs to run with Python 2.

Run

./runall.sh

to iterate through all the folders and save REBOUND sims
