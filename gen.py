import pyperclip
import csv
from random import choice as grand
import json

class ReviewTemplate:
    
    def __init__(self, template, marks_case, class_case, home_case, discipline_case) -> None:
        self.template = template
        self.marks_case = marks_case
        self.class_case = class_case
        self.home_case = home_case
        self.discipline_case = discipline_case
        
class Review:
    
    def __init__(self, words: dict, template: ReviewTemplate, fields = list()) -> None:
        self.template = template
        self.fields = fields
        self.words = words
        
    def set_word(self, field, case):
        self.fields[field] = grand(self.words[self.fields[field]])[case]
        
    def __str__(self) -> str:
        self.set_word("marks", self.template.marks_case)
        self.set_word("work_home", self.template.home_case)
        self.set_word("work_class", self.template.class_case)
        self.set_word("discipline", self.template.discipline_case)
        return self.template.template.format_map(self.fields)
        

def read_words_dict(filename: str) -> dict:
    mark2word = dict()

    with open(filename, "r", encoding='utf-8') as words:
        dr = csv.DictReader(words)
        for row in dr:
            mark2word.setdefault(row["MARK"],list())
            mark2word[row["MARK"]].append(row)

    return mark2word
    

def read_templates(filename: str) -> list:
    templates = []
    with open(filename, "r") as templates_file:
        res = json.load(templates_file)
        for template in res:
            text = template["template"]
            mc = template["marks_case"]
            cc = template["class_case"]
            hc = template["home_case"]
            dc = template["discipline_case"]
            templates.append(ReviewTemplate(text, mc, cc, hc, dc))
    return templates
        
def ask_fields():
    
    fields = {
        "name":"",
        "marks":1,
        "discipline":0,
        "work_class":0,
        "work_home":0,
        "qualities":"",
        "additional":""
    }
    fields["name"] = input("Имя: ")
    fields["marks"] = str(int(input("Успеваемость (1-5): ")))
    fields["discipline"] = str(int(input("Дисциплина (1-5): ")))
    fields["work_class"] = str(int(input("Работа в классе (1-5): ")))
    fields["work_home"] = str(int(input("Работа дома (1-5): ")))
    fields["qualities"] = input("Особые качества (В.П.): ")
    fields["additional"] = " " + input("Дополнительный комментарий: ")
    return fields
