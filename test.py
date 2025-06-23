import tomllib

with open("F:/stuff/blender/blender-config/config/leader_key.toml", "rb") as f:
    data = tomllib.load(f)
    for i in data:
        ctype = "ALL"
        cmode = "ALL"
        if "sequence" not in data[i] or "func" not in data[i]:
            break
        if  "ctype" in data[i]:
            ctype = data[i]["ctype"]
        if  "cmode" in data[i]:
            cmode = data[i]["cmode"]
        print(data[i]["sequence"])
        print(data[i])
    print(data)