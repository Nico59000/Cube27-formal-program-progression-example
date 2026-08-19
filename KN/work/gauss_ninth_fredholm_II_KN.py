#!/usr/bin/env python3
import json,time
from collections import Counter
from decimal import Decimal,getcontext
from pathlib import Path
from flint import arb,ctx
ctx.prec=192; getcontext().prec=90
ROOT=Path(__file__).resolve().parents[1]; G=ROOT/'dependencies'/'gauss'

def mm(M,n):
 A,B,C,D=M; return (B,A+B*n,D,C+D*n)

def trace_hist(m=9,N=6):
 states={(1,0,0,1):1}
 sizes=[]
 for _ in range(m):
  ns={}
  for M,c in states.items():
   for n in range(1,N+1):
    X=mm(M,n); ns[X]=ns.get(X,0)+c
  states=ns; sizes.append(len(states))
 h=Counter()
 for (A,B,C,D),c in states.items(): h[A+D]+=c
 return h,N**m,len(states),sizes

def contribution(T):
 t=arb(T); lam=(t+(t*t+4).sqrt())/2  # det=-1: expanding eigenvalue solves l^2-Tl-1=0
 q=1/(lam*lam)
 return q/(1+q)

def decint(a,b): return Decimal(str(a)),Decimal(str(b))
def iadd(a,b): return a[0]+b[0],a[1]+b[1]
def imul(a,b):
 p=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]; return min(p),max(p)
def iscale(a,c):
 c=Decimal(c); return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def arb_bounds(x):
 s=x.str(80,more=True); body=s.strip('[]')
 if '+/-' not in body:
  d=Decimal(body); return d,d,s
 mid,rad=body.split('+/-'); m=Decimal(mid.strip()); r=Decimal(rad.strip()); return m-r,m+r,s

def main():
 t0=time.time(); m=9; N=6
 h,words,dmats,sizes=trace_hist(m,N)
 partial=arb(0)
 for T,c in h.items(): partial += c*contribution(T)
 z2=arb.pi()**2/6; SN=sum(arb(1)/(n*n) for n in range(1,N+1))
 # odd parity: q/(1+q) <= q <= product digit^-2
 tail=z2**m-SN**m
 plo,phi,pstr=arb_bounds(partial); blo,bhi,bstr=arb_bounds(tail)
 tr9=(plo,phi+bhi)
 kh=json.load(open(G/'II_KH_gauss_fredholm_riesz.json'))
 ki=json.load(open(G/'II_KI_gauss_fredholm_second_riesz.json'))
 kj=json.load(open(G/'II_KJ_gauss_fifth_third_riesz.json'))
 kk=json.load(open(G/'II_KK_gauss_sixth_threepoint.json'))
 kl=json.load(open(G/'II_KL_gauss_seventh_reduced_resolvent.json'))
 km=json.load(open(G/'II_KM_gauss_eighth_fredholm.json'))
 traces={
 1:decint(*kh['trace_data']['trL']['interval']),2:decint(*kh['trace_data']['trL2']['interval']),3:decint(*kh['trace_data']['trL3']['interval']),
 4:decint(*ki['fourth_trace']['certified_interval']),5:decint(*kj['fifth_trace']['certified_interval']),6:decint(*kk['sixth_trace']['certified_interval']),
 7:decint(*kl['seventh_trace']['certified_interval']),8:tuple(Decimal(x) for x in km['eighth_trace']['certified_interval_decimal']),9:tr9}
 ds={1:decint(*kh['fredholm_coefficients']['d1']),2:decint(*kh['fredholm_coefficients']['d2']),3:decint(*kh['fredholm_coefficients']['d3']),
 4:decint(*ki['fredholm_d4']['certified_interval']),5:decint(*kj['fredholm_d5']['certified_interval']),6:decint(*kk['fredholm_d6']['certified_interval']),
 7:decint(*kl['fredholm_d7']['certified_interval']),8:tuple(Decimal(x) for x in km['fredholm_d8']['certified_interval_decimal'])}
 s=(Decimal(0),Decimal(0)); terms=[]
 for j in range(1,9):
  term=imul(ds[9-j],traces[j]); s=iadd(s,term); terms.append({'d':9-j,'trace_power':j,'interval':[str(term[0]),str(term[1])]})
 s=iadd(s,traces[9]); d9=iscale(s,-Decimal(1)/Decimal(9))
 out={'phase':'II-KN','carrier':'Gauss analytic trace-class transfer operator on inherited Hardy/weighted nuclear lane',
 'ninth_trace':{'box_N':N,'ordered_word_count':words,'distinct_exact_matrices':dmats,'state_sizes_by_depth':sizes,'distinct_matrix_traces':len(h),
 'orientation':'nine inverse branches have determinant -1; fixed-point contribution q/(1+q)','partial_ball':pstr,'tail_bound_ball':bstr,
 'certified_interval_decimal':[str(tr9[0]),str(tr9[1])], 'tail_bound':'q/(1+q)<=q<=prod(digit)^-2; complement <= zeta(2)^9-S_N^9',
 'min_trace_in_box':min(h),'max_trace_in_box':max(h),'status':'PASS_CERTIFIED_TR_L9_CONSERVATIVE_POSITIVE_TAIL'},
 'fredholm_d9':{'newton_identity':'9 d9=-(d8 trL+d7 trL2+d6 trL3+d5 trL4+d4 trL5+d3 trL6+d2 trL7+d1 trL8+trL9)',
 'certified_interval_decimal':[str(d9[0]),str(d9[1])],'term_intervals':terms,'status':'PASS_CERTIFIED_D9_FROM_FROZEN_INTERVALS_AND_NEW_TRL9'},
 'reduced_resolvent_norm':'PENDING_QUANTITATIVE_SOURCE_AUDIT','third_pressure_numeric':'PENDING_QUANTITATIVE_SOURCE_AUDIT',
 'runtime':{'python_flint':'0.9.0','arb_precision_bits':192,'seconds':time.time()-t0},
 'guards':['ninth-trace tail positive and conservative','no sign claim for d9 if interval crosses zero','quantitative resolvent/P3 not inferred from eigenvalue gap alone']}
 (ROOT/'II_KN_gauss_ninth_fredholm.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'trL9':out['ninth_trace']['certified_interval_decimal'],'d9':out['fredholm_d9']['certified_interval_decimal'],'words':words,'distinct_matrices':dmats,'distinct_traces':len(h),'sizes':sizes,'seconds':round(out['runtime']['seconds'],3)}))
if __name__=='__main__': main()
