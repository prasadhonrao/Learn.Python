import csv
import math
import pandas as pd
import operator
import os
from os.path import join, getsize
from xml.etree import ElementTree as ET
import time
from copy import deepcopy

root_directory = '' 
directory_rows = []
dependency_rows = []
springboot_files_rows = []
angular_component_files_rows = []
angular_service_files_rows = []



directory_row = ''
springboot_file_row = ''
directory_analysis_col_names =  ['Folder', 'Sub-Folder Count', 'File Count', 'Folder Size', 'Largest File', 'Largest File Size']
dependency_analysis_col_names =  ['FileName', 'GroupId', 'ArtifactId']
springboot_files_col_names = ['Path', 'FileName']
angular_component_col_names = ['FilePath', 'AngularComponentFileName']
angular_service_col_names = ['FilePath', 'AngularServiceFileName']


def analyze(root):
    print('analysis started...')
    for path, dirs, files in os.walk(root, topdown=True):

        # Handle exclude directory and files condition
        analyze_dirs_files(path, dirs, files)

        # Dependency xml search
        analyze_dependency(deepcopy(path),deepcopy(dirs),deepcopy(files))

        # '@Component' text search
        analyze_angular_component(deepcopy(path),deepcopy(dirs),deepcopy(files))

        # '@Injectable' text search
        analyze_angular_service(deepcopy(path),deepcopy(dirs),deepcopy(files))

        # '@Springboot' text search
        analyze_springbootapp(path,dirs,files)

    # Write to CSV
    write_to_csv(directory_rows, 'directory-analysis.csv', directory_analysis_col_names)
    write_to_csv(dependency_rows, 'dependency-analysis.csv', dependency_analysis_col_names)
    print "dependency-analysis count: ", len(dependency_rows)
    write_to_csv(springboot_files_rows, 'springboot-analysis.csv', springboot_files_col_names)
    print "@SpringbootFiles Count: " , len(springboot_files_rows)
    write_to_csv(angular_component_files_rows, 'AngularComponent-analysis.csv', angular_component_col_names)
    print "@Component File Count: " , len(angular_component_files_rows)
    write_to_csv(angular_service_files_rows, 'AngularService-analysis.csv', angular_service_col_names)
    print "@Injectable File Count: " , len(angular_service_files_rows)


def analyze_dirs_files(path, dirs, files):
    #directory_rows.clear()
    exclude_directories = set(['node_modules', 'bin', '.git',  'obj'])
    exclude_file_extensions = set(['.dll', '.exe',  '.jar','.jpg', '.log', '.md', '.old', '.pdf', '.png', '.svg', '.txt', '.yaml', '.yml', '.yaml.txt'])
    exclude_file_name = set(['.classpath', '.factorypath', '.gitignore', 'package.json', 'package-lock.json', '.project'])

    # handle exclude directory and files condition
    dirs[:] = [d for d in dirs if d not in exclude_directories]
    files[:] = [f for f in files if os.path.splitext(f)[1] not in exclude_file_extensions]
    files[:] = [f for f in files if f not in exclude_file_name]
    if len(files) == 0:
        return
    d = dict((getsize(join(path, name)),name) for name in files)
    if len(d.items()) == 0: # handle error condition when input element is empty
        return
    max_size,file_name = max(d.items(), key=operator.itemgetter(0))
    directory_row = [path , str(len(dirs)) , str(len(files)) , str(convert_size(sum(getsize(join(path, name)) for name in files))) , file_name , str(convert_size(max_size))]
    directory_rows.append(directory_row)

def analyze_dependency(path_dep,dirs_dep,files_dep):
    file_name = ['pom.xml']
    row = ''
    rows = []
    try:
        files_dep[:] = [f for f in files_dep if f in file_name] # exclude other files
        if len(files_dep) == 0:
            return rows
        it = ET.iterparse(path_dep +'\\' + 'pom.xml')

        for _, el in it:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
        root = it.root
        for p in root.findall('.//dependency'):
            row = [path_dep, p.find('groupId').text, p.find('artifactId').text]
            rows.append(row)

        if len(rows) > 0:
            dependency_rows.extend(rows)
    except Exception as ex:
        print("error")
        #print(ex.args)
        #print(ex.message)



def analyze_springbootapp(path,dirs,files):
    # Get Java Code files
    files[:] = [f for f in files if os.path.splitext(f)[1]  in set(['.java']) and '@SpringBootApplication' in open(path + '\\'+ f, 'r').read()]
    rows = []
    if len(files) > 0:
        for file in files:
            rows = [path , file]
            if(rows > 0):
                springboot_files_rows.append(rows)


def analyze_angular_component(path,dirs,files):

    files[:] = [f for f in files if os.path.splitext(f)[1]  in set(['.ts']) and '@Component' in open(path + '\\'+ f, 'r').read()]
    rows = []
    if len(files) > 0:
        for file in files:
            rows = [path , file]
            if(rows > 0) or ( len(rows) > 0):
                angular_component_files_rows.append(rows)


def analyze_angular_service(path,dirs,files):

    files[:] = [f for f in files if os.path.splitext(f)[1]  in set(['.ts']) and '@Injectable' in open(path + '\\'+ f, 'r').read()]
    rows = []
    if len(files) > 0:
        for file in files:
            rows = [path , file]
            if(rows > 0):
                angular_service_files_rows.append(rows)


def write_to_csv(collection, name, cols):
    if os.path.exists(name):
        os.remove(name)

    df = pd.DataFrame(collection, columns = cols)
    df.to_csv(name, header=True, index=False )

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def main():
    start_time = time.time()
    analyze(root_directory)
    elapsed_time = time.time() - start_time
    print("Script Execution Time: ", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


main()
