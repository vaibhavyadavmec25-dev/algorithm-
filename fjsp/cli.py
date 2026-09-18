import argparse,json
from .generator import generate_class
from .algorithm import solve
from .validator import validate
from .metrics import metrics

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--class-name",default="average"); a.add_argument("--seed",type=int,default=1)
    a.add_argument("--jobs",type=int,default=8); a.add_argument("--machines",type=int,default=4)
    a.add_argument("--ops",type=int,default=5)
    x=a.parse_args(); inst=generate_class(x.class_name,x.jobs,x.machines,x.ops,x.seed)
    sch=solve(inst); err=validate(inst,sch)
    print("VALID" if not err else "INVALID"); print(json.dumps(metrics(inst,sch),indent=2))
if __name__=="__main__": main()
