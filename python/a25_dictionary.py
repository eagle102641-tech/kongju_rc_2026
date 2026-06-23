def main():
    dict_a={"a": "aa"}
    dict_a=dict()
    print(type(dict_a))
    
    dict_a["b"]="bbb"
    print(dict_a)
    print(dict_a["a"], dict_a["b"], dict_a.get("c"))
    
    print(dict_a.pop("a"))
    print(dict_a)
    
if __name__ == "__main__":
    main()