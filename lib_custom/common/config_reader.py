try:
    import configparser
except:
    from six.moves import configparser


class ConfigReader:

    def __init__(self, **kwargs):
        self._config_file_path = kwargs['config_file_path']
        self.config = configparser.ConfigParser()
        self.config.read(self._config_file_path)

    def get_configuration(self):
        return self.config

    def get_conf_file_location(self):
        return self._config_file_path

    def check_section_exists(self, section, new_key,  new_value):
        if not self.config.has_section(section):
           self.config.add_section(section)
        self.config.set(section, new_key, new_value)

    def save_configuration_file(self, file_path):
        self.config.write(open(file_path, 'w'))

    def add_configuration(self, section, new_key,  new_value):
        self.check_section_exists(section, new_key, new_value)
        self.save_configuration_file(self._config_file_path)