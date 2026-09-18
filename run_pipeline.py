import os
from fjsp.generator import generate_class
from fjsp.algorithm import solve
from fjsp.validator import validate
from fjsp.metrics import metrics
from fjsp.model import save_instance

os.makedirs("instances",exist_ok=True)
inst=generate_class("average",8,4,5,42)
save_instance(inst,"instances/average_seed42.json")
schedule=solve(inst)
errors=validate(inst,schedule)
print("VALID" if not errors else "INVALID")
print(metrics(inst,schedule))
