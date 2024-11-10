for opti in 2; do
    for type in float; do
        for n in 1000; do
            for blk in {1..128};do
                echo "BLK = ${blk}" 
                gcc -O"$opti" -DN="$n" -DTYPE="$type" -DBL="$blk" tp1.c -o main
                ./main >> ./results_blk/"result_${type}_N${n}_O${opti}_blk${blk}.txt"
            done
        done
    done
done
