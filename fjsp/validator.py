from collections import defaultdict

def validate(instance,schedule):
    errors=[]; expected={(o["job_id"],o["operation_id"]) for o in instance.operations}; seen=set()
    jobs=defaultdict(list); machines=defaultdict(list)
    for x in schedule if isinstance(schedule,list) else []:
        try:
            key=(int(x["job_id"]),int(x["operation_id"])); m=int(x["machine_id"])
            s=float(x["start_time"]); c=float(x["completion_time"])
        except Exception:
            errors.append("malformed operation record"); continue
        if key in seen: errors.append(f"duplicate operation {key}")
        seen.add(key)
        op=next((o for o in instance.operations if (o["job_id"],o["operation_id"])==key),None)
        if op is None: errors.append(f"unknown operation {key}"); continue
        if str(m) not in op["eligible"]: errors.append(f"ineligible machine for {key}")
        if s<0: errors.append(f"negative start time for {key}")
        if str(m) in op["eligible"] and abs(c-s-op["eligible"][str(m)])>1e-9:
            errors.append(f"wrong completion time for {key}")
        jobs[key[0]].append((key[1],s,c)); machines[m].append((s,c,key))
    if not isinstance(schedule,list): errors.append("schedule must be a list")
    for key in expected-seen: errors.append(f"missing operation {key}")
    for j,a in jobs.items():
        a.sort()
        for u,v in zip(a,a[1:]):
            if v[1]<u[2]-1e-9: errors.append(f"precedence violation in job {j}")
    for m,a in machines.items():
        a.sort()
        for u,v in zip(a,a[1:]):
            if v[0]<u[1]-1e-9: errors.append(f"machine overlap on machine {m}")
    return errors

def is_valid(instance,schedule): return not validate(instance,schedule)
