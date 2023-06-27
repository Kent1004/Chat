import yaml

with open('input.txt', 'r') as f_n:
    OBJ = f_n.read()

with open('output.yaml', 'w') as f_n:
    yaml.dump(OBJ, f_n, allow_unicode=True, default_flow_style=False)
