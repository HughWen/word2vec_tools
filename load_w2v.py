import numpy as np


def get_w2v_dict(textfile):
    w2v_dict = {}
    f = open(textfile, encoding='utf8')
    line = f.readline()
    while line:
        parts = line.split()
        w2v_dict[parts[0]] = np.array([float(i) for i in parts[1:]])
        line = f.readline()
    return w2v_dict

if __name__ == '__main__':
    w2v_model_path = './test_model.txt'
    w2v_dict = get_w2v_dict(w2v_model_path)
    print(w2v_dict['a'])
