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


    # Plots  N/opti pour chaque function et type

    # for type_number, type_str in enumerate(result_1_type):
    #     for func_number, func_name in enumerate(result_1_function):
    #         data = result1_values_mean[type_number,:,:,func_number]

    #         # Set up the plot
    #         fig, ax = plt.subplots(figsize=(10, 6))

    #         # Number of groups and bars per group
    #         num_groups, num_bars = len(result_1_N), len(result_1_opti)

    #         # Bar width and positioning
    #         bar_width = 0.2
    #         group_spacing = 0.5  # Adjust this for more or less spacing between groups
    #         x = np.arange(num_groups) * (num_bars * bar_width + group_spacing)  # Adding space between groups

    #         # Plotting each set of bars
    #         for i in range(num_bars):
    #             ax.bar(x + i * bar_width, data[:, i], width=bar_width, label=f'O{result_1_opti[i]}')

    #         # Add labels, title, and legend
    #         ax.set_xlabel('N')
    #         ax.set_ylabel('Number of cycle/iteration')
    #         ax.set_title(f'Impact of the optimisation and N on the function {func_name} with type {type_str}')
    #         ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    #         ax.set_xticklabels([f'N = {result_1_N[i]}' for i in range(num_groups)])
    #         ax.legend()
    #         plt.savefig(f'./plot_N_opti/opti_N_{type_str}_{func_name}.pdf')
    #         #plt.show()

    # Plots  N/opti pour chaque function et type

    # for opti_number, opti_str in enumerate(result_1_opti):
    #     for func_number, func_name in enumerate(result_1_function):
    #         data = np.transpose(result1_values_mean[:,:,opti_number,func_number])

    #         # Set up the plot
    #         fig, ax = plt.subplots(figsize=(10, 6))

    #         # Number of groups and bars per group
    #         num_groups, num_bars = len(result_1_N), len(result_1_type)

    #         # Bar width and positioning
    #         bar_width = 0.2
    #         group_spacing = 0.5  # Adjust this for more or less spacing between groups
    #         x = np.arange(num_groups) * (num_bars * bar_width + group_spacing)  # Adding space between groups

    #         # Plotting each set of bars
    #         for i in range(num_bars):
    #             ax.bar(x + i * bar_width, data[:, i], width=bar_width, label=f'{result_1_type[i]}')

    #         # Add labels, title, and legend
    #         ax.set_xlabel('N')
    #         ax.set_ylabel('Number of cycle/iteration')
    #         ax.set_title(f'Impact of the type and N on the function {func_name} with O{opti_str}')
    #         ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    #         ax.set_xticklabels([f'N = {result_1_N[i]}' for i in range(num_groups)])
    #         ax.legend()
    #         plt.savefig(f'./plot_N_type/N_type_O{opti_str}_{func_name}.pdf')
    #         #plt.show()


if __name__ == "__main__":
    main()