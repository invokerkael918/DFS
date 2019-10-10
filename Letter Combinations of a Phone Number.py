
num_to_letters = {'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}

def letterCombinations(digits):
    # write your code here
    if not digits:
        return []
    result = []
    dfs(digits,0,'',result)
    return result



def dfs(digits,index,path,result):
    if len(path) == len(digits):
        result.append(path)
        return

    for numStr in num_to_letters[digits[index]]:
        dfs(digits,index+1,path+numStr,result)





