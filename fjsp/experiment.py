import json,os
from .generator import generate_class
from .algorithm import solve
from .validator import validate
from .metrics import metrics

def run(classes=None,seeds=range(1,6),out_dir="results"):
    classes=classes or ["average","easy","hard","extreme","bottleneck-heavy",
                         "high-flexibility","low-flexibility","high-variance","unbalanced"]
    os.makedirs(out_dir,exist_ok=True); rows=[]
    for cls in classes:
        for seed in seeds:
            inst=generate_class(cls,8,4,5,seed); sch=solve(inst)
            err=validate(inst,sch); met=metrics(inst,sch)
            rows.append({"class":cls,"seed":seed,"makespan":met["makespan"],
                         "valid":not err,"validation_errors":err})
    with open(os.path.join(out_dir,"experiment_results.json"),"w") as f:
        json.dump(rows,f,indent=2)
    return rows

if __name__=="__main__": run()
