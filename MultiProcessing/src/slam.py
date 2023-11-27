

import torch.multiprocessing as mp


class SLAM:
    def __init__(self):
        pass
    
    
    def tracking(self):
        pass
    
    
    def mapping(self):
        pass
    
    def run(self):
        processes = [
            mp.Process(target=self.tracking)
        ]