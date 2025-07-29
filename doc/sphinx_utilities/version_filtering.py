#
from pathlib import Path


def get_tutorial_version_requirements(tutorial_path: str) -> str:
    note_flag = r".. note::"
    version_flag = "This tutorial requires DPF"
    previous_line_is_note = False
    minimum_version = "0.0"
    tutorial_path = Path(tutorial_path)
    skip_empty_line = False
    with tutorial_path.open(mode="rt", encoding="utf-8") as tutorial_file:
        for line in tutorial_file:
            if (version_flag in line) and previous_line_is_note:
                minimum_version = line.strip(version_flag).split()[0]
                break
            if note_flag in line:
                previous_line_is_note = True
                skip_empty_line = True
            else:
                if skip_empty_line:
                    skip_empty_line = False
                else:
                    previous_line_is_note = False
    return minimum_version
