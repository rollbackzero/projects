# Import Jinja2 library and PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml

# Declare template environment
ENV = Environment(loader=FileSystemLoader('/Users/richardt/src/projects/'))

def get_interface_speed(interface_name):
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

ENV.filters['interface_speed'] = get_interface_speed
template = ENV.get_template('template2.j2') 

# We load our YAML file and pass it in to the template when rendering it. 
with open("data.yml") as file:   
    interfaces = yaml.load(file, Loader=yaml.FullLoader)  
    print(template.render(interface_list=interfaces))    
