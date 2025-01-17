import unittest
import compiler

class TestCompiler(unittest.TestCase):
    def test_all_opcodes(self):
        for key, op in [[k,v] for k, v in compiler.opcode_map.items()]:
            inp = key + " "
            len_out = 1
            for i, opp in enumerate(op[1:]):
                opp=opp.split(',')[0]
                inp+=opp
                inp+='1'
                if "p" in opp:
                    len_out+=5
                elif "c" == opp:
                    len_out+=1
                elif "r" == opp:
                    len_out+=1
                inp+=" "
            code = compiler.assembly_to_bin(inp,verbose=False)
            self.assertTrue([str(v) for v in code][0] == str(int(op[0])),f"Err ({[str(v) for v in code][0]} != {str(int(op[0]))})")
            self.assertTrue(len([str(v) for v in code]) == len_out,f"Code is not right size {len([str(v) for v in code])}/{len_out}: {[str(v) for v in code]}")
            

if __name__ == '__main__':
    unittest.main()