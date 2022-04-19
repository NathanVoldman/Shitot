def has_repeating_letter(x): #has_rep
    x = list(x)
    while x:
        y = x.pop()
        if y in x:
            return True
    return False

def filter_repeating_letter_words(x_list): #fltr_rep
    z = []
    for x in x_list:
        if has_repeating_letter(x):
            z.append(x)
    return z


if __name__=="__main__":
    x_list = ['this','riddle','has','nothing','to','do','with','all','the','other','questions']
    print(filter_repeating_letter_words(x_list))

# Answers:

# 1.['riddle', 'nothing', 'all', 'questions']
# 2.['this', 'has', 'to', 'do', 'with', 'the', 'other']
# 3.['this', 'riddle', 'has', 'nothing', 'to', 'do', 'with', 'all', 'the', 'other', 'questions']
# 4.['riddle', 'all']