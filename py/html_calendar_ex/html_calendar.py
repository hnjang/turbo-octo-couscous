#!/usr/bin/python3

import os
import shutil
import calendar
from jinja2 \
        import Environment, PackageLoader, select_autoescape, FileSystemLoader
from pprint import pprint


def mkdir_helper(dname):
    try:
        os.mkdir(dname)
    except FileExistsError:
        # keep silent
        pass
    print('Created {}'.format(dname))


def copytree_helper(src, dest):
    try:
        shutil.copytree(src, dest)
    except FileExistsError:
        pass
    print('Created {}'.format(dest))


def get_days_of_month(year, month):
    (first_weekday, day_cnt) = calendar.monthrange(year, month)
    head = (first_weekday + 1) % 7
    tail = 42 - head - day_cnt
    result = [''] * head + [str(x) for x in range(1, day_cnt+1)] + [''] * tail
    return result

output_dir = 'output'
html_fname = 'calendar.html'
mkdir_helper('./{}'.format(output_dir))

copytree_helper('./templates/static', './{}/static'.format(output_dir))

env = Environment(
    loader=FileSystemLoader('templates/html'),
    autoescape=select_autoescape(['html', 'xml']))

template = env.get_template(html_fname)

months = [] * 12
for i in range(12):
    m = {}
    m['name'] = calendar.month_name[i+1]
    m['days'] = get_days_of_month(2019, i+1)
    months.append(m)
# pprint(months)

content = template.render(months=months)
with open('{}/{}'.format(output_dir, html_fname), "wt", encoding="utf-8") as outf:
    outf.write(content)

print('Created ./{}/{}'.format(output_dir, html_fname))
