
import re


def serch_and_valid_email_address_format_by_file_name(file_name):
    with open(file_name) as file:
        text = ' '.join([line for line in file])
    mail_addresses = re.findall("[#|\w.-]*@[#|\w.-]*", text)
    return valid_email_address_format(mail_addresses=mail_addresses)

def valid_email_address_format(mail_addresses):
    good = []
    bad = []
    for mail in mail_addresses:
        prefix_domain = mail.split('@')
        prefix = prefix_domain[0]
        domain = prefix_domain[1]
        if valid_prefix(prefix) and valid_domain(domain):
            good.append(mail)
        else:
            bad.append(mail)
    return good, bad

def valid_prefix(prefix):
    num_or_letters = '[^_\W]'
    allowed_characters = '[\w.-]'
    return re.match(f'^({num_or_letters}({allowed_characters}{num_or_letters}+)*)+$',prefix)

def valid_domain(domain):
    allowed_characters = '([^_\W]|-)'
    return re.match(f'^({allowed_characters}+\.({allowed_characters}){{2,}})+$',domain)


def main():
    good, bad =serch_and_valid_email_address_format_by_file_name('./home_works/hw3/test2.txt')
    print(f'good: {good}')
    print(f'bad: {bad}')
    

    # import doctest
    # print(doctest.testmod())

if __name__ == "__main__":
    main()