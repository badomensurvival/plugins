import yaml
from os import walk

path_read = './jobsbase'
path_write = './jobs'

filenames = next(walk(path_read), (None, None, []))[2]  # [] if no file

mapps = {
    "brewer.yml": ['Brew'],
    "builder.yml": ['Place', 'Kill'],
    "crafter.yml": ['Craft','Smelt'],
    "digger.yml": ['Break'],
    "enchanter.yml": ['Enchant'],
    "explorer.yml": ['Explore'],
    "farmer.yml": ['Tame','Breed','Shear','Milk','Break','Place'],
    "fisherman.yml": ['Fish'],
    "hunter.yml": ['Tame', 'Kill'],
    "miner.yml": ['TNTBreak','Break','Place'],
    "woodcutter.yml": ['Break', 'Kill'],
    "weaponsmith.yml": ['Craft','Repair','Smelt'],
}

factor = 0.25

for f in filenames:
    with open(f'{path_read}/{f}') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        job = yaml.load(file, Loader=yaml.FullLoader)
        
        f_item = list(job.keys())[0]

        for t in job[f_item].keys():
            if f in mapps and t in mapps[f]:
                for k in job[f_item][t].keys(): 
                    job[f_item][t][k]['income'] = float("{:.2f}".format(job[f_item][t][k]['income'] * factor))

        yaml.dump(job, sort_keys=True)

        with open(f'{path_write}/{f}', 'w') as write:
            yaml.dump(job, write)
        