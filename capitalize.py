def capitalize_2nd_letter(x):
    ans = ''
    for i,c in enumerate(x):
        if i==1:
            ans = ans + c.upper()
        else:
            ans = ans + c
    return ans

def capitalize_2nd_letter_of_even_words(x):
    ans = []
    x = x.split(' ')
    for i,y in enumerate(x):
        if i%2:
            z = capitalize_2nd_letter(y)
        else:
            z=y
        ans.append(z)
    return ' '.join(ans)

def main():
    x = str(input('?:'))
    y = capitalize_2nd_letter_of_even_words(x)
    print(y)

if __name__=="__main__":
    main()
