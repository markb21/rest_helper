"""Mark Budiak.

Usage:
  rest_helper.py (-n=<NUM> | --num=<NUM>)  (-c=<FILE> | --config=<FILE>)
  rest_helper.py (-h | --help)
  rest_helper.py --version

Options:
  -n=NUM --num=NUM      Specify the number of urls to parse
  -c=FILE --config=FILE   Specify the path to config file
  -h --help     Show this help.
  --version     Show version.

"""
from docopt import docopt
import configparser
import re
import os


def parse_config_file(num, file):
    if not os.path.isfile(file):
        print('Config file does not exist')
        return

    config = configparser.ConfigParser()
    config.read(file)
    try:
        username = config['Data']['username']
        url_path = config['Data']['urlpath']
    except KeyError as e:
        print('The configuration file is malformed - missing key ' + str(e))
        return

    try:
        for n in range(1, min(int(num), len(config['Urls'])) + 1):
            if 'Url'+str(n) not in config['Urls']:
                break
            else:
                url = config['Urls']['Url'+str(n)]
                url_splits = re.search(r'^(https?://)(.*)$', url).groups()
                print(url_splits[0] + username + '@' + url_splits[1] + url_path)
    except KeyError as e:
        print('The configuration file is malformed - missing key ' + str(e))
        return


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    parse_config_file(arguments['--num'], arguments['--config'])