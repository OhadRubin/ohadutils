from sqlitedict import SqliteDict
import os
import fire
#adads
from contextlib import contextmanager
import logging

@contextmanager
def all_logging_disabled(highest_level=logging.CRITICAL):
    previous_level = logging.root.manager.disable

    logging.disable(highest_level)
    try:
        yield
    finally:
        logging.disable(previous_level)

class PersistentQueue:
    def __init__(self,name="~/.cache/slurm.bin"):
        self.cache_name = os.path.expanduser(name)
        with all_logging_disabled():
            self.database = SqliteDict(self.cache_name, autocommit=True)
            
        if "jobs" not in self.database:
            self.database['jobs'] = []
    def put(self,item):
        queue = self.database['jobs']
        queue.append(item)
        self.database['jobs'] = queue
        
    def get(self,idx):
        return self.database['jobs'][idx]
    def __len__(self):
        return len(self.database['jobs'])
    def reset(self):
        self.database['jobs'] = []
        
    @classmethod
    def put_job(cls,job_id):
        cls().put(job_id)

if __name__ == '__main__':
  fire.Fire(PersistentQueue)