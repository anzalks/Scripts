#!/Users/anzalks/miniconda/bin/python3 
import shutil
from pathlib import Path

file_paths = Path("/Users/anzalks/Documents/Expt_data/trail_copy_py/2021_12_16/")
fetch_file=Path("/Users/anzalks/Documents/"
                "Expt_data/trail_copy_py/experiment_parameters_2021_12_16.py")

def list_files(file_paths):
    f_list = []
    f_list=list(file_paths.glob('**/*abf'))
    return f_list

file_list = list_files(file_paths)

for file in file_list:
    x = str(file).split('.')[0]+'_experiment_parameters.py'
    shutil.copy2(fetch_file,x)
print("all done")
#    print(fetch_file)

#print(f"all done:{shutil}")
#x = [path(f).abspath() for f in glob(f"{file_path}*.txt")]
#org_path = r''
#targ_path = r''
#shutil.copy(org_path,target_path)

