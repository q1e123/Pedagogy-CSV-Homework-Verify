import csv
import pandas

class Homework():
    BAD_NAME_FILE_SUFIX = '-wrong-name.txt'
    CHECK_FILE_NAME = 'check.txt'
    FRAUD_MESSAGE = 'FRAUD'
    GOOD_MESSAGE = 'GOOD'
    WRONG_MESSAGE = 'WRONG'
    NOT_SENT_MESSAGE = 'NOT SENT'

    def __init__(self, title, student_list, path_list):
        self.title = title
        self.student_homework_map = dict.fromkeys(student_list)
        self.student_status_map = dict.fromkeys(student_list)
        self.bad_name_file_name = self.title + Homework.BAD_NAME_FILE_SUFIX
        self.dataset_list = []
        self.read_dataset(path_list)

    def read_dataset(self, path_list):
        for path in path_list:
            with open(path) as csv_file:
                lines = csv.reader(csv_file)
                line_list = [line for line in lines]
                self.dataset_list.append(line_list)

    def add_student_homework(self, student, solution):
        print(self.title, student, solution)
        if student not in student:
            with open(self.bad_name_file_name, 'a') as bad_name_file:
                bad_name_file.write(student)
            return
        try:
            with open(solution) as csv_file:
                lines = csv.reader(csv_file)
                line_list = [line for line in lines]
                if line_list in self.dataset_list:
                    self.student_status_map[student] = Homework.WRONG_MESSAGE
                    return
                if line_list in self.student_homework_map.values():
                    self.student_homework_map[student] = line_list
                    self.student_status_map[student] = Homework.FRAUD_MESSAGE
                    for student in self.student_homework_map:
                        if line_list == self.student_homework_map[student]:
                            self.student_homework_map[student] = line_list
                            self.student_status_map[student] = Homework.FRAUD_MESSAGE
                    return
            self.student_status_map[student] = Homework.GOOD_MESSAGE
            self.student_homework_map[student] = line_list
        except Exception as e:
            print(e)
            self.student_status_map[student] = Homework.WRONG_MESSAGE

    def check_not_sent(self):
        for student in self.student_status_map:
            if self.student_status_map[student] is None:
                self.student_status_map[student] = Homework.NOT_SENT_MESSAGE

    def to_csv(self):
        with open(self.title, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for student in self.student_status_map:
                writer.writerow([student, self.student_status_map[student]])
