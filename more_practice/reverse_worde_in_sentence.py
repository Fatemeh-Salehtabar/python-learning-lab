user_sentence = input("enter a sentence: ")
new_list= []
for word in user_sentence.split(" "):
    if len(word) > 5 :
        new_list.append(word[ : :-1])
    else:
        new_list.append(word)
print(" ".join(new_list))