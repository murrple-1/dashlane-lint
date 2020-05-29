import argparse
import json


def _print_entry(entry, with_domain=False):
    if not with_domain:
        print(entry['title'])
    else:
        print(entry['title'], '|', entry['domain'])


def _print_where_email_is_login(json_):
    print('Email is Login:')

    count = 0
    for entry in json_['AUTHENTIFIANT']:
        login = entry['login']
        secondary_login = entry['secondaryLogin']
        if (type(login) is str and '@' in login) or (type(secondary_login) is str and '@' in secondary_login):
            _print_entry(entry)

            count += 1

    print(f'Total: {count}')


def _print_where_no_domain(json_):
    print('Note: lack of domain does not necessarily mean the domain isn\'t set...')
    print('No Domain:')

    count = 0
    for entry in json_['AUTHENTIFIANT']:
        domain = entry['domain']

        if type(domain) is not str or domain.strip() == '':
            _print_entry(entry)

            count += 1

    print(f'Total: {count}')


def _print_where_domain(json_):
    print('Domain:')

    count = 0
    for entry in json_['AUTHENTIFIANT']:
        domain = entry['domain']

        if type(domain) is str and domain != '':
            _print_entry(entry, True)

            count += 1

    print(f'Total: {count}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('json_file')
    parser.add_argument('-e', '--email-as-login', action='store_true')
    parser.add_argument('-d', '--no-domain', action='store_true')
    parser.add_argument('-D', '--good-domain', action='store_true')

    args = parser.parse_args()

    json_ = None
    with open(args.json_file, 'r') as f:
        json_ = json.load(f)

    if args.email_as_login:
        _print_where_email_is_login(json_)

    if args.no_domain:
        _print_where_no_domain(json_)

    if args.good_domain:
        _print_where_domain(json_)


if __name__ == '__main__':
    main()
