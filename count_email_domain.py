import random
import string
import pdb

pdb.set_trace()
import re
import collections


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def count_email_domain_v1():
    with open('mails.txt') as f:
        text = f.read()

    domains = re.findall(r'@(.*)$', text, re.MULTILINE)
    mail_values = collections.Counter(domains)
    # Outputs example: Counter({'gmail.com':4, 'yahoo.com':3})
    return mail_values


def count_email_domain_v2():
    domain_count = collections.defaultdict(lambda: 0)
    with open('mails.txt', 'r') as f:
        text = f.readlines()
        for line in text:
            domain = line.split('@')[-1]
            domain_count[domain] += 1


def count_email_domain_v3():
    email_list = []
    with open('mails.txt', 'r') as f:
        text = f.read().split('\n')
        email_list.append(email for email in text)

    return email_list


if __name__ == '__main__':
    print(random_char(7) + '@gmail.com')
    prod_list_adding = []
    prod_list_added = []

    for button in buttons:
        prod_name = button.find_element_by_xpath("parent::div/parent::div/h4")
        # print(prod_name.text)
        prod_list_adding.append(prod_name.text)
        button.click()
