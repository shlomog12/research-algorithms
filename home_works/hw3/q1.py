"""
 Author: Shlomo Glick
 Since : 2022-11
"""

import re


def print_valid_and_invalid_email_address_formats_by_filename(file_name: str):
    """
    Argument: file name
    This function searches for email addresses in a file.
    The function prints a list of the correct addresses and a list of the
    incorrect addresses according to the definition that appears
    here: https://help.xmatters.com/ondemand/trial/valid_email_format.htm

    >>> print_valid_and_invalid_email_address_formats_by_filename('./home_works/hw3/test3.txt')
    good: ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']
    bad: ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']
    """
    with open(file_name) as file:
        text = ' '.join([line for line in file])
    mail_addresses = re.findall("[#|\w|.|-]*@[#|\w|.|-]*", text)
    good, bad = get_good_and_bad_addresses(mail_addresses=mail_addresses)
    print(f'good: {good}')
    print(f'bad: {bad}')

def get_good_and_bad_addresses(mail_addresses: list):
    """
    Arguments: list of email addresses
    This function returns a list of good addresses and a list of bad addresses
    >>> get_good_and_bad_addresses(['abc-d@mail.com', 'abc-@mail.com', 'abc..def@mail.com'])
    (['abc-d@mail.com'], ['abc-@mail.com', 'abc..def@mail.com'])

    >>> get_good_and_bad_addresses(['_dd@', 'abc-@mail...com', 'a', '@22'])
    ([], ['_dd@', 'abc-@mail...com', 'a', '@22'])

    >>> get_good_and_bad_addresses([])
    ([], [])
    """
    good = []
    bad = []
    for mail in mail_addresses:
        prefix_domain = mail.split('@')
        if len(prefix_domain) != 2:
            bad.append(mail)
            continue
        prefix, domain = prefix_domain[0], prefix_domain[1]
        if valid_prefix(prefix) and valid_domain(domain):
            good.append(mail)
        else:
            bad.append(mail)
    return good, bad

def valid_prefix(prefix: str):
    num_or_letters = '[^_\W]'
    allowed_characters = '[\w.-]'
    return re.match(f'^({num_or_letters}({allowed_characters}{num_or_letters}+)*)+$',prefix)

def valid_domain(domain: str):
    allowed_characters = '([^_\W]|-)'
    return re.match(f'^({allowed_characters}+\.({allowed_characters}){{2,}})+$',domain)


def main():
    import doctest
    print(doctest.testmod())
    # examples:
    # print_valid_and_invalid_email_address_formats_by_filename('./home_works/hw3/test1.txt')
    # print_valid_and_invalid_email_address_formats_by_filename('./home_works/hw3/test2.txt')
    # print_valid_and_invalid_email_address_formats_by_filename('./home_works/hw3/test4.txt')

if __name__ == "__main__":
    main()