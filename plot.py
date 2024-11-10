import matplotlib.pyplot as plt
import numpy as np


def main() -> None:

    CPU_freq = 2.5 * 1e9        # 2.50 GHz
    L1_cache_size = 64 * 1e3    # 64 KiB    
    L2_cache_size = 512 * 1e3   # 512 KiB    
    L3_cache_size = 3 * 1e6     # 3 MiB

    # Processing data generated during script 1

    result_1_type = ["char",  "short", "int", "double", "float"]
    result_1_N = ["100", "500", "1000"]
    result_1_opti = ["0", "1", "2", "3"]
    result_1_function = ["ZERO", "COPY_ij", "COPY_ji", "ADD_ij", "ADD_ji", "PS", "MM_ijk", "MM_ikj", "MM_B_ijk"]

    result1_values_mean = np.zeros((len(result_1_type),len(result_1_N),len(result_1_opti),len(result_1_function)))

    # store the min values of each function in the result_values_mean table

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
                        result1_values_mean[i,j,k,(line_number-1)//2] =  min(values)


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
    #         plt.close()
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
    #         plt.close()
    #         #plt.show()



    # Processing data generated during script 2

    result_2_N = ["25", "50", "75", "100", "250", "500", "1000", "1500", "2000", "3000"]
    result_2_function = ["MM_ijk", "MM_ikj", "MM_B_ijk (BL =16)"]

    result2_values_mean = np.zeros((len(result_2_N),len(result_2_function)))

    # store the mean values of each function in the result_values_mean table


    for i,N in enumerate(result_2_N):
        with open(f"./results_2/result_float_N{N}_O2.txt") as file:
            lines = file.readlines()
            for line_number in range(1,7,2):
                line = lines[line_number]
                values = line.split('\t')[1:]
                for l,val in enumerate(values):
                    values[l] = float(val)
                result2_values_mean[i,(line_number-1)//2] =  min(values)
    
    # fig, ax = plt.subplots(figsize=(10, 6))
    # for func_index, func_name  in enumerate(result_2_function):
    #     plt.plot([int(n) for n in result_2_N], result2_values_mean[:,func_index],"-o",label=func_name)
    # plt.title("Impact of N on different dot product function(N = 1000, O = 2, type = float)")
    # plt.xlabel("N")
    # plt.ylabel("Cycles / Iteration")
    # plt.legend()
    # plt.savefig("./plot_tr/Impact_of_N_on_dot_product.pdf")
    # plt.close()
    # #plt.show()

    # Loading data from result_blk

    n_blks = list(range(1,129)) + list(range(128, 1024, 8))

    blks_cycles_per_itr = np.zeros((len(n_blks),))

    for i,n in enumerate(n_blks):
        with open(f"./results_blk/result_float_N1000_O2_blk{n}.txt") as file:
            lines = file.readlines()
            blks_cycles_per_itr[i]+= min([float(val) for val in lines[1].split('\t')[1:]])

    
    # fig, ax = plt.subplots(figsize=(10, 6))
    # plt.plot(n_blks, blks_cycles_per_itr)
    # plt.title("Impact of the block size on MM_B_ijk (N = 1000, O = 2, type = float)")
    # plt.xlabel("block size")
    # plt.ylabel("Cycles / Iteration")
    # plt.savefig("./plot_blk/Impact_of_blk_size.pdf")
    # plt.close()
    # #plt.show()


    # Loading data from result_tr

    result_t_type = ["int", "float"]
    result_t_N = ["1000"]
    result_t_opti = ["2"]
    result_t_function = ["MM_ijk", "MM_t_ijk", "MM_ikj", "MM_B_ijk"]

    result_tr_values_mean = np.zeros((len(result_t_type),len(result_t_function)))

    # store the min values of each function in the result_values_mean table

    for type_index,data_type in enumerate(result_t_type):
        with open(f"./results_tr/result_{data_type}_N1000_O2.txt") as file:
            lines = file.readlines()
            for line_number in range(1,8,2):
                line = lines[line_number]
                values = line.split('\t')[1:]
                for l,val in enumerate(values):
                    values[l] = float(val)
                result_tr_values_mean[type_index,(line_number-1)//2] = min(values)

    # data = result_tr_values_mean
    # # Set up the plot
    # fig, ax = plt.subplots(figsize=(10, 6))
    # # Number of groups and bars per group
    # num_groups, num_bars = len(result_t_type), len(result_t_function)
    # # Bar width and positioning
    # bar_width = 0.2
    # group_spacing = 0.5  # Adjust this for more or less spacing between groups
    # x = np.arange(num_groups) * (num_bars * bar_width + group_spacing)  # Adding space between groups
    # # Plotting each set of bars
    # for i in range(num_bars):
    #     ax.bar(x + i * bar_width, data[:, i], width=bar_width, label=f'{result_t_function[i]}')
    # # Add labels, title, and legend
    # ax.set_xlabel('Type')
    # ax.set_ylabel('Number of cycle/iteration')
    # ax.set_title(f'Impact of the mul function on Int and Float (N = 1000, O = 2)')
    # ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    # ax.set_xticklabels([f'{result_t_type[i]}' for i in range(num_groups)])
    # ax.legend()
    # plt.savefig(f'./plot_tr/plot_transpose.pdf')
    # plt.close()
    # #plt.show()


if __name__ == "__main__":
    main()