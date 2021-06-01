# Homework 13
# E. Plotnychenko

class FileWorker:
    def __init__(self, authors, domains, names):
        self._authors = self.file_reader(authors)
        self._domains = self.file_reader(domains)
        self._names = self.file_reader(names)
        self._month_dict = {"January": "01",
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
        self._surnames_list = []

    def file_reader(self, filename):
        with open(filename, "r") as txt_files:
            return txt_files.readlines()

    @property
    def domains_list(self):
        format_domains_list = [value.lstrip(".") for value in self._domains]
        return format_domains_list

    @property
    def surnames_list(self):
        strings_split_list = [my_str.split("\t") for my_str in self._names]
        self._surnames_list = [surname[1] for surname in strings_split_list]
        return self._surnames_list

    def _create_date_original_list(self):
        info_list = [value.split(" - ")[0].split() for value in self._authors if " - " in value]
        _date_original_list = [value for value in info_list if len(value) == 3]
        return _date_original_list

    def _modified_date(self, date):
        date[0] = date[0].rstrip("nsthrd")
        if len(date[0]) == 1:
            date[0] = "0" + date[0]
        date[1] = self._month_dict[date[1]]
        return "/".join(date)

    @property
    def list_date_dict(self):
        _list_date_dict = []
        date_original_list = self._create_date_original_list()
        index = 0
        while index < len(date_original_list):
            original_date = " ".join(date_original_list[index])
            dict_date = {"data_original": original_date, "data_modified": self._modified_date(date_original_list[index])}
            _list_date_dict.append(dict_date)
            index += 1
        return _list_date_dict


file_worker = FileWorker("authors.txt", "domains.txt", "names.txt")
print(file_worker.surnames_list)
print(file_worker.list_date_dict)
print(file_worker.domains_list)