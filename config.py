from typing import Any
import yaml

def load(value:any) -> any:
    with open('settings.yml') as f:
        config = yaml.safe_load(f)
        try:
            return_output = config.split(f'{value}:')[1]
            return return_output
        except IndexError:
            print(f'The value {value} is not found!')

def set_val(key:any, value:any) -> None:
    with open('settings.yml' , mode='a') as f:
        f.write(key+':'+value)

def delete(key:any, value:any):
    with open('settings.yml' , 'r') as f:
        new_value = f.read().replace(f'{key}:{value}' , '\n')
        with open('settings.yml' , 'w+') as f:
            f.write(new_value)