# Import Jinja2 library and PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml

# Declare template environment
ENV = Environment(loader=FileSystemLoader('/Users/richardt/src/projects/'))

def get_interface_speed(interface_name):
    """
    get_interface_speed returns the default Mbps value for a given
    network interface by looking for certain keywords in the name.
    also convert to lowercase and check for a string match on the description.
    """

    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

# Filters are added to the ENV object after declaration. Note that we're
# actually passing in our "get_interface_speed" function and not running
# it -- the template engine will execute this function when we call the 
# template.render()
ENV.filters['interface_speed'] = get_interface_speed
template = ENV.get_template('template2.j2') 

# We load our YAML file and pass it in to the template when rendering it. 
with open("data.yml") as file:   
    interfaces = yaml.load(file, Loader=yaml.FullLoader)  
    print(template.render(interface_list=interfaces))    
