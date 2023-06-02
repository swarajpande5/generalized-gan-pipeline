from model_class import ACGAN

import json
import os
import time 


def train_model():
    print("Training model...")
    
    if not os.path.exists('./images'):
        os.mkdir('./images')
    
    start_time = time.time()
    acgan = ACGAN() 
    acgan.train(epochs=100, batch_size=32, sample_interval=25)
    end_time = time.time()
    
    with open('./metrics/train_metric.json', 'w') as f:
        json.dump({'training_time': end_time - start_time}, f)
    print("done.")

if __name__ == '__main__':
    train_model()
