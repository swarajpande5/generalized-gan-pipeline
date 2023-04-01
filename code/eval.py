import json 

def eval_model():
    print("Loading the data and the model...")
    with open('./metrics/eval.json', 'w') as f:
        json.dump({}, f)
    print("done.")

if __name__ == '__main__':
    eval_model()