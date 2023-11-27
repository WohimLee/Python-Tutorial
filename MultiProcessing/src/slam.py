

import torch.multiprocessing as mp


class SLAM:
    def __init__(self):
        self.only_track = False    
    
    def tracking(self, rank):
        print("Running tracking...")
    
    
    def mapping(self, rank, stop=False):
        print("Running mapping...")
        
    
    def run(self):
        stop = True
        processes = [
            mp.Process(target=self.tracking, args=(0, )),
            mp.Process(target=self.mapping, args=(1, stop if self.only_track else (not stop)))
        ]
        
        for p in processes:
            p.start()
            
        for p in processes:
            p.join()
        
        
if __name__ == '__main__':
    slam = SLAM()
    slam.run()