import configparser


def open_conf_file():
    conf_file = "./config.ini"
    config = configparser.ConfigParser()
    config.read(conf_file)
    return config