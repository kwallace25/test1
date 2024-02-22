#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:52:57 2024

@author: kristenwallace
"""

# PART 2.1

proteins = ['PF13411.1', 'PF12728.1', 'PF01381.2',
            'PF00205.2', 'PF10875.1', 'PF05766.1',
            'PF00860.2', 'PF13411.1', 'PF11812.1']


def count_unique_proteins(proteins):
    unique = list({protein[:7] for protein in proteins})
    return len(unique)


count_unique_proteins(proteins)

'''
comments on 2.1:
I ran the code i originally wrote and it failed when I tested it with
repeat PFs.
ie., I replaced the second to last protein with a repeat one to make sure the
result was 8 as intended.
A set should be easier to make unique  than a list. This leads me to use
sets, with comprehension notation from
https://python-reference.readthedocs.io/en/latest/docs/comprehensions
/set_comprehension.html

'''

# PART 2.2


def count_proteins(proteins):
    protein_dict = {}
    for protein in proteins:
        protein_dict[protein[:7]] = protein_dict.get(protein[:7], 0) + 1
    return protein_dict


count_proteins(proteins)

'''
comments on 2.2:
I think this one was already correct? Seems like it runs as intended.
I only forgot to slice the revision numbers
off to make sure the dict keys were only the protein family numbers.
To that end, I added the slicer [:7].

'''

# PART 2.3


def merge_protein_counts(dict1, dict2):
    combined_dict = {}
    both_dicts = set(dict1.keys()) | set(dict2.keys())
    for key in both_dicts:
        count_dict1 = dict1.get(key, 0)
        count_dict2 = dict2.get(key, 0)
        combined_dict[key] = (count_dict1, count_dict2)
    return combined_dict


proteins1 = ['PF13411.1', 'PF12728.1', 'PF01381.2',
            'PF00860.2', 'PF10875.1', 'PF00860.1',
            'PF00860.2', 'PF13411.1', 'PF11812.1']

proteins2 = ['PF13411.1', 'PF12728.1', 'PF01381.2',
            'PF00225.2', 'PF10225.1', 'PF05766.1',
            'PF00860.2', 'PF13411.1', 'PF11812.1']

merge_protein_counts(count_proteins(proteins1), count_proteins(proteins2))

'''
comments on 2.3:
I had  similar syntax in 2.2 using .get() properly, and meant to do that when
I wrote 'combined_dict.values' for 2.3 on the exam in pseudo code.
I misinterpreted the last sentence of the instructions as "report everything as
zero if absent from either dictionary", which should now be fixed. The if
statement was just not necessary.

'''

# PART 3.1

dates_list = ["February 6, 1992", "February 16, 1992", "February 27, 1992",
              "September 6, 1994", "December 1, 1993"]


def dates_to_iso8601(dates_list):
    ISO_dates = []
    for date in dates_list:
        month, day, year = date.split()
        months = {
            "January": "01",
            "February": "02",
            "March": "03",
            "April": "04",
            "May": "05",
            "June": '06',
            "July": "07",
            "August": "08",
            "September": "09",
            "October": "10",
            "November": "11",
            "December": "12"}
        ISO_month = months[month]
        ISO_day = day.replace(",", "")
        ISO_dates.append(f"{year}-{ISO_month}-{ISO_day.zfill(2)}")
    return ISO_dates


'''

comments on 3.1
Adding a leading zero with zfill
https://www.geeksforgeeks.org/python-add-leading-zeros-to-string/
I had a general idea of how this could have been done but could not put it
together. The .append() line is really what I needed to figure out
To access the values inside the braces, used the f-string documentation
https://peps.python.org/pep-0498/#:~:text=F%2Dstrings%20provide%20a%20way,
which%20contains%20expressions%20inside%20braces.
Had issues where the comma kept popping up in each date, removed with .replace

'''

# PART 3.2


def sort_dates(dates_list):
    def dates_to_iso8601(date):
        month, day, year = date.split()
        months = {
            "January": "01",
            "February": "02",
            "March": "03",
            "April": "04",
            "May": "05",
            "June": '06',
            "July": "07",
            "August": "08",
            "September": "09",
            "October": "10",
            "November": "11",
            "December": "12"}
        ISO_month = months[month]
        ISO_day = day.replace(",", "")
        return (f"{year}-{ISO_month}-{ISO_day.zfill(2)}")
    chronological = sorted(dates_list, key=dates_to_iso8601)
    return chronological


'''

comments on 3.2
I noted on the test that a helper function could have utility here, but working
through this I realized that 3.1 directly helps with 3.2, because to sort dates
the ISO format is much more convenient. So i reused that definition for
individual dates, and then sorted based on that key
https://docs.python.org/3/howto/sorting.html

'''
