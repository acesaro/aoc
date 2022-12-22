import argparse
import logging


def calorie_sum(items: list[int] = []):
    return sum(items)


def main():
    elves_items: list[list[int]] = [[]]
    elves_calorie_sums: list[int] = []
    elf_count = 0
    top_calorie_sum = 0
    inputs_file = "amcpu/y2022/day1/inputs.txt"

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        dest="logging_level",
        type=str,
        default="INFO",
        help="Logging level",
        choices=["ERROR", "WARN", "INFO", "DEBUG"],
    )

    args = parser.parse_args()

    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(message)s", level=args.logging_level
    )

    with open(inputs_file) as f:
        for line in f.readlines():
            try:
                calories = int(line)
                logging.debug(f"Adding {calories} to elves_items[{elf_count}] list")
                elves_items[elf_count].append(calories)
            except ValueError:
                logging.debug(
                    f"Non-integer fount, incrementing elf_count to {elf_count + 1}"
                )
                elf_count += 1
                elves_items.append([])

    for elf in elves_items:
        elf_calorie_sum = calorie_sum(elf)
        elves_calorie_sums.append(elf_calorie_sum)
        if elf_calorie_sum > top_calorie_sum:
            top_calorie_sum = elf_calorie_sum

    elves_calorie_sums.sort(reverse=True)
    top_three_calorie_sum = sum(elves_calorie_sums[0:3])

    logging.info(f"Top calorie sum: {top_calorie_sum}")
    logging.info(f"Top three elves calorie sum: {top_three_calorie_sum}")
