import argparse
import json


def _print_entry(entry):
    print(entry['title'])


def _print_where_email_is_login(_json):
    print('Email is Login:')

    count = 0
    for entry in _json['AUTHENTIFIANT']:
        login = entry['login']
        secondary_login = entry['secondaryLogin']
        if (isinstance(login, str) and '@' in login) or (isinstance(secondary_login, str) and '@' in secondary_login):
            _print_entry(entry)

            count += 1

    print('Total: {}'.format(count))


def _print_where_no_domain(_json):
    print('No Domain:')

    count = 0
    for entry in _json['AUTHENTIFIANT']:
        domain = entry['domain']

        if not isinstance(domain, str) or domain.strip() == '':
            _print_entry(entry)

            count += 1

    print('Total: {}'.format(count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('json_file')
    parser.add_argument('-e', '--email-as-login', action='store_true')
    parser.add_argument('-d', '--no-domain', action='store_true')

    args = parser.parse_args()

    _json = None
    with open(args.json_file, 'r') as f:
        _json = json.load(f)

    if args.email_as_login:
        _print_where_email_is_login(_json)

    if args.no_domain:
        _print_where_no_domain(_json)


if __name__ == '__main__':
    main()
