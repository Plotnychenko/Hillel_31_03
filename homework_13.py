# Homework 13
# E. Plotnychenko

class FileWorker:
    def __init__(self, filename):
        self.filename = filename
        self.month_dict = {"January": "01",
                           "February": "02",
                           "March": "03",
                           "April": "04",
                           "May": "05",
                           "June": "06",
                           "July": "07",
                           "August": "08",
                           "September": "09",
                           "October": "10",
                           "November": "11",
                           "December": "12"
                           }
        self.format_domains_list = []
        self.surnames_list = []
        self.list_date_dict = {}
        self.file_reader()

    def file_reader(self):
        with open(self.filename, "r") as txt_files:
            return txt_files.readlines()

    def create_domains_list(self):
        domains_list = self.file_reader()
        format_domains_list = [value.lstrip(".") for value in domains_list]
        return format_domains_list

    def create_surnames_list(self):
        object_list = self.file_reader()
        strings_split_list = [my_str.split("\t") for my_str in object_list]
        self.surnames_list = [surname[1] for surname in strings_split_list]
        return self.surnames_list

    def create_date_original_list(self):
        info_list = self.file_reader()
        info_list = [value.split(" - ")[0].split() for value in info_list if " - " in value]
        date_original_list = [value for value in info_list if len(value) == 3]
        return date_original_list

    def modified_date(self, date):
        date[0] = date[0].rstrip("nsthrd")
        if len(date[0]) == 1:
            date[0] = "0" + date[0]
        date[1] = self.month_dict[date[1]]
        return "/".join(date)

    def create_list_date_dict(self):
        list_date_dict = []
        date_original_list = self.create_date_original_list()
        index = 0
        while index < len(date_original_list):
            original_date = " ".join(date_original_list[index])
            dict_date = {"data_original": original_date, "data_modified": self.modified_date(date_original_list[index])}
            list_date_dict.append(dict_date)
            index += 1
        return list_date_dict


author_worker = FileWorker("authors.txt")
list_data_dict = author_worker.create_list_date_dict()
domains_worker = FileWorker("domains.txt")
domains = domains_worker.create_domains_list()
names_worker = FileWorker("names.txt")
surnames = names_worker.create_surnames_list()
