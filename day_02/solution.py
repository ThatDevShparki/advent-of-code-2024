import os


def get_input_data(path: str) -> list[list[int]]:
    abs_path = os.path.join(os.path.dirname(__file__), path)
    with open(abs_path, "r") as file:
        input_data: list[list[int]] = []
        for line in file:
            input_data.append(list(map(int, line.strip().split())))
        return input_data


def main() -> None:
    reports = get_input_data("input.txt")

    report_diffs: list[list[int]] = []
    for report in reports:
        report_diffs.append([report[i] - report[i - 1] for i in range(1, len(report))])

    report_affs: list[list[int]] = []
    for diff in report_diffs:
        report_aff = [1]
        report_aff.extend([diff[i] * diff[i - 1] for i in range(1, len(diff))])
        report_affs.append(report_aff)

    report_diff_masks: list[list[int]] = [
        [int(0 < abs(v) <= 3) for v in report_diff] for report_diff in report_diffs
    ]
    report_aff_masks: list[list[int]] = [
        [int(v > 0) for v in report_aff] for report_aff in report_affs
    ]

    # Part 1

    safe_reports = 0
    for report_diff_mask, report_aff_mask in zip(report_diff_masks, report_aff_masks):
        if all(report_diff_mask) and all(report_aff_mask):
            safe_reports += 1

    print("Number of safe reports:", safe_reports)

    # Part 2

    def is_report_safe(report: list[int], inner: bool = False) -> bool:
        diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
        affs = [1]
        affs.extend([diffs[i] * diffs[i - 1] for i in range(1, len(diffs))])

        diff_mask = [int(0 < abs(v) <= 3) for v in diffs]
        aff_mask = [int(v > 0) for v in affs]

        mask = [d * a for d, a in zip(diff_mask, aff_mask)]
        if all(mask):
            return True

        if not inner:
            for i in range(len(report)):
                if is_report_safe(report[:i] + report[i + 1 :], True):
                    return True

        return False

    safeish_reports = 0
    for report in reports:
        if is_report_safe(report):
            safeish_reports += 1

    print("Number of safeish reports:", safeish_reports)


if __name__ == "__main__":
    main()
