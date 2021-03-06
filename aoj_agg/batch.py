#!/usr/bin/env python3

import csv
import sys

from tqdm import tqdm

import aggregator as aggregator
import const as const


def main(lecture_number: int = None) -> None:
    data = parse_csv()
    accepted = aggregate(data)
    score = {}
    for k, v in accepted.items():
        if lecture_number:
            score[k] = calc_score(v, lecture_number)
        else:
            score[k] = calc_score(v)
    for k, v in score.items():
        print(k, v)


def calc_score(accepted_problems: list, lecture_number: int = None) -> int:
    score_list = const.SCORE_LIST
    score = 0
    for index, score_dict in enumerate(score_list):
        if lecture_number and lecture_number != index + 1:
            continue
        for k, v in score_dict.items():
            # only scoring problem for beginner.
            # if k != 1:
            #     continue
            for problem in v:
                if problem in accepted_problems:
                    score += k
    return score


def parse_csv() -> list:
    csv_data = []
    # Download it from Waseda Moodle.
    with open('./Aizu_Online_Judge_.csv', 'r') as csv_fp:
        csv_reader = csv.DictReader(csv_fp)
        for line in csv_reader:
            csv_data.append(line)
    return csv_data


def aggregate(data) -> list:
    result = {}
    for line in tqdm(data):
        user_name = line['フルネーム']
        user_id = line['Q00_アカウント名']
        user_id = user_id.split('=')[-1] if '=' in user_id else user_id
        accepted = aggregator.main(user_id)
        result[user_name] = accepted
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdecimal():
        main(int(sys.argv[1]))
    else:
        main()
