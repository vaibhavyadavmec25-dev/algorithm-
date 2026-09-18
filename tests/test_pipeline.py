import unittest
from fjsp.generator import generate_class
from fjsp.algorithm import solve
from fjsp.validator import validate

class PipelineTests(unittest.TestCase):
    def test_pipeline(self):
        inst=generate_class("hard",5,3,4,7)
        self.assertEqual(validate(inst,solve(inst)),[])
    def test_invalid_machine(self):
        inst=generate_class("easy",2,2,2,3); s=solve(inst)
        s[0]["machine_id"]=999
        self.assertTrue(validate(inst,s))

if __name__=="__main__": unittest.main()
