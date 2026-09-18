def single_machine():
    return {"number_of_jobs":3,"number_of_machines":1,"operations_per_job":[2,1,2],
      "operations":[
       {"job_id":0,"operation_id":0,"eligible":{"0":3}},
       {"job_id":0,"operation_id":1,"eligible":{"0":2}},
       {"job_id":1,"operation_id":0,"eligible":{"0":4}},
       {"job_id":2,"operation_id":0,"eligible":{"0":1}},
       {"job_id":2,"operation_id":1,"eligible":{"0":5}}],
      "metadata":{"class":"single-machine"}}
