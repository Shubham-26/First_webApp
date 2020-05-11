from . import views
import operator
def count(article):
    words= article.split()
    words_count= len(words)
    dict_word ={}

    for word in words:
        if word in dict_word:
            dict_word[word] +=1
        else:
            dict_word[word] = 1


    var_dict= sorted(dict_word.items(),key=operator.itemgetter(1), reverse=True)
    return var_dict,words_count
