from file_finder import FileFinder
from menu import Menu

class Converto:
    menu_options = list()
    config = None
    main_menu = None
    chosen_option = None
    user_input = None

    def __init__(self, config, user_input):
        self.config = config
        self.input = user_input
        self.show_main_menu()

    def _convert(self, files):
        print "Converting files..."

    def show_main_menu(self):
        menu_options = self._generate_menu_options()
        self.main_menu = Menu(title = "Choose which command you would like to run")
        self.main_menu.set_options(menu_options)
        self.main_menu.open()

    def _find_files_and_convert(self, option_index):
        self.main_menu.close()
        self.chosen_option = self.config.options[option_index]
        print "You chose {0}".format(self.chosen_option.name)
        file_finder = FileFinder(self.chosen_option, self.user_input)
        self._convert(file_finder.files)

    def _generate_menu_options(self):
        menu_options = list()
        for i, opt in enumerate(self.config.options):
            menu_options.append((opt.name, lambda i=i: self._find_files_and_convert(i)))
        return menu_options