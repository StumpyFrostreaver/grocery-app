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
        if field is None or StringUtils.is_blank(field) or str(field).lower() == "none":
            field = ''
        csvified_field = str(field)
        csvified_field = csvified_field.replace('"', '""')
        csvified_field = csvified_field.replace('\n', ' ')
        csvified_field = f"\"{csvified_field}\""
        return csvified_field

    @staticmethod
    def decsvify_field(field):
        if field is None or StringUtils.is_blank(field) or str(field).lower() == "none":
            field = ''
        decsvified_field = str(field)
        decsvified_field = decsvified_field.strip()
        if decsvified_field.startswith('"') and decsvified_field.endswith('"'):
            decsvified_field = decsvified_field[1:-1].strip()
        return decsvified_field

