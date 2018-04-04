def string_to_num(in_str):
    try:
        return int(in_str)
    except:
        try:
            return float(in_str)
        except:
            return in_str