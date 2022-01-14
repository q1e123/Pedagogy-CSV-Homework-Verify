import os

import pandas

from Homework import Homework

def get_files_from_directory(directory_path):
    file_list = []
    for filename in os.listdir(directory_path):
        path = os.path.join(directory_path, filename)
        # checking if it is a file
        if os.path.isfile(path):
            file_list.append(path)
    return file_list

def get_dataset_list(dataset_file_list):
    dataset_list = []
    for file in dataset_file_list:
        dataset = pandas.read_csv(file)
        dataset_list.append(dataset)
    return  dataset_list

def get_student_list(student_file_path):
    student_list = []
    with open(student_file_path) as student_file:
        student_list = student_file.readlines()
    student_list = [s.replace("\n", "") for s in student_list]
    return student_list

def verify_homeworks(homework_directory_path, student_list):
    homework_list = []
    dataset_list = get_files_from_directory('Datasets')
    for homework_title in os.listdir(homework_directory_path):
        homework = Homework(homework_title, student_list, dataset_list)
        homework_path = os.path.join(homework_directory_path, homework_title)
        solution_list = get_files_from_directory(homework_path)
        for solution in solution_list:
            solution_name = solution.split('\\')[-1]
            student = solution_name[:-4]
            homework.add_student_homework(student, solution)
        homework.check_not_sent()
        homework.to_csv()

homework_directory_path = "Homeworks"
student_list = get_student_list('students.txt')
verify_homeworks(homework_directory_path, student_list)