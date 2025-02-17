from main import *
from functools import partial

def test_simple_work():
    assert simple_work_calc(10, 2, 2) == 36
    assert simple_work_calc(20, 3, 2) == 230 
    assert simple_work_calc(30, 4, 2) == 650


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300

def test_compare_work():
	work_fn1 = partial(work_calc, a=2, b=2, f=lambda n: n)
	work_fn2 = partial(work_calc, a=3, b=2, f=lambda n: n*n)
	res = compare_work(work_fn1, work_fn2)
	print(res)

def test_compare_span():
	span_fn1 = partial(span_calc, a=2, b=2, f=lambda n: n)
	span_fn2 = partial(span_calc, a=3, b=2, f=lambda n: n*n)
	res = compare_work(span_fn1, span_fn2)
	print(res)
