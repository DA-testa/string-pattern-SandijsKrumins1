# python3

def read_input():
    mode = input()
    if "I" in mode:
        p = input().rstrip()
        t = input().rstrip()
    else:
        filename= "06"
        folder = './tests/'
        file = open(folder + filename, 'r')
        p = file.readline().rstrip()
        t = file.readline().rstrip()
    return (p,t)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    res = []
    M = len(pattern)
    N = len(text)
    hashp = 0    
    hasht = 0    
    h = 1
    for i in range(M-1):
        h = (h*256) % 101
    for i in range(M):
        hashp = (256*hashp + ord(pattern[i])) % 101
        hasht = (256*hasht + ord(text[i])) % 101
    for i in range(N-M+1):
        if hashp == hasht:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1
            if j == M:
                res.append(i)
        if i < N-M:
            hasht = (256*(hasht-ord(text[i])*h) + ord(text[i+M])) % 101
            if hasht < 0:
                hasht = hasht+101
    return res


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

