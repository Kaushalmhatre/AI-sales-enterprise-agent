def parse_output(text):
    pain = ""
    stack = ""
    outcome = ""

    lines = text.split("\n")

    for line in lines:
        if "Pain" in line:
            pain += line
        elif "Tech" in line:
            stack += line
        elif "Outcome" in line:
            outcome += line

    return pain, stack, outcome