from dataclasses import dataclass, asdict
import json

@dataclass
class Instance:
    number_of_jobs: int
    number_of_machines: int
    operations_per_job: list
    operations: list
    metadata: dict

def save_instance(inst, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(asdict(inst), f, indent=2)

def load_instance(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    return Instance(d["number_of_jobs"], d["number_of_machines"],
                    d["operations_per_job"], d["operations"], d["metadata"])
