

class ConfigPropertyInvalid(Exception):
    def __init__(self, section: object, key, *args):
        super(ConfigPropertyInvalid, self).__init__(args)
        self._section = section
        self._key = key

    def __repr__(self):
        return f'Config section "{self._section}" or "{self._key}" not allowed'
