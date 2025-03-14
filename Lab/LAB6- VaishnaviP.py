def partition(s: str):
    def word(begin, flow):
        if begin == len(s):
            substr.append(flow[:])
            return
        
        
        w= begin +1        
        for last in range(w, len(s) + 1):
            if s[begin:last] == s[begin:last][::-1]:
                flow.append(s[begin:last])
                word(last, flow)
                flow.pop()

    substr = []
    word(0, [])
    return sorted(substr)

