from improved import App, load_config, do_the_thing

load_config("config.txt")
do_the_thing()

bob_app = App('bobconfig.txt')
bob_app.do_the_thing()

do_the_thing()