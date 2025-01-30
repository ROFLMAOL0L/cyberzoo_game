def read_config(path: str) -> dict:
    out_dict = {}
    with open(path, "r") as config_file:
        for config_line in config_file:
            out_dict[config_line.split(" = ")[0]] = config_line.split(" = ")[1][:-1]
    return out_dict
