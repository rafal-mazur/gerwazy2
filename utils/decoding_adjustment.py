def all_possibilities(s: str):
    res = []
    res.append(s)
    res.append(s.replace('5', 's'))
    res.append(s.replace('s', '5'))
    res.append(s.replace('2', 'z'))
    res.append(s.replace('z', '2'))
    
    return set(res)
    
