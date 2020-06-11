#!/usr/bin/python
#_*_ coding: iso-8859-15 _*_
#autor: Jefferson

from difflib import SequenceMatcher
import os
import csv
import os.path
import shutil
import fnmatch
import sys
import time

def find(file_name, path):
    # This function looks for a file (file_name param) within a directory
    result = find_file_bypattern(file_name, path)
    return [] if result == [] else result[0]

def find_file_bypattern(pattern, path):
    result = []
    # pylint: disable=W0612
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def run(seed1, seed2, output):
    # verificar se tem um arquivo shell.js para não executar, ele n serve
    arquivos_origem = find_file_bypattern('*.js', f'seeds/{seed1}/')
    detections = find_file_bypattern('*.js', f'seeds/{seed2}/')
    tam1 = len(arquivos_origem)
    tam2 = len(detections)
    for index, origin_path in enumerate(arquivos_origem):
        if origin_path.endswith('shell.js'):
            continue 
        lista = []
        with open(origin_path, encoding='utf-8', errors='ignore') as doc1:
            doc1 = doc1.read()
        for index_2, eachObject_path in enumerate(detections):
            if eachObject_path.endswith('shell.js'):
                continue
            print(f"comparando arquivo da seed do {seed1} com {seed2}")
            print(f"{seed1}: {index} de {tam1} - {seed2}: {index_2} de {tam2}")
            with open(eachObject_path, encoding='utf-8', errors='ignore') as doc2:
                doc2 = doc2.read()

            similarity = similar(doc1, doc2)
            if (similarity >= 0.95):
                lista.append(
                    {
                        "File1": origin_path,
                        "File2": eachObject_path,
                        "Similarity": similarity
                    }
                )

                # print(f"arquivo: {index} de {index_2}: {similarity}")
        with open(f'{output}.csv', 'a+', newline='') as file:
            # writer = csv.writer(file)
            fieldnames = ["File1", "File2", "Similarity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            #writer.writeheader()
            for arquivo in lista:
                writer.writerow(arquivo)
        print("--- ok ---")

if __name__ == "__main__":
    seeds = [
        'JSI', 'DukTape', 'TinyJS', 'hermes', 'JerryJS', 'WebKit', 'test262', 'mozilla', 'v8', 
    ]
    t_init = time.time()
    for i in range(len(seeds)):
        run(seeds[i], seeds[i+1], time.asctime())
        with open('time_spent.log', 'a+') as doc:
            doc.write(f'{time.time() - t_init}')