import csv
import sys

reverse_item = [2, 9, 11, 14, 19]
interest_enjoyment_item = [1, 5, 8, 10, 14, 17, 20]
perceived_competence_item = [4, 7, 12, 16, 22]
perceived_choice_item = [3, 11, 15, 19, 21]
pressure_tension_item = [2, 6, 9, 13, 18]


def main():
    interest_enjoyment_sum = 0
    perceived_competence_sum = 0
    perceived_choice_sum = 0
    pressure_tension_sum = 0
    res = {}

    with open(sys.argv[1]) as f:
        f2 = csv.reader(f, delimiter=",", doublequote=True,
                        lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        header = next(f2)
        for i, row in enumerate(f2):
            # print("---------------------------------")
            for j, ans in enumerate(row):

                if ans == '':
                    row[1] = i

                if j-1 in interest_enjoyment_item:
                    interest_enjoyment_sum += return_true_result(int(ans), j-1)

                elif j-1 in perceived_competence_item:
                    perceived_competence_sum += return_true_result(
                        int(ans), j-1)

                elif j-1 in perceived_choice_item:
                    perceived_choice_sum += return_true_result(int(ans), j-1)

                elif j-1 in pressure_tension_item:
                    pressure_tension_sum += return_true_result(int(ans), j-1)

            res[row[1]] = [interest_enjoyment_sum,
                           perceived_competence_sum, perceived_choice_sum, pressure_tension_sum]

            interest_enjoyment_sum = 0
            perceived_competence_sum = 0
            perceived_choice_sum = 0
            pressure_tension_sum = 0

    print(res)
    # print(calc_average(res))


def calc_average(res):
    # 平均を出すことにあまり意味はない
    interest_enjoyment_sum_all = 0
    perceived_competence_sum_all = 0
    perceived_choice_sum_all = 0
    pressure_tension_sum_all = 0
    # val == [1,2,3,4]
    for val in res.values():
        interest_enjoyment_sum_all += val[0]
        perceived_competence_sum_all += val[1]
        perceived_choice_sum_all += val[2]
        pressure_tension_sum_all += val[3]

    return [interest_enjoyment_sum_all/len(res), perceived_competence_sum_all/len(res), perceived_choice_sum_all/len(res), pressure_tension_sum_all/len(res)]


def return_true_result(ans: int, index: int):
    if index in reverse_item:
        return 8 - ans
    else:
        return ans


if __name__ == '__main__':
    main()
