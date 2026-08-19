#!/usr/bin/env python3
import json, math, time
from collections import Counter
from decimal import Decimal, getcontext
from pathlib import Path
from flint import arb, ctx

ctx.prec=192
getcontext().prec=80
ROOT=Path('/mnt/data/II_KM_predecessor')
G=ROOT/'gauss'

def mm(M,n):
    A,B,C,D=M
    # M * [[0,1],[1,n]]
    return (B, A+B*n, D, C+D*n)

def trace_hist(m=8,N=6):
    states={(1,0,0,1):1}
    # keep multiplicities of matrices to compress repeated products early
    for _ in range(m):
        ns={}
        for M,c in states.items():
            for n in range(1,N+1):
                X=mm(M,n)
                ns[X]=ns.get(X,0)+c
        states=ns
    h=Counter()
    for (A,B,C,D),c in states.items(): h[A+D]+=c
    return h, sum(states.values()), len(states)

def contribution_from_trace(T:int):
    t=arb(T)
    lam=(t+(t*t-4).sqrt())/2
    q=1/(lam*lam)
    return q/(1-q)

def interval_decimal(lo,hi):
    return (Decimal(str(lo)),Decimal(str(hi)))
def iadd(a,b): return (a[0]+b[0],a[1]+b[1])
def imul(a,b):
    p=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return (min(p),max(p))
def iscale(a,c):
    c=Decimal(c)
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)

def arb_bounds_decimal(x):
    # parse a sufficiently detailed decimal ball and turn it into outward decimal endpoints
    s=x.str(70,more=True)
    if '+/-' not in s:
        d=Decimal(s.strip('[]')); return d,d,s
    body=s.strip('[]')
    mid_s,rad_s=body.split('+/-')
    mid=Decimal(mid_s.strip()); rad=Decimal(rad_s.strip())
    return mid-rad,mid+rad,s

def main():
    t0=time.time(); N=6; m=8
    hist,words,distinct_mats=trace_hist(m,N)
    partial=arb(0)
    for T,c in hist.items(): partial += c*contribution_from_trace(T)
    z2=arb.pi()**2/6
    SN=sum(arb(1)/(n*n) for n in range(1,N+1))
    tail_bound=arb(4)/3*(z2**m-SN**m)
    plo,phi,pstr=arb_bounds_decimal(partial)
    blo,bhi,bstr=arb_bounds_decimal(tail_bound)
    # The unknown complement lies in [0, tail_bound]. Build decimal endpoints
    # directly; arb(mid,rad) uses fixed low precision for rad and can visibly inflate.
    tlo,thi=plo,phi+bhi
    tstr=f'[{tlo}, {thi}]'

    kh=json.load(open(G/'II_KH_gauss_fredholm_riesz.json'))
    ki=json.load(open(G/'II_KI_gauss_fredholm_second_riesz.json'))
    kj=json.load(open(G/'II_KJ_gauss_fifth_third_riesz.json'))
    kk=json.load(open(G/'II_KK_gauss_sixth_threepoint.json'))
    kl=json.load(open(ROOT/'II_KL_gauss_seventh_reduced_resolvent.json'))
    traces={
      1: interval_decimal(*kh['trace_data']['trL']['interval']),
      2: interval_decimal(*kh['trace_data']['trL2']['interval']),
      3: interval_decimal(*kh['trace_data']['trL3']['interval']),
      4: interval_decimal(*ki['fourth_trace']['certified_interval']),
      5: interval_decimal(*kj['fifth_trace']['certified_interval']),
      6: interval_decimal(*kk['sixth_trace']['certified_interval']),
      7: interval_decimal(*kl['seventh_trace']['certified_interval']),
      8: (tlo,thi),
    }
    ds={
      1: interval_decimal(*kh['fredholm_coefficients']['d1']),
      2: interval_decimal(*kh['fredholm_coefficients']['d2']),
      3: interval_decimal(*kh['fredholm_coefficients']['d3']),
      4: interval_decimal(*ki['fredholm_d4']['certified_interval']),
      5: interval_decimal(*kj['fredholm_d5']['certified_interval']),
      6: interval_decimal(*kk['fredholm_d6']['certified_interval']),
      7: interval_decimal(*kl['fredholm_d7']['certified_interval']),
    }
    s=(Decimal(0),Decimal(0))
    terms=[]
    for j in range(1,8):
        term=imul(ds[8-j],traces[j])
        terms.append({'d':8-j,'trace_power':j,'interval':[str(term[0]),str(term[1])]})
        s=iadd(s,term)
    s=iadd(s,traces[8])
    d8=iscale(s,Decimal(-1)/Decimal(8))
    out={
      'phase':'II-KM',
      'carrier':'Gauss analytic trace-class transfer operator on inherited Hardy/weighted nuclear lane',
      'eighth_trace':{
        'box_N':N,'ordered_word_count':words,'distinct_exact_matrices':distinct_mats,'distinct_matrix_traces':len(hist),
        'orientation':'eight inverse branches have determinant +1; fixed-point contribution q/(1-q)',
        'partial_ball':pstr,'tail_bound_ball':bstr,'certified_total_ball':tstr,
        'certified_interval_decimal':[str(tlo),str(thi)],
        'tail_bound':'q/(1-q) <= (4/3)q and q <= prod(digit)^-2; complement <= (4/3)(zeta(2)^8-S_N^8)',
        'min_trace_in_box':min(hist),'max_trace_in_box':max(hist),
        'status':'PASS_CERTIFIED_TR_L8_CONSERVATIVE_TAIL'
      },
      'fredholm_d8':{
        'newton_identity':'8 d8=-(d7 trL+d6 trL2+d5 trL3+d4 trL4+d3 trL5+d2 trL6+d1 trL7+trL8)',
        'certified_interval_decimal':[str(d8[0]),str(d8[1])],
        'term_intervals':terms,
        'status':'PASS_CERTIFIED_D8_FROM_FROZEN_PREDECESSOR_INTERVALS_AND_NEW_TRL8'
      },
      'reduced_resolvent_norm':'SEPARATED_NO_NEW_CERTIFIED_OPERATOR_NORM_BOUND',
      'third_pressure_numeric':'SEPARATED_NO_NEW_PROOF_GRADE_NUMERICAL_P3_ENCLOSURE',
      'runtime':{'python':'3.13.5','python_flint':'0.9.0','arb_precision_bits':192,'seconds':time.time()-t0},
      'guards':['eighth-trace tail is positive and deliberately conservative','no numerical reduced-resolvent norm is inferred from existence alone','no numerical third-pressure value is fabricated'],
      'status':'PASS_EIGHTH_FREDHOLM_TRACE_COEFFICIENT__NUMERICAL_RESOLVENT_NORM_AND_THIRD_PRESSURE_REMAIN_SEPARATED'
    }
    Path('/mnt/data/II_KM/II_KM_gauss_eighth_fredholm.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'trL8':out['eighth_trace']['certified_interval_decimal'],'d8':out['fredholm_d8']['certified_interval_decimal'],'words':words,'distinct_traces':len(hist),'seconds':round(out['runtime']['seconds'],3)}))
if __name__=='__main__':main()
