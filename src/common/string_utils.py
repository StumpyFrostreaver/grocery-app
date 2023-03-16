class StringUtils:
    @staticmethod
    def is_blank(string):
        if string is None:
            string = ''
        string = str(string)
        if len(string.strip()) == 0:
            return True
        return False

    @staticmethod
    def is_something(string):
        return not StringUtils.is_blank(string)

    @staticmethod
    def csvify_field(field):
        csvified_field = field
        csvified_field = f"\"{csvified_field}\""
        return csvified_field
