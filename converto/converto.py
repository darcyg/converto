from file_finder import FileFinder
from menu import Menu
from ffmpy import FFmpeg


class Converto:
    menu_options = list()
    files = list()
    config = None
    main_menu = None
    satisfied_menu = None
    chosen_option = None
    user_input = None

    def __init__(self, config, user_input):
        self.config = config
        self.input = user_input
        self.show_main_menu()

    def _convert(self):
        print "Converting files..."
        for f in self.files:
            for i, command in enumerate(self.chosen_option.commands):
                input_file = f
                is_intermediary = (i != len(self.chosen_option.commands))

                if is_intermediary:
                    pass
                    #check for _INTERMEDIARY_i-1, and make that the input_file if it exists
                    #outputfilename = _INTERMEDIARY_i
                    #run command
                    #remove intermediary

                output_filename = self._get_output_filename(f, command)
                ff = FFmpeg(
                    inputs={input_file: command.input_options},
                    outputs={output_filename: command.output_options}
                )
                print "Executing: {0}".format(ff.cmd)
                ff.run()

    def _ask_if_commands_look_right(self):
        command_list = ""
        for command in self.chosen_option.commands:
            ff = FFmpeg(
                inputs={"{input_filename}": command.input_options},
                outputs={"{output_filename}": command.output_options}
            )
            command_list = command_list + ff.cmd + "\n"
        menu_title = "About to process these files: {0}\nUsing these commands:\n{1}\n\nDoes this look right?".format(
            self.files, command_list)
        self.satisfied_menu = Menu(title=menu_title)
        self.satisfied_menu.set_options([
            ("Yes, process the files now", lambda: self._handle_user_satisfaction_choice(True)),
            ("No, cancel", lambda: self._handle_user_satisfaction_choice(False)),
        ])
        self.satisfied_menu.open()

    def _handle_user_satisfaction_choice(self, satisified):
        if satisified:
            self.satisfied_menu.close()
            self._convert()
        else:
            exit(0)

    def show_main_menu(self):
        menu_options = self._generate_menu_options()
        self.main_menu = Menu(
            title="Choose which command you would like to run")
        self.main_menu.set_options(menu_options)
        self.main_menu.open()

    def _generate_menu_options(self):
        menu_options = list()
        for i, opt in enumerate(self.config.options):
            menu_options.append(
                (opt.name, lambda i=i: self._find_files_and_convert(i)))
        return menu_options

    def _find_files_and_convert(self, option_index):
        self.main_menu.close()
        self.chosen_option = self.config.options[option_index]
        print "You chose \"{0}\"\n".format(self.chosen_option.name)
        file_finder = FileFinder(self.chosen_option, self.user_input)
        self.files = file_finder.files
        print self.files
        self._ask_if_commands_look_right()

    def _get_output_filename(self, filename, command):
        output_filename = filename[:-4] + command.output_extension
        return output_filename
