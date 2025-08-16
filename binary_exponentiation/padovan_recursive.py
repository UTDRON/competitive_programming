#unlike fibonacci, in padovan sequence tn = tn-2+ tn-3
#so t0 = 1, t1 = 1, t2 = 1

def padovan(n: int) -> int:
    if n in [0, 1, 2]:
        return 1
    
    return padovan(n-2) + padovan(n-3)


assert padovan(0) == 1, "should be 1"
assert padovan(1) == 1, "should be 1"
assert padovan(2) == 1, "should be 1"
assert padovan(3) == 2, "should be 2"
assert padovan(4) == 2, "should be 2"
assert padovan(5) == 3, "should be 3"
assert padovan(6) == 4, "should be 4"
assert padovan(7) == 5, "should be 5"
assert padovan(13) == 28, "should be 28"
assert padovan(15) == 49, "should be 49"
assert padovan(40) == 55405, "should be 55405"
assert padovan(65) == 62608681, "should be 62608681"

