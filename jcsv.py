import json
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
args = parser.add_argument('--file', required=True)

filename = args.file

def is_primitive(value):
    if type(value, int):
        return True
    elif type(value, float):
        return True
    elif type(value, str):
        return True
    elif type(value, bool):
        return True


def get_flat_list(keyname, arr):
    flat_list = {}

    for index, val in enumerate(arr):
        flat_list[f'{keyname}_{index}'] = val
    
    return flat_list


def is_just_a_list(arr):
    return is_primitive(arr[0])


def get_flat_mutli_dict(keyname, d):
    flat_dict = {}
    counter = 0

    for key, value in d.items():
        flat_dict[f'{keyname}_{key}_{counter}'] = value
        counter += 1

    return flat_dict
        


def get_flat_json(obj):
    res = {}

    for key, value in obj.items():
        if is_primitive(value):
            res[key] = value
        elif type(value, dict):
            res.update(value)
        elif type(value, list):
            if is_just_a_list(value):
                res.update(get_flat_list(value))
            else:
                res.update(get_flat_multi_dict(value))
        else:
            raise Exception("Custom classes are not supported!")

    df = pd.DataFrame(res)
    df.to_csv(f'{filename[:-5].csv', index=False)


if __name__ == '__main__':

    with open(filename, 'r') as f:
        json_file = json.loads(filename)

    get_flat_json(json_file)
