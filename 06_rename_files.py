import os

os.chdir('/home/filip/Programming/Courses/Python_useful/rename_files')
# printing working directory
# print(os.getcwd())
# printing a list of files in directory
# print(os.listdir())

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    file_course, file_planet, file_num = file_name.split('-')
    # strip white spaces and #. zfill will add zero at the beginning
    file_num = file_num.strip()[1:].zfill(2)
    file_course = file_course.strip()
    file_planet = file_planet.strip()
    # print(file_course, file_planet, file_num)
    pattern = f'{file_num}-{file_course}-{file_planet}'

    os.rename(file, pattern)
    print(file)