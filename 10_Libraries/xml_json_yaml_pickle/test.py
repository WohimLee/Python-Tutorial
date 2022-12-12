
import os
import sys
import json
import warnings
warnings.filterwarnings('ignore')
ROOT = os.getcwd()
sys.path.append('/home/liheqian/datav/QuatitativeTrading/vnpy/')


dict1 = {
    "a": 111,
    "b": 222
}

def load_json(path):
    with open(path) as f:
        # data = f.read()
        data = json.load(f)
    return data
d = load_json('./test.json')

print(d)