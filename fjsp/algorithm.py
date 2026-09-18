def solve(instance):
    machine_free=[0.0]*instance.number_of_machines
    job_free=[0.0]*instance.number_of_jobs
    schedule=[]
    for j in range(instance.number_of_jobs):
        ops=[o for o in instance.operations if o["job_id"]==j]
        ops.sort(key=lambda o:o["operation_id"])
        for o in ops:
            choices=[]
            for sm,p in o["eligible"].items():
                m=int(sm); start=max(job_free[j],machine_free[m]); finish=start+p
                choices.append((finish,start,m,p))
            finish,start,m,p=min(choices)
            schedule.append({"job_id":j,"operation_id":o["operation_id"],
              "machine_id":m,"start_time":start,"completion_time":finish})
            machine_free[m]=finish; job_free[j]=finish
    return schedule
