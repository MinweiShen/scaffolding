from config_parser import ConfigParser

if __name__ == '__main__':
    config = ConfigParser('templates/python/context.txt')
    print config.parse()
