import random
from .model import Instance, save_instance

CLASSES = {
 "average":(.50,.10,.20),"easy":(.70,.05,.10),"hard":(.45,.20,.35),
 "extreme":(.35,.35,.70),"bottleneck-heavy":(.55,.55,.25),
 "high-flexibility":(.85,.10,.25),"low-flexibility":(.20,.10,.25),
 "high-variance":(.50,.10,.80),"unbalanced":(.50,.45,.60)
}

def generate(jobs,machines,ops,machine_flexibility=.5,
             processing_time_range=(1,100),processing_time_variance=.2,
             bottleneck_probability=.1,seed=1,instance_class="custom"):
    rng=random.Random(seed); lo,hi=processing_time_range
    b=rng.randrange(machines); out=[]
    for j in range(jobs):
        for k in range(ops if isinstance(ops,int) else ops[j]):
            target=max(1,min(machines,round(1+machine_flexibility*(machines-1))))
            size=max(1,min(machines,target+rng.choice([-1,0,0,1])))
            eligible=set(rng.sample(range(machines),size))
            if rng.random()<bottleneck_probability: eligible={b}
            elif rng.random()<.25: eligible.add(b)
            times={}
            spread=(hi-lo)*(0.15+0.85*processing_time_variance)
            for m in sorted(eligible):
                p=round(rng.gauss((lo+hi)/2,spread))
                p=max(lo,min(hi,int(p)))
                times[str(m)]=max(1,p)
            out.append({"job_id":j,"operation_id":k,"eligible":times})
    op_counts=[ops if isinstance(ops,int) else ops[j] for j in range(jobs)]
    return Instance(jobs,machines,op_counts,out,{
      "seed":seed,"instance_class":instance_class,
      "machine_flexibility":machine_flexibility,
      "processing_time_range":list(processing_time_range),
      "processing_time_variance":processing_time_variance,
      "bottleneck_probability":bottleneck_probability})

def generate_class(name,jobs=8,machines=4,ops=5,seed=1):
    f,b,v=CLASSES[name]
    return generate(jobs,machines,ops,f,(1,100),v,b,seed,name)

if __name__=="__main__":
    import argparse
    a=argparse.ArgumentParser()
    a.add_argument("--class-name",choices=sorted(CLASSES),default="average")
    a.add_argument("--jobs",type=int,default=8); a.add_argument("--machines",type=int,default=4)
    a.add_argument("--ops",type=int,default=5); a.add_argument("--seed",type=int,default=1)
    a.add_argument("--out",default="instances/example.json")
    x=a.parse_args(); save_instance(generate_class(x.class_name,x.jobs,x.machines,x.ops,x.seed),x.out)
