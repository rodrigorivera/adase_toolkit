import pickle

def load_pkl(name):
    name = name + '.pkl'
    pkl_file = open(name, 'rb')
    result = pickle.load(pkl_file)
    pkl_file.close()
    return result