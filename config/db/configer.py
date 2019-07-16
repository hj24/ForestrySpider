import configparser

config = configparser.ConfigParser()

config.read('./conf/info.ini')

sections = config.sections()

print(config.options(sections[0]))

item_list = config.items(sections[0])
print(item_list)

db_host = config.get(sections[0], 'host')
print(db_host)

db_post = config.getint(sections[0], 'port')
print(db_post)