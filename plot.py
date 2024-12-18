import matplotlib.pyplot as plt
import numpy as np


def main() -> None:

    CPU_freq = 2.5 * 1e9  # 2.50 GHz
    L1_cache_size = 64 * 1e3  # 64 KiB
    L2_cache_size = 512 * 1e3  # 512 KiB
    L3_cache_size = 3 * 1e6  # 3 MiB

    # Processing data generated during script 1

    result_1_type = ["char", "short", "int", "float", "double"]
    result_1_N = ["100", "500", "1000"]
    result_1_opti = ["0", "1", "2", "3"]
    result_1_function = [
        "ZERO",
        "COPY_ij",
        "COPY_ji",
        "ADD_ij",
        "ADD_ji",
        "PS",
        "MM_ijk",
        "MM_ikj",
        "MM_B_ijk",
    ]

    result1_values_mean = np.zeros(
        (
            len(result_1_type),
            len(result_1_N),
            len(result_1_opti),
            len(result_1_function),
        )
    )

    # store the min values of each function in the result_values_mean table

    for i, data_type in enumerate(result_1_type):
        for j, N in enumerate(result_1_N):
            for k, opti in enumerate(result_1_opti):
                with open(f"./results_1/result_{data_type}_N{N}_O{opti}.txt") as file:
                    lines = file.readlines()
                    for line_number in range(1, 19, 2):
                        line = lines[line_number]
                        values = line.split("\t")[1:]
                        for l, val in enumerate(values):
                            values[l] = float(val)
                        result1_values_mean[i, j, k, (line_number - 1) // 2] = min(
                            values
                        )

    # Plots  N/opti pour chaque function et type

    # for type_number, type_str in enumerate(result_1_type):
    #     for func_number, func_name in enumerate(result_1_function):
    #         data = result1_values_mean[type_number, :, :, func_number]

    #         # Set up the plot
    #         fig, ax = plt.subplots(figsize=(10, 6))

    #         # Number of groups and bars per group
    #         num_groups, num_bars = len(result_1_N), len(result_1_opti)

    #         # Bar width and positioning
    #         bar_width = 0.2
    #         group_spacing = 0.5  # Adjust this for more or less spacing between groups
    #         x = np.arange(num_groups) * (
    #             num_bars * bar_width + group_spacing
    #         )  # Adding space between groups

    #         # Plotting each set of bars
    #         for i in range(num_bars):
    #             ax.bar(
    #                 x + i * bar_width,
    #                 data[:, i],
    #                 width=bar_width,
    #                 label=f"O{result_1_opti[i]}",
    #             )

    #         # Add labels, title, and legend
    #         ax.set_xlabel("N")
    #         ax.set_ylabel("Number of cycle/iteration")
    #         ax.set_title(
    #             f"Impact of the optimisation and N on the function {func_name} with type {type_str}"
    #         )
    #         ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    #         ax.set_xticklabels([f"N = {result_1_N[i]}" for i in range(num_groups)])
    #         ax.legend()
    #         plt.savefig(f"./plot_N_opti/opti_N_{type_str}_{func_name}.png")
    #         plt.close()
    #         # plt.show()

    # Plots  N/type pour chaque function et type

    # for opti_number, opti_str in enumerate(result_1_opti):
    #     for func_number, func_name in enumerate(result_1_function):
    #         data = np.transpose(result1_values_mean[:, :, opti_number, func_number])

    #         # Set up the plot
    #         fig, ax = plt.subplots(figsize=(10, 6))

    #         # Number of groups and bars per group
    #         num_groups, num_bars = len(result_1_N), len(result_1_type)

    #         # Bar width and positioning
    #         bar_width = 0.2
    #         group_spacing = 0.5  # Adjust this for more or less spacing between groups
    #         x = np.arange(num_groups) * (
    #             num_bars * bar_width + group_spacing
    #         )  # Adding space between groups

    #         # Plotting each set of bars
    #         for i in range(num_bars):
    #             ax.bar(
    #                 x + i * bar_width,
    #                 data[:, i],
    #                 width=bar_width,
    #                 label=f"{result_1_type[i]}",
    #             )

    #         # Add labels, title, and legend
    #         ax.set_xlabel("N")
    #         ax.set_ylabel("Number of cycle/iteration")
    #         ax.set_title(
    #             f"Impact of the type and N on the function {func_name} with O{opti_str}"
    #         )
    #         ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    #         ax.set_xticklabels([f"N = {result_1_N[i]}" for i in range(num_groups)])
    #         ax.legend()
    #         plt.savefig(f"./plot_N_type/N_type_O{opti_str}_{func_name}.png")
    #         plt.close()
    #         # plt.show()

    # Plots  N/type pour chaque function et type

    # opti_number, opti_str = 3, "3"
    # type_size = [1, 2, 4, 4, 8]
    # for func_number, func_name in enumerate(result_1_function):
    #     data = np.transpose(result1_values_mean[:, :, opti_number, func_number])

    #     # Set up the plot
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Number of groups and bars per group
    #     num_groups, num_bars = len(result_1_N), len(result_1_type)

    #     # Bar width and positioning
    #     bar_width = 0.2
    #     group_spacing = 0.5  # Adjust this for more or less spacing between groups
    #     x = np.arange(num_groups) * (
    #         num_bars * bar_width + group_spacing
    #     )  # Adding space between groups

    #     # Plotting each set of bars
    #     for i in range(num_bars):
    #         ax.bar(
    #             x + i * bar_width,
    #             (type_size[i] * CPU_freq * 1e-9) / data[:, i],
    #             width=bar_width,
    #             label=f"{result_1_type[i]}",
    #         )

    #     # Add labels, title, and legend
    #     ax.set_xlabel("N")
    #     ax.set_ylabel("Débit (Go/s)")
    #     ax.set_title(
    #         f"Débit en fonction de N et du type sur la function {func_name} avec O{opti_str}"
    #     )
    #     ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    #     ax.set_xticklabels([f"N = {result_1_N[i]}" for i in range(num_groups)])
    #     ax.legend()
    #     plt.savefig(f"./plot_timing/N_type_O{opti_str}_{func_name}.png")
    #     plt.savefig(f"./plot_timing/N_type_O{opti_str}_{func_name}.pdf")
    #     plt.close()
    #     # plt.show()

    # Copy

    # opti_number, opti_str = 2, "2"
    # type_size = [1, 2, 4, 4, 8]
    # type_index = 3
    # data = result1_values_mean[type_index, :, opti_number, 1:3]

    # # Set up the plot
    # fig, ax = plt.subplots(figsize=(10, 6))

    # # Number of groups and bars per group
    # num_groups, num_bars = len(result_1_N), len([1, 2])

    # # Bar width and positioning
    # bar_width = 0.2
    # group_spacing = 0.5  # Adjust this for more or less spacing between groups
    # x = np.arange(num_groups) * (
    #     num_bars * bar_width + group_spacing
    # )  # Adding space between groups

    # # Plotting each set of bars
    # for i in range(num_bars):
    #     ax.bar(
    #         x + i * bar_width,
    #         data[:, i],
    #         width=bar_width,
    #         label=f"{result_1_function[i+1]}",
    #     )

    # # Add labels, title, and legend
    # ax.set_xlabel("N")
    # ax.set_ylabel("Cycles / itération")
    # ax.set_title(
    #     f"Cycle par itération pour copy de matrice avec O{opti_str} pour type float"
    # )
    # ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    # ax.set_xticklabels([f"N = {result_1_N[i]}" for i in range(num_groups)])
    # ax.legend()
    # plt.savefig(f"./plot_copy/copy_O{opti_str}.png")
    # plt.savefig(f"./plot_copy/copy_O{opti_str}.pdf")
    # plt.close()
    # # plt.show()

    # # Add

    # opti_number, opti_str = 2, "2"
    # type_size = [1, 2, 4, 4, 8]
    # type_index = 3
    # data = result1_values_mean[type_index, :, opti_number, 3:5]

    # # Set up the plot
    # fig, ax = plt.subplots(figsize=(10, 6))

    # # Number of groups and bars per group
    # num_groups, num_bars = len(result_1_N), len([3, 4])

    # # Bar width and positioning
    # bar_width = 0.2
    # group_spacing = 0.5  # Adjust this for more or less spacing between groups
    # x = np.arange(num_groups) * (
    #     num_bars * bar_width + group_spacing
    # )  # Adding space between groups

    # # Plotting each set of bars
    # for i in range(num_bars):
    #     ax.bar(
    #         x + i * bar_width,
    #         data[:, i],
    #         width=bar_width,
    #         label=f"{result_1_function[i+3]}",
    #     )

    # # Add labels, title, and legend
    # ax.set_xlabel("N")
    # ax.set_ylabel("Cycles / itération")
    # ax.set_title(
    #     f"Cycle par itération pour add de matrice avec O{opti_str} pour type float"
    # )
    # ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    # ax.set_xticklabels([f"N = {result_1_N[i]}" for i in range(num_groups)])
    # ax.legend()
    # plt.savefig(f"./plot_add/add_O{opti_str}.png")
    # plt.savefig(f"./plot_add/add_O{opti_str}.pdf")
    # plt.close()
    # # plt.show()

    # Processing data generated during script 2

    result_2_N = [f"{i}" for i in range(11, 351)]
    result_2_function = ["MM_ijk", "MM_ikj", "MM_B_ijk (BL =16)"]

    result2_values_mean = np.zeros((len(result_2_N), len(result_2_function)))

    # store the mean values of each function in the result_values_mean table

    for i, N in enumerate(result_2_N):
        with open(f"./results_2/result_float_N{N}_O2.txt") as file:
            lines = file.readlines()
            for line_number in range(1, 7, 2):
                line = lines[line_number]
                values = line.split("\t")[1:]
                for l, val in enumerate(values):
                    values[l] = float(val)
                result2_values_mean[i, (line_number - 1) // 2] = min(values)

    fig, ax = plt.subplots(figsize=(10, 6))
    for func_index, func_name in enumerate(result_2_function):
        plt.plot(
            [int(n) for n in result_2_N],
            result2_values_mean[:, func_index],
            "-",
            label=func_name,
        )
    plt.title("Impact of N on different dot product function(O = 2, type = float)")
    plt.xlabel("N")
    plt.ylabel("Cycles / Iteration")
    plt.legend()
    # plt.savefig("./plot_tr/Impact_of_N_on_dot_product.png")
    # plt.savefig("./plot_tr/Impact_of_N_on_dot_product.pdf")
    # plt.close()
    # plt.show()

    fig, ax = plt.subplots(figsize=(10, 6))
    for func_index, func_name in enumerate(result_2_function[:1]):
        plt.plot(
            [int(n) for n in result_2_N],
            result2_values_mean[:, func_index],
            "-",
            label=func_name,
        )
    plt.title("Impact of N on mm_ijk (O = 2, type = float)")
    plt.xlabel("N")
    plt.ylabel("Cycles / Iteration")
    plt.legend()
    plt.savefig("./plot_tr/Impact_mm_ijk.png")
    plt.savefig("./plot_tr/Impact_mm_ijk.pdf")
    plt.show()
    plt.close()

    # fig, ax = plt.subplots(figsize=(10, 6))
    # for func_index, func_name in enumerate(result_2_function):
    #     plt.plot(
    #         [int(n) for n in result_2_N],
    #         result2_values_mean[:, func_index] / CPU_freq * 1e9,
    #         "-",
    #         label=func_name,
    #     )
    # plt.title(
    #     "Temps d'execution par itération des multiplications matricielles (O = 2, type = float)"
    # )
    # plt.xlabel("N")
    # plt.ylabel("temps (µs)")
    # plt.legend()
    # plt.savefig("./plot_tr/timing_on_dot_product.png")
    # plt.savefig("./plot_tr/timing_on_dot_product.pdf")
    # plt.close()
    # plt.show()

    # Loading data from result_blk

    n_blks = list(range(2, 129)) + list(range(128, 1024, 8))

    blks_cycles_per_itr = np.zeros((len(n_blks),))

    for i, n in enumerate(n_blks):
        with open(f"./results_blk/result_float_N1000_O2_blk{n}.txt") as file:
            lines = file.readlines()
            blks_cycles_per_itr[i] += min(
                [float(val) for val in lines[1].split("\t")[1:]]
            )

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(n_blks, blks_cycles_per_itr, label="mm_b_ijk(BL)")
    plt.plot([2, 1024], [3.63574, 3.63574], label="mm_ijk")
    plt.plot([2, 1024], [0.500909, 0.500909], label="mm_ikj")
    plt.title("Impact of the block size on MM_B_ijk (N = 1000, O = 2, type = float)")
    plt.xlabel("block size")
    plt.ylabel("Cycles / Iteration")
    plt.legend()
    # plt.savefig("./plot_blk/Impact_of_blk_size.png")
    plt.close()
    # plt.show()

    # Loading data from result_tr

    result_t_type = ["int", "float"]
    result_t_N = ["1000"]
    result_t_opti = ["2"]
    result_t_function = ["MM_ijk", "MM_t_ijk", "MM_ikj", "MM_B_ijk"]

    result_tr_values_mean = np.zeros((len(result_t_type), len(result_t_function)))

    # store the min values of each function in the result_values_mean table

    for type_index, data_type in enumerate(result_t_type):
        with open(f"./results_tr/result_{data_type}_N1000_O2.txt") as file:
            lines = file.readlines()
            for line_number in range(1, 8, 2):
                line = lines[line_number]
                values = line.split("\t")[1:]
                for l, val in enumerate(values):
                    values[l] = float(val)
                result_tr_values_mean[type_index, (line_number - 1) // 2] = min(values)

    # data = result_tr_values_mean
    # # Set up the plot
    # fig, ax = plt.subplots(figsize=(10, 6))
    # # Number of groups and bars per group
    # num_groups, num_bars = len(result_t_type), len(result_t_function)
    # # Bar width and positioning
    # bar_width = 0.2
    # group_spacing = 0.5  # Adjust this for more or less spacing between groups
    # x = np.arange(num_groups) * (
    #     num_bars * bar_width + group_spacing
    # )  # Adding space between groups
    # # Plotting each set of bars
    # for i in range(num_bars):
    #     ax.bar(
    #         x + i * bar_width,
    #         data[:, i],
    #         width=bar_width,
    #         label=f"{result_t_function[i]}",
    #     )
    # # Add labels, title, and legend
    # ax.set_xlabel("Type")
    # ax.set_ylabel("Number of cycle/iteration")
    # ax.set_title(f"Impact of the mul function on Int and Float (N = 1000, O = 2)")
    # ax.set_xticks(x + bar_width * (num_bars - 1) / 2)
    # ax.set_xticklabels([f"{result_t_type[i]}" for i in range(num_groups)])
    # ax.legend()
    # plt.savefig(f"./plot_tr/plot_transpose.png")
    # plt.close()
    # # plt.show()


if __name__ == "__main__":
    main()
