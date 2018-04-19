import course

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='Geometry Honors',
                  teacher_name='Ms. Lee',
                  resource_name='Pearson Realize',
                  resource_url='https://www.pearsonrealize.com'),
    course.Course(period=3,
                  name='Geometry Honors',
                  teacher_name='Ms. Lee',
                  resource_name='MathXLforSchool',
                  resource_url='http://www.mathxlforschool.com/'),
    course.Course(period=4,
                  name='Geometry',
                  teacher_name='Ms. Lee',
                  resource_name='Interactive simulations',
                  resource_url='https://www.desmos.com'),
    course.Course(period=5,
                  name='Prep',
                  teacher_name='Ms. Lee',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/math/geometry'),
    course.Course(period=6,
                  name='EL Geometry',
                  teacher_name='Ms. Lee',
                  resource_name='Pearson Realize',
                  resource_url='https://www.pearsonrealize.com'),
]
