import re
sentences = ['This is awesome', 'because it is the best!', 'What do you think you', 'are doing?']

new_sentences = []

properEnding = ['.', '!', '?']
# properBeginning = re.match('^[A-Z]')


# for i in range(len(sentences) - 1):
#     if sentences[i][-1] in properEnding:
#         print('True')
#     else:
#         print('False')

# for i in range(len(sentences) - 1):
#     if re.match('^[A-Z]', sentences[i]):
#         print('True')
#     else:
#         print('False')

for i in range(len(sentences) - 1):
    if not re.match('^[A-Z]',sentences[i + 1][0]):
        if sentences[i][-1] not in properEnding:
            sentences[i] = sentences[i] + ' ' + sentences[i + 1]
            sentences[i+1] = 'Delete this Sentence!'
            new_sentences.append(sentences[i])
    else:
        new_sentences.append(sentences[i])
new_sentences.append(sentences[i+1])

for i in new_sentences:
    if 'Delete this Sentence!' in new_sentences:
        new_sentences.remove('Delete this Sentence!')


print(new_sentences)
