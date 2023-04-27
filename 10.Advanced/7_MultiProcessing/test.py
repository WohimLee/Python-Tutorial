import numpy as np
import multiprocessing
from sklearn.manifold import TSNE
import time
 
 
path = "E:\\blog\\data\\MNIST50m\\"
 
 
def run_tsne(data):
    t_sne = TSNE(n_components=2, perplexity=30.0)
    Y = t_sne.fit_transform(data)
    return Y
 
 
def single_run(digits, fold="1by1"):
    for digit in digits:
        print(str(digit) + " starting...")
        X = np.loadtxt(path+str(digit)+".csv", dtype=np.float, delimiter=",")
        t_sne = TSNE(n_components=2, perplexity=30.0)
        Y = t_sne.fit_transform(X)
        np.savetxt(path+fold+"\\Y"+str(digit)+".csv", Y, fmt='%f', delimiter=",")
        print(str(digit) + " finished.")
 
 
def one_by_one():
    begin_time = time.time()
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # digits = [1, 2, 3, 4, 5, 6]
    single_run(digits, "1by1")
    end_time = time.time()
    print("one by one time: ", end_time-begin_time)
 
 
def parallel():
    begin_time = time.time()
    n = 10  # 10
    procs = []
    n_cpu = multiprocessing.cpu_count()
    chunk_size = int(n/n_cpu)
 
    for i in range(0, n_cpu):
        min_i = chunk_size * i
 
        if i < n_cpu-1:
            max_i = chunk_size * (i+1)
        else:
            max_i = n
        digits = []
        for digit in range(min_i, max_i):
            digits.append(digit)
        procs.append(multiprocessing.Process(target=single_run, args=(digits, "parallel")))
 
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()
 
    end_time = time.time()
    print("parallel time: ", end_time-begin_time)
 
 
if __name__ == '__main__':
    # one_by_one()
    parallel()