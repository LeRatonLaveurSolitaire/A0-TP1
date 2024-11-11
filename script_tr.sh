for opti in 2; do
    for type in float int; do
        for n in 1000; do
            echo "Type = ${type}" 
            gcc -O"$opti" -DN="$n" -DTYPE="$type" tp1.c -o main
            taskset -c 1 ./main >> ./results_tr/"result_${type}_N${n}_O${opti}.txt"
        done
    done
done
