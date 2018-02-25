import json
from os import path, getcwd


class Configuration:
    config_file_path = None
    options = None

    def __init__(self, config_file_path=None):
        self._find_config(config_file_path)
        self._parse_options()

    def __repr__(self):
        return "Config File: {0}\nOptions: {1}".format(self.config_file_path, self.options)

    def _find_config(self, config_file_path):
        if config_file_path:
            self.config_file_path = config_file_path
        else:
            self.config_file_path = path.join(
                getcwd(), "configuration/configuration.json")
        if not path.exists(self.config_file_path):
            raise Exception("Failed to find configuration file at: {0}.".format(self.config_file_path))

    def _parse_options(self):
        options = list()
        with open(self.config_file_path, 'r') as config_file:
            config = json.load(config_file)
        for opt in config["options"]:
            commands = list()
            for com in opt["commands"]:
                commands.append(
                    Command(
                        com["input-options"],
                        com["output-options"],
                        com["output-extension"]
                    ))
            option = Option(
                opt["name"],
                opt["valid-input-extensions"],
                commands
            )
            options.append(option)
        self.options = options


class Option:
    name = None
    valid_input_exts = None
    commands = None

    def __init__(self, name, valid_input_exts, commands):
        self.name = name
        self.valid_input_exts = valid_input_exts
        self.commands = commands

    def __repr__(self):
        return "Name: {0} | Valid Input Exts: {1}\nCommands: {2}".format(self.name, self.valid_input_exts, self.commands)

class Command:
    input_options = None
    output_options = None
    output_extension = None

    def __init__(self, input_options, output_options, output_extension):
        self.input_options = input_options
        self.output_options = output_options
        self.output_extension = output_extension

    def __repr__(self):
        return "Input Opts: {0} | Output Opts: {1} | Output Ext: {2}\n".format(self.input_options, self.output_options, self.output_extension)
