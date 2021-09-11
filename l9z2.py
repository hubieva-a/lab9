import json

if __name__ == '__main__':

    students_list = []
    while True:
        command = input("Add, list, exit, load <>, save <>: ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            last_name = input('Your last name^ ')
            class_name = input('Class ')
            grades = []
            n = 0
            while n < 5:
                grades.append(int(input('Your grades ')))
                n += 1

            student = {
                'Last name': last_name,
                'Class': class_name,
                'Grades': grades,
            }
            students_list.append(student)
            if len(students_list) > 1:
                students_list.sort(key=lambda item: item.get('Last name', ''))

            print(students_list)

        elif command == 'list':
            count = 0
            for student in students_list:
                for i in student['Grades']:
                    if i == 2:
                        count += 1
                        print('{:>4}: {}'.format('This student got an F', student.get('Last name', '')))

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                data = json.load(f)
                print(data)


        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(students_list, f)

















