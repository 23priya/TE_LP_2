rules = []
facts = set()

def add_rule(conditions, result):
    rules.append((conditions, result))

def add_fact(fact):
    facts.add(fact)

def forward_chaining():
    new_facts = set()
    while True:
        new_fact_added = False
        for conditions, result in rules:
            if all(condition in facts for condition in conditions) and result not in facts:
                new_facts.add(result)
                new_fact_added = True
        facts.update(new_facts)
        if not new_fact_added:
            break

def is_possible(item):
    forward_chaining()
    return item in facts


add_rule(["cargo_available", "plane_available"], "cargo_schedule")
add_rule(["airline_available"], "airline_schedule")


add_fact("cargo_available")
add_fact("plane_available")


if is_possible("cargo_schedule"):
    print("Cargo schedule is possible!")
else:
    print("Cargo schedule is not possible.")


if is_possible("airline_schedule"):
    print("Airline schedule is possible!")
else:
    print("Airline schedule is not possible.")
 
