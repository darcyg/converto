from __future__ import print_function
from file_finder import FileFinder
from menu import Menu
from ffmpy import FFmpeg
from os import path, remove


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

    def show_main_menu(self):
        menu_options = self._generate_menu_options()
        self.main_menu = Menu(
            title="Choose which command you would like to run")
        self.main_menu.set_options(menu_options)
        self.main_menu.open()

    def _convert(self):
        for f in self.files:
            for i, command in enumerate(self.chosen_option.commands):
                input_file, was_intermediate = self._get_file_to_operate_on(
                    f, i)
                ff = self._build_ffmpeg_command(input_file, i)
                ff.run()
                if was_intermediate:
                    remove(previous_intermediary_file)
                if self.chosen_option.multi_input:
                    return

    def _get_file_to_operate_on(self, input_file, i):
        previous_intermediary_file = self._get_output_filename(input_file, (i - 1))
        if path.isfile(previous_intermediary_file):
            return previous_intermediary_file, True
        else:
            return input_file, False

    def _build_ffmpeg_command(self, input_file, command_index):
        command = self.chosen_option.commands[command_index]
        output_filename = self._get_output_filename(input_file, command_index)
        if self.chosen_option.multi_input:
            inputs = {}
            for f in self.files:
                inputs[f] = command.input_options
        else:
            inputs = {input_file: command.input_options}
        outputs = {output_filename: command.output_options}

        ff = FFmpeg(
            inputs=inputs,
            outputs=outputs
        )
        return ff

    def _get_output_filename(self, filename, command_index):
        command = self.chosen_option.commands[command_index]
        if self._is_intermediary(command_index):
            output_filename = "{0}_INTERMEDIARY_{1}.{2}".format(
                filename[:-4], command_index, command.output_extension)
        elif command.output_filename_format:
            output_filename = command.output_filename_format.format(
                input_filename=filename, extension=command.output_extension)
        else:
            output_filename = "{0}.{1}".format(
                filename[:-4], command.output_extension)
        return output_filename

    def _is_intermediary(self, index):
        return index != len(self.chosen_option.commands) - 1

    def _generate_menu_options(self):
        menu_options = list()
        for i, opt in enumerate(self.config.options):
            menu_options.append(
                (opt.name, lambda i=i: self._find_files_and_convert(i)))
        return menu_options

    def _find_files_and_convert(self, option_index):
        self.main_menu.close()
        self.chosen_option = self.config.options[option_index]
        print("You chose \"{0}\"\n".format(self.chosen_option.name))
        file_finder = FileFinder(self.chosen_option, self.user_input)
        file_finder.get_user_input()
        self.files = file_finder.files
        self._ask_if_commands_look_right()

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
            ("Yes, process the files now",
             lambda: self._handle_user_satisfaction_choice(True)),
            ("No, cancel", lambda: self._handle_user_satisfaction_choice(False)),
        ])
        self.satisfied_menu.open()

    def _handle_user_satisfaction_choice(self, satisified):
        self.satisfied_menu.close()
        if satisified:
            self._convert()
        else:
            exit(0)
