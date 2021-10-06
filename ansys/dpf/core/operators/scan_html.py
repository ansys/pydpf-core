"""
Get available operators, categories, and short names from "dpf.html"
"""
import argparse
import os
import black
from warnings import warn

from bs4 import BeautifulSoup


def interpert_html(this_path):
    """Get available operators, categories, and short names from 'dpf.html'"""
    project_root_dir = os.path.abspath(os.curdir)
    html_file = os.path.join(project_root_dir, "docs", "source", "_static", "dpf.html")
    with open(html_file, "r", encoding="latin1") as f:
        contents = f.read()
    soup = BeautifulSoup(contents, features="html.parser")

    operators = soup.findAll(class_="operator")
    result = {}
    for operator in operators:
        scp = operator.find_all("scripting-part")[0]
        name = scp.get("cpp-name")
        short_name = scp.get("scripting_name")
        if name in result:
            warn(f"Duplicate name {name}")
        result[name] = {"category": scp.get("cat"), "short_name": short_name}

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan dpf.html file.")
    parser.add_argument("--operators-file", default="_operators_list")
    args = parser.parse_args()

    this_path = os.path.dirname(os.path.abspath(__file__))
    operators_file = os.path.join(this_path, args.operators_file + ".py")
    operators = interpert_html(this_path)
    print(f"Extracted {len(operators)} operators to {operators_file}.")
    with open(operators_file, "w") as f:
        operator_contents = black.format_str(
            f"operators = {operators}", mode=black.FileMode()
        )
        f.write(operator_contents)
