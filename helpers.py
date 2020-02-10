import yaml

def load_config(path='./config.yaml'):
  with open(path) as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)
  return config