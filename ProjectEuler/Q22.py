

with open('./ProjectEuler/names.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
for line in content:
    names = line.split(',')

names.sort()
name=[]
scores=[]
score=[]
# sum_answer=0
for i in range(0,len(names)):
    name.append(names[i].replace('"', ''))
    for character in name[i]:
        number = ord(character) - 64
        scores.append(number)
    score.append(sum(scores)*(i+1))
    # sum_answer = sum_answer + sum(scores)*(i+1)
    scores=[]

print(sum(score))

