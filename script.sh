for opti in 0 1 2 3; do
    for type in int float short double char; do
        for n in 100 500 1000; do
            gcc -O"$opti" -DN="$n" -DTYPE="$type" tp1.c -o main
            ./main >> "result_${type}_N${n}_O${opti}.txt"
        done
    done
done
