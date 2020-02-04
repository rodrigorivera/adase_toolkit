

def featurization(rips_filtrations, ratio=0.8):
    if type(rips_filtrations[0]) == list:
        #         print('Not only 0-dim homologies are available')

        n_d_0 = []
        n_d_1 = []

        max_d_0 = []
        max_d_1 = []

        relevant_points_0 = []
        relevant_points_1 = []

        av_d_0 = []
        av_d_1 = []

        sums_d_0 = []
        sums_d_1 = []

        for PDs in (rips_filtrations):

            n_d_0.append(len(PDs[0]))
            n_d_1.append(len(PDs[1]))

            if len(PDs[0]) > 1:
                a = max((PDs[0][:, 1] - PDs[0][:, 0])[:-1]) * 100
                max_d_0.append(a)

                ratio_max_d_0 = ratio * a
                b = sum((PDs[0][:, 1] - PDs[0][:, 0])[:-1] >= ratio_max_d_0) - 1
                relevant_points_0.append(max(b, 0))

                av_d_0.append(((PDs[0][:, 1] - PDs[0][:, 0])[:-1]).mean() * 10)

                sums_d_0.append(((PDs[0][:, 1] - PDs[0][:, 0])[:-1]).sum() * 10)

            else:
                max_d_0.append(0)
                relevant_points_0.append(0)
                av_d_0.append(0)
                sums_d_0.append(0)

            if len(PDs[1]) != 0:
                a = max(PDs[1][:, 1] - PDs[1][:, 0]) * 100
                max_d_1.append(a)

                ratio_max_d_1 = ratio * a
                b = sum((PDs[1][:, 1] - PDs[1][:, 0])[:-1] >= ratio_max_d_1) - 1
                relevant_points_1.append(max(b, 0))

                av_d_1.append((PDs[1][:, 1] - PDs[1][:, 0]).mean() * 10)

                sums_d_1.append((PDs[1][:, 1] - PDs[1][:, 0]).sum() * 10)

            else:
                max_d_1.append(0)
                relevant_points_1.append(0)
                av_d_1.append(0)
                sums_d_1.append(0)

        total_features = np.vstack(
            [n_d_0, n_d_1, max_d_0, max_d_1, relevant_points_0, relevant_points_1, av_d_0, av_d_1, sums_d_0,
             sums_d_1]).T
        return total_features

    elif type(rips_filtrations[0]) == np.ndarray:
        #         print('Only 0-dim homologies are available')
        n_d_0 = []

        max_d_0 = []

        relevant_points_0 = []

        av_d_0 = []

        sums_d_0 = []

        for PD in (rips_filtrations):

            n_d_0.append(len(PD))

            if len(PD) > 1:
                a = max((PD[:, 1] - PD[:, 0])[:-1]) * 100
                max_d_0.append(a)

                ratio_max_d_0 = ratio * a
                b = sum((PD[:, 1] - PD[:, 0])[:-1] >= ratio_max_d_0) - 1
                relevant_points_0.append(max(b, 0))

                av_d_0.append(((PD[:, 1] - PD[:, 0])[:-1]).mean() * 10)

                sums_d_0.append(((PD[:, 1] - PD[:, 0])[:-1]).sum() * 10)

            else:
                max_d_0.append(0)
                relevant_points_0.append(0)
                av_d_0.append(0)
                sums_d_0.append(0)

        total_features = np.vstack([n_d_0, max_d_0, relevant_points_0, av_d_0, sums_d_0]).T
        return total_features