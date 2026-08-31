def print_table(data: list[dict], attrnames: list[str]):
    format = ['%10s'] * len(attrnames)
    format = ' '.join(format)
        
    print(format % tuple(attrnames))
    
    print(format % tuple(['----------'] * len(attrnames)))
    
    for item in data:
        print(format % tuple(getattr(item, attr) for attr in attrnames))