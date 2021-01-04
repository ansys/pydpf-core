"""
Get available operators, categories, and short names from "dpf.html"
"""
import os
from bs4 import BeautifulSoup


def interpert_html():
    """Get available operators, categories, and short names from 'dpf.html'"""
    with open('dpf.html', 'r', encoding='latin1') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html')

    operators = soup.findAll(class_="operator")
    oper_dict = {}
    for operator in operators:
        scp = operator.find_all('scripting-part')[0]
        name = scp.get('cpp-name')
        oper_dict[name] = {'category': scp.get('cat'),
                           'short_name': scp.get('scripting_name')}

    return oper_dict


if __name__ == '__main__':
    this_path = os.path.dirname(os.path.abspath(__file__))
    oper_file = os.path.join(this_path, '_operators_list.py')
    oper_dict = interpert_html()
    with open(oper_file, 'w') as f:
        f.write('oper_dict = ' + str(oper_dict))
