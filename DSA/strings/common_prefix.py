str = ["flower", "flow", "flight"]

def common_prefix(str):
    prefix=str[0]
    for s in str:
        while not s.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix :
                return " "
    return prefix

print(common_prefix(str))