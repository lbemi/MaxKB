from datasets import load_dataset

dataset = load_dataset("victor/real-or-fake-fake-jobposting-prediction")

print(len(dataset['train']))
print(dataset['train'][0])
with open('real-or-fake-fake-jobposting-prediction.txt', 'w') as f:
    for row in dataset['train']:
        f.write(str(row) + '\n')
