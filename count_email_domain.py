import random
import string
import pdb; pdb.set_trace()
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

def count_email_domain_v2():
    domain_count = collections.defaultdict(lambda: 0)
    with open('mails.txt', 'r') as f:
        text = f.readlines()
        for line in text:
            domain = line.split('@')[-1]
            domain_count[domain] += 1

def count_email_domain_v3():
    with open('mails.txt', 'r') as f:
        text = f.read().split('\n')
        l = []

if __name__ == '__main__':
    print(random_char(7) + '@gmail.com')


