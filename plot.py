import matplotlib.pyplot as plt
import numpy as np


def main() -> None:

    CPU_freq = 2.5 * 1e9        # 2.50 GHz0
    L1_cache_size = 64 * 1e3    # 64 KiB    
    L2_cache_size = 512 * 1e3   # 512 KiB    
    L3_cache_size = 3 * 1e6     # 3 MiB

    # Processing of data generated during script 1

    result_1_type = ["char",  "short", "int", "double", "float"]
    result_1_N = ["100", "500", "1000"]
    result_1_opti = ["0", "1", "2", "3"]
    result_1_function = ["ZERO", "COPY_ij", "COPY_ji", "ADD_ij", "ADD_ji", "PS", "MM_ijk", "MM_ikj", "MM_B_ijk"]

    result1_values_mean = np.zeros((len(result_1_type),len(result_1_N),len(result_1_opti),len(result_1_function)))

    # store the mean values of each function in the result_values_mean table

    for i,data_type in enumerate(result_1_type):
        for j,N in enumerate(result_1_N):
            for k,opti in enumerate(result_1_opti):
                with open(f"./results_1/result_{data_type}_N{N}_O{opti}.txt") as file:
                    lines = file.readlines()
                    for line_number in range(1,19,2):
                        line = lines[line_number]
                        values = line.split('\t')[1:]
                        for l,val in enumerate(values):
                            values[l] = float(val)
                        result1_values_mean[i,j,k,(line_number-1)//2] = sum(values)/len(values)


    # Processing of data generated during script 2

    result_2_N = ["100", "500", "1000"]
    result_2_function = ["MM_ijk", "MM_ikj", "MM_B_ijk"]

    result2_values_mean = np.zeros((len(result_2_N),len(result_2_function)))

    # store the mean values of each function in the result_values_mean table


    for i,N in enumerate(result_1_N):
        with open(f"./results_2/result_float_N{N}_O2.txt") as file:
            lines = file.readlines()
            for line_number in range(1,7,2):
                line = lines[line_number]
                values = line.split('\t')[1:]
                for l,val in enumerate(values):
                    values[l] = float(val)
                result2_values_mean[i,(line_number-1)//2] = sum(values)/len(values)



if __name__ == "__main__":
    main()