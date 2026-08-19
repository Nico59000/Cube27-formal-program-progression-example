#!/usr/bin/env python3
import json, math, time, argparse
from pathlib import Path
from functools import lru_cache
from flint import nmod_poly, fmpz

MOD=3
X=nmod_poly([0,1],MOD)
ONE=nmod_poly([1],MOD)
MINUS_ONE=nmod_poly([MOD-1],MOD)

@lru_cache(maxsize=None)
def factor_integer(n:int):
    return [(int(p),int(e)) for p,e in fmpz(n).factor()]

@lru_cache(maxsize=None)
def factor_q_degree(d:int):
    return factor_integer(pow(MOD,d)-1)

def irred_x_order(g):
    d=g.degree()
    N=pow(MOD,d)-1
    o=N
    rev=None
    # FLINT's pow_mod is fast enough; reduce by each prime divisor fully.
    for p,e in factor_q_degree(d):
        for _ in range(e):
            if o%p==0 and X.pow_mod(o//p,g)==ONE:
                o//=p
            else:
                break
    assert X.pow_mod(o,g)==ONE
    return o

def char_p_mult_factor(m:int,p:int=MOD):
    # smallest p^a >= m, because order of unipotent nilpotent block of multiplicity m
    q=1
    while q<m: q*=p
    return q

def poly_kv(k:int,v:int):
    c=[0]*(k+1)
    c[0]=MOD-1
    c[v]=(c[v]+MOD-1)%MOD
    c[k]=1
    return nmod_poly(c,MOD)

def v2(n:int):
    c=0
    while n and n%2==0:
        c+=1; n//=2
    return c

def record(k:int,v:int):
    f=poly_kv(k,v)
    unit, facs=f.factor()
    contrib=[]; strings=[]
    for g,m in facs:
        o=irred_x_order(g)
        co=o*char_p_mult_factor(int(m))
        contrib.append([int(g.degree()),int(m),int(o),int(co)])
        strings.append(str(g))
    N=1
    for *_,co in contrib:
        N=math.lcm(N,co)
    if k%2==1:
        anti=None; mode='ZERO_BY_ODD_DETERMINANT_THEOREM'
    else:
        if N%2==0 and X.pow_mod(N//2,f)==MINUS_ONE:
            anti=N//2
        else:
            anti=None
        mode='DIRECT_POWER_MOD'
    return {
        'recurrence_order':k,'tap_value':v,'reflected_value':k-v,
        'order_plus_value':k+v,
        'factor_strings':strings,
        'factor_degree_multiplicity':contrib,
        'irreducible_factor_count':len(facs),
        'matrix_order':int(N),'global_antiperiod_h':anti,
        'antiperiod_decision_mode':mode,
        'matrix_order_equals_order':N==k,
        'matrix_order_equals_order_plus_value':N==k+v,
        'k_divides_matrix_order':N%k==0,
        'v_divides_matrix_order':N%v==0,
        'k_plus_v_divides_matrix_order':N%(k+v)==0,
        'gcd_matrix_with_order':math.gcd(N,k),
        'gcd_matrix_with_value':math.gcd(N,v),
        'gcd_matrix_with_order_plus_value':math.gcd(N,k+v),
        'v2_matrix_order':v2(N),
    }

def compare(a,b):
    keys=['recurrence_order','tap_value','reflected_value','order_plus_value','factor_strings','factor_degree_multiplicity','irreducible_factor_count','matrix_order','global_antiperiod_h','antiperiod_decision_mode','matrix_order_equals_order','matrix_order_equals_order_plus_value','k_divides_matrix_order','v_divides_matrix_order','k_plus_v_divides_matrix_order','gcd_matrix_with_order','gcd_matrix_with_value','gcd_matrix_with_order_plus_value','v2_matrix_order']
    return {k:(a.get(k),b.get(k)) for k in keys if a.get(k)!=b.get(k)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--qualify',type=Path)
    ap.add_argument('--orders',nargs='*',type=int)
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    t=time.time()
    qualification={}
    if args.qualify:
        old=json.loads(args.qualify.read_text())
        oldrecs=old['records_89']+old['records_96_105']
        # deterministic compact qualification set: endpoints/centers and every 97th record
        idx=sorted(set([0,len(old['records_89'])-1,len(old['records_89']),len(oldrecs)-1]+list(range(0,len(oldrecs),97))))
        mism=[]
        for i in idx:
            o=oldrecs[i]; n=record(o['recurrence_order'],o['tap_value']); d=compare(n,o)
            if d:mism.append({'index':i,'k':o['recurrence_order'],'v':o['tap_value'],'diff':d})
        qualification={'checked':len(idx),'matches':len(idx)-len(mism),'mismatches':mism}
    records=[]
    for k in args.orders or []:
        kt=time.time(); ks=[]
        for v in range(1,k):
            ks.append(record(k,v))
        records.extend(ks)
        print(json.dumps({'order':k,'records':len(ks),'seconds':round(time.time()-kt,3),'distinct_matrix_orders':len({r['matrix_order'] for r in ks}),'global_antiperiod_count':sum(r['global_antiperiod_h'] is not None for r in ks)}),flush=True)
    out={'phase':'II-KM','family':'tap_pair(k,v): x^k-x^v-1 over F3','engine':'python-flint 0.9.0 nmod_poly.factor + fmpz.factor','qualification':qualification,'orders':args.orders or [],'records':records,'runtime_seconds':time.time()-t}
    if args.out: args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'DONE','records':len(records),'qualification':qualification,'runtime_seconds':round(time.time()-t,3)}))
if __name__=='__main__':main()
