# A file to test functions & practice new skills

# from pathlib import Path

# FILE & FOLDER SECTION

# Rename CSV files according to parent folders
# folder = Path('2022')
# paths = folder.glob('**/*.csv')
#
# for path in paths:
#     print(list(path.parts))
#
#     date_list = list(path.parts)
#     new_name = path.stem
#     new_name = new_name + date_list[0] + (date_list[1])[3:] + (date_list[2])[4:] + ".csv"
#     new_path_name = path.with_name(new_name)
#     print(new_path_name)
#     path.rename(new_path_name)

# Change file types

# txt to csv
# folder = Path('2022')
# paths = folder.glob('**/*.txt')
#
# for path in paths:
#     new_name = path.stem
#     new_name += ".csv"
#     new_path_name = path.with_name(new_name)
#     print(type(new_path_name))
#     path.rename(new_path_name)
#
#
# # csv to txt
# paths = folder.glob('**/*.csv')
#
# for path in paths:
#     new_name = path.stem
#     new_name += ".txt"
#     new_path_name = path.with_name(new_name)
#     print(type(new_path_name))
#     path.rename(new_path_name)