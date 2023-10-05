from connection import create_connection
from random import randint, choice, sample
from faker import Faker
from datetime import datetime

gr = ["101", "201", "301"]
subj = [
    "English",
    "IT",
    "Economics",
    "Marketing",
    "Management",
    "Finance",
    "Art",
    "Alchemy",
]

sql_commands = {
    "ins_groups": "INSERT INTO groups(name) VALUES(?)",
    "ins_students": "INSERT INTO students(name, group_id) VALUES(?, ?)",
    "ins_teachers": "INSERT INTO teachers(name) VALUES(?)",
    "ins_subjects": "INSERT INTO subjects(name, teacher_id) VALUES(?, ?)",
    "ins_grades": "INSERT INTO grades(student_id, subject_id, grade, date_received) VALUES(?, ?, ?, ?)",
}

fake = Faker()
current_year = datetime.now().year


def insert_sql():
    num_groups = 0
    num_students = 0
    num_teachers = 0
    num_subjects = 0
    num_grades = 0

    with create_connection() as cur:
        try:
            for operation in [
                "ins_groups",
                "ins_students",
                "ins_teachers",
                "ins_subjects",
                "ins_grades",
            ]:
                command = sql_commands.get(operation)
                if command:
                    match operation:
                        case "ins_groups":
                            for g in gr:
                                cur.execute(command, (g,))
                                num_groups += 1
                        case "ins_students":
                            for _ in range(randint(30, 50)):
                                group_id = choice(range(1, len(gr) + 1))
                                cur.execute(command, (fake.name(), group_id))
                                num_students += 1
                        case "ins_teachers":
                            for _ in range(randint(3, 5)):
                                teacher_name = fake.name()
                                cur.execute(command, (teacher_name,))
                                num_teachers += 1
                        case "ins_subjects":
                            list_subj = sample(subj, k=randint(5, 8))
                            for sub in list_subj:
                                teacher_id = choice(range(1, num_teachers + 1))
                                cur.execute(command, (sub, teacher_id))
                                num_subjects += 1
                        case "ins_grades":
                            for student_id in range(1, num_students + 1):
                                dates = set()
                                subject_ids = sample(
                                    range(1, num_subjects + 1), k=min(num_subjects, 20)
                                )  # limit to max 20 subjects
                                for subject_id in subject_ids:
                                    date_received = None
                                    while (
                                        date_received is None or date_received in dates
                                    ):
                                        date_received = fake.date_between_dates(
                                            date_start=datetime(current_year, 1, 1),
                                            date_end=datetime(current_year, 9, 30),
                                        )
                                    dates.add(date_received)
                                    grade_value = randint(1, 5)
                                    cur.execute(
                                        command,
                                        (
                                            student_id,
                                            subject_id,
                                            grade_value,
                                            date_received,
                                        ),
                                    )
                                    num_grades += 1

        except Exception as e:
            print(e)

    print(
        f"\nStuds: {num_students}, Groups: {num_groups}, Teach: {num_teachers}, Subj: {num_subjects}, Grades: {num_grades}"
    )


if __name__ == "__main__":
    insert_sql()
