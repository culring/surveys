import csv


class Model:
    def __init__(self, filename: str):
        with open(filename) as file:
            answers_reader = csv.reader(file, delimiter=',')
            for answers in answers_reader:
                print(answers)


if __name__ == '__main__':
    Model()
