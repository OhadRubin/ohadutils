
import glob
import os
import json
from tqdm.auto import tqdm
def read_glob(paths_,limit=None,use_tqdm=False):
    if isinstance(paths_,list):
        paths = []
        for p in paths_:
            paths.extend(glob.glob(os.path.expandvars(p)))
    else:
        assert isinstance(paths_,str)
        paths = glob.glob(os.path.expandvars(paths_))
    data = []
    if use_tqdm:
        wrapper = tqdm(paths[:limit])
    else:
        wrapper = paths[:limit]

    for path in wrapper:
        with open(path) as f:
            if path.endswith(".json"):
                data.extend(json.load(f))
            elif path.endswith(".jsonl"):
                for line in f:
                    data.append(json.loads(line))
    return data
