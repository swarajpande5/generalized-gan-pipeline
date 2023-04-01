import json 
import numpy as np 

def featurization():
    print("Featurizing the datasets...")
    np.save('./data/processed_train_data', [])
    np.save('./data/processed_test_data', [])

    with open('./data/norm_params.json', 'w') as f:
        json.dump({}, f)
    print("done.")


if __name__ == '__main__':
    featurization() 