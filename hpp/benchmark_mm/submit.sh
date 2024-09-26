# the number of python processes to start, P=3 if not set
P=${1:-3}
# the size of the matrix, use the default in overcommit.py if not set
for i in $(seq $P); do 
    echo -n "Starting process ${i}… "
    python bench.py $i
done
