for opti in 2; do
    for type in float; do
        for n in 3000; do
            gcc -O"$opti" -DN="$n" -DTYPE="$type" tp1.c -o main
            ./main >> ./results_2/"result_${type}_N${n}_O${opti}.txt"
        done
    done
done
