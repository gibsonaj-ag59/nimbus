class Normalizer():
    def __init__(self, app):
        self.replace_dict = app.config.get("REPLACE_DICT", {" ": "_"})

    def normalize_header(self, heading):
        column_names = heading.split(',')
        for key, value in self.replace_dict.items():
            column_names = [name.replace(key, value) for name in column_names]  
    
    def normalize_row(self, row):
        for key, value in self.replace_dict.items():
            row = [cell.replace(key, value) for cell in row]
        return row