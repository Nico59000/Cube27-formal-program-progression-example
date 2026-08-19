#!/usr/bin/env python3
from __future__ import annotations
import json, math, time, csv
from pathlib import Path
from collections import defaultdict, Counter
from flint import nmod_poly, fmpz, __version__ as flint_version
ROOT=Path(__file__).resolve().parent
P=3
FACT={}
X=nmod_poly([0,1],P); ONE=nmod_poly([1],P); MINUS=nmod_poly([2],P)

def v2(n:int)->int:
    return (n & -n).bit_length()-1

def factor_Z(n:int):
    return [(int(p),int(e)) for p,e in fmpz(n).factor()]

def root_order(g:nmod_poly)->int:
    d=g.degree(); N=P**d-1; o=N
    fac=FACT.setdefault(d,factor_Z(N))
    for r,e in fac:
        for _ in range(e):
            if o%r==0 and X.pow_mod(o//r,g)==ONE:
                o//=r
            else: break
    return int(o)

def factor_record(k:int,v:int):
    coeff=[0]*(k+1); coeff[0]=2; coeff[v]=2; coeff[k]=1
    cp=nmod_poly(coeff,P); unit,fac=cp.factor()
    orders=[]; parts=[]
    for g,e in fac:
        ro=root_order(g); pp=1
        while pp<e: pp*=P
        bo=ro*pp; orders.append(bo)
        parts.append({'degree':int(g.degree()),'multiplicity':int(e),'root_order':int(ro),'block_order':int(bo),'factor':str(g)})
    mo=math.lcm(*orders) if orders else 1
    # determinant theorem gives zero antiperiod for odd k. Check directly only for even k.
    if k%2:
        anti=None; anti_mode='ZERO_BY_ODD_DETERMINANT_THEOREM'
    else:
        anti=(mo//2 if (mo%2==0 and X.pow_mod(mo//2,cp)==MINUS) else None); anti_mode='DIRECT_POWER_MOD'
    return {'recurrence_order':k,'tap_value':v,'reflected_value':k-v,'order_plus_value':k+v,
            'matrix_order':int(mo),'global_antiperiod_h':anti,'antiperiod_decision_mode':anti_mode,
            'factor_degree_multiplicity':[[p['degree'],p['multiplicity'],p['root_order'],p['block_order']] for p in parts],
            'factor_strings':[p['factor'] for p in parts],
            'irreducible_factor_count':len(parts),
            'gcd_matrix_with_order':math.gcd(mo,k),'gcd_matrix_with_value':math.gcd(mo,v),
            'gcd_matrix_with_order_plus_value':math.gcd(mo,k+v),'v2_matrix_order':v2(mo),
            'matrix_order_equals_order':mo==k,'matrix_order_equals_order_plus_value':mo==k+v,
            'k_divides_matrix_order':mo%k==0,'v_divides_matrix_order':mo%v==0,
            'k_plus_v_divides_matrix_order':mo%(k+v)==0}

def sweep(k:int):
    t=time.time(); rows=[factor_record(k,v) for v in range(1,k)]
    out={'k':k,'engine':'python-flint nmod_poly factor + fmpz factor','python_flint':flint_version,
         'records':rows,'record_count':len(rows),'runtime_seconds':round(time.time()-t,6)}
    (ROOT/f'II_KL_recurrence_chunk_{k}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    return out

def load_prior():
    rec=[]
    for fn in ['II_KG_recurrence_order_value_45_55.json','II_KH_recurrence_order_value_56_65.json','II_KI_recurrence_order_value_66_75.json','II_KJ_recurrence_order_value_76_85.json']:
        rec+=json.load(open(ROOT/'dependencies'/fn))['records']
    # KK records excluding order89 probes, which are superseded here by the full FLINT sweep.
    kk=json.load(open(ROOT/'dependencies'/'II_KK_recurrence_order_value_86_95.json'))['records']
    rec += [r for r in kk if r['recurrence_order']!=89]
    return rec

def main():
    t=time.time(); chunks={}
    for k in [89]+list(range(96,106)):
        chunks[k]=sweep(k)
        print('swept',k,'records',chunks[k]['record_count'],'sec',chunks[k]['runtime_seconds'],flush=True)
    rows89=chunks[89]['records']; rows_new=sum((chunks[k]['records'] for k in range(96,106)),[])
    # direct full-89 diagnostics
    # Qualification against the nine II-KK selected order89 probes.
    oldkk=json.load(open(ROOT/'dependencies'/'II_KK_recurrence_order_value_86_95.json'))['records']
    old89={(r['recurrence_order'],r['tap_value']):r for r in oldkk if r['recurrence_order']==89}
    new89={(r['recurrence_order'],r['tap_value']):r for r in rows89}
    q89=[]
    for key,r0 in sorted(old89.items()):
        rn=new89[key]
        q89.append({'tap_value':key[1],'old_matrix_order':r0['matrix_order'],'new_matrix_order':rn['matrix_order'],'match':r0['matrix_order']==rn['matrix_order'],'old_antiperiod':r0['global_antiperiod_h'],'new_antiperiod':rn['global_antiperiod_h']})
    qual89={'records':q89,'matches':sum(x['match'] and x['old_antiperiod']==x['new_antiperiod'] for x in q89),'total':len(q89),'status':'PASS_9_OF_9_SELECTED_ORDER89_CERTIFICATES_MATCH'}
    assert qual89['matches']==qual89['total']==9
    s89={'record_count':len(rows89),'distinct_matrix_orders':len({r['matrix_order'] for r in rows89}),
         'factor_count_histogram':dict(sorted(Counter(r['irreducible_factor_count'] for r in rows89).items())),
         'k_divides_matrix_order':sum(r['k_divides_matrix_order'] for r in rows89),
         'v_divides_matrix_order':sum(r['v_divides_matrix_order'] for r in rows89),
         'k_plus_v_divides_matrix_order':sum(r['k_plus_v_divides_matrix_order'] for r in rows89),
         'matrix_order_equals_k':sum(r['matrix_order_equals_order'] for r in rows89),
         'matrix_order_equals_k_plus_v':sum(r['matrix_order_equals_order_plus_value'] for r in rows89),
         'max_matrix_order':max(r['matrix_order'] for r in rows89),
         'min_matrix_order':min(r['matrix_order'] for r in rows89),
         'global_antiperiod_count':0,
         'runtime_seconds':chunks[89]['runtime_seconds'],
         'old_resource_issue_interpretation':'the prior bounded-window failure was implementation/resource behavior of the SymPy route, not evidence that order 89 is intrinsically computationally singular; the FLINT factor engine completes all 88 tap values.'}
    by={(r['recurrence_order'],r['tap_value']):r for r in rows_new}
    reflection=[]; violations=[]; cases=Counter(); fixed=[]
    for k in [96,98,100,102,104]:
        rr=by[k,k//2]; fixed.append({'k':k,'v':k//2,'matrix_order':rr['matrix_order'],'global_antiperiod_h':rr['global_antiperiod_h'],'ord_equals_4k':rr['matrix_order']==4*k,'anti_equals_2k':rr['global_antiperiod_h']==2*k})
        for v in range(1,k//2):
            a=by[k,v];b=by[k,k-v]
            if v%2==1:
                N=a['matrix_order']; anti=a['global_antiperiod_h'] is not None
                pred=N//math.gcd(N,N//2-1) if anti else math.lcm(2,N)
                cls=('equal' if v2(N)>=2 else 'half') if anti else ('equal' if N%2==0 else 'double')
                q={'k':k,'v':v,'kv':k-v,'order_v':N,'order_reflected':b['matrix_order'],'predicted':pred,'classification':cls,'verified':pred==b['matrix_order']}
                reflection.append(q);cases[cls]+=1
                if not q['verified']:violations.append(q)
    assert not violations and all(q['ord_equals_4k'] and q['anti_equals_2k'] for q in fixed)
    # combined collision quotient
    prior=load_prior(); combined=prior+rows89+rows_new
    groups=defaultdict(list)
    for r in combined: groups[int(r['matrix_order'])].append((int(r['recurrence_order']),int(r['tap_value'])))
    newpairs={(89,r['tap_value']) for r in rows89}|{(r['recurrence_order'],r['tap_value']) for r in rows_new}
    coll=[]
    for o,ps in sorted(groups.items()):
        u=sorted(set(ps))
        if len(u)>1 and any(p in newpairs for p in u):
            ks=sorted({p[0] for p in u});coll.append({'matrix_order':o,'order_value_pairs':[list(p) for p in u],'class_size':len(u),'recurrence_orders':ks,'cross_order':len(ks)>1,'contains_full89':any(p[0]==89 for p in u),'contains_fixed_center':any(p[0]%2==0 and p[1]==p[0]//2 for p in u)})
    hist=Counter(c['class_size'] for c in coll); largest=max(coll,key=lambda c:c['class_size']) if coll else None
    # full summaries and divisibility
    summaries={}
    for k in range(96,106):
        rs=chunks[k]['records']; summaries[str(k)]={'families':len(rs),'distinct_matrix_orders':len({r['matrix_order'] for r in rs}),
            'global_antiperiod_count':sum(r['global_antiperiod_h'] is not None for r in rs),'max_matrix_order':max(r['matrix_order'] for r in rs),
            'k_divides_matrix_order':sum(r['k_divides_matrix_order'] for r in rs),'v_divides_matrix_order':sum(r['v_divides_matrix_order'] for r in rs),
            'k_plus_v_divides_matrix_order':sum(r['k_plus_v_divides_matrix_order'] for r in rs),'runtime_seconds':chunks[k]['runtime_seconds']}
    # theorem search: fixed-center divisibility implies k|ord at centers, reflection-class consequences. Search exact repeated ratio ord/k.
    ratio_classes=defaultdict(list)
    for r in rows_new:
        if r['matrix_order']%r['recurrence_order']==0:
            ratio=r['matrix_order']//r['recurrence_order'];
            if ratio<=1000: ratio_classes[int(ratio)].append([r['recurrence_order'],r['tap_value']])
    common_ratios=[{'ratio':q,'pairs':ps,'count':len(ps)} for q,ps in sorted(ratio_classes.items()) if len(ps)>=2]
    formula_hits={'ord_eq_k':[[r['recurrence_order'],r['tap_value']] for r in rows_new+rows89 if r['matrix_order']==r['recurrence_order']],
                  'ord_eq_k_plus_v':[[r['recurrence_order'],r['tap_value']] for r in rows_new+rows89 if r['matrix_order']==r['recurrence_order']+r['tap_value']]}
    out={'phase':'II-KL','family':'tap_pair(k,v): x^k-x^v-1 over F3',
         'engine_upgrade':{'engine':'python-flint nmod_poly.factor + fmpz.factor with cached factorization of 3^d-1','old_sympy89_resource_issue_resolved':True,'full_order89_completed':True,'full_order89':s89,'qualification_against_II_KK_selected_order89':qual89,
                           'guard':'89 is a Fibonacci number and is retained as a structurally interesting coordinate, but the old runtime overrun is not itself mathematical evidence of specialness.'},
         'campaign_96_105':{'mode':'FULL_ALL_TAP_VALUES','orders':list(range(96,106)),'record_count':len(rows_new),'summaries':summaries,'aggregate_runtime_seconds':round(sum(chunks[k]['runtime_seconds'] for k in range(96,106)),6)},
         'records_89':rows89,'records_96_105':rows_new,
         'reflection_theorem':{'verified_pairs':sum(q['verified'] for q in reflection),'violations':violations,'case_counts':dict(cases),'fixed_centers':fixed,'status':'PASS_ALL_124_APPLICABLE_EVEN_K_ODD_V_REFLECTION_PAIRS_AND_FIVE_FIXED_CENTERS'},
         'collision_quotient':{'scope':'exact prior atlas 45-95 with full order89 replacing prior probes, plus full 96-105','classes_involving_new_pairs':len(coll),'cross_order_classes':sum(c['cross_order'] for c in coll),'classes_containing_order89':sum(c['contains_full89'] for c in coll),'classes_containing_fixed_center':sum(c['contains_fixed_center'] for c in coll),'component_size_histogram':{str(k):v for k,v in sorted(hist.items())},'largest_component':largest,'classes':coll,'status':'PASS_EXACT_COLLISION_QUOTIENT_WITH_FULL89_REPAIR'},
         'divisibility_theorem_search':{'common_small_integer_order_over_k_ratios':common_ratios,'formula_hits':formula_hits,'statement':'fixed-center theorem gives universal ratio ord/k=4 at v=k/2 for even k; outside that locus the exact atlas shows multiple ratio/divisibility strata rather than one linear law','status':'PASS_FIXED_CENTER_RATIO4_THEOREM_PRESERVED__GENERAL_DIVISIBILITY_LAW_NOT_PROMOTED'},
         'guards':['all records are factor certificates; no 3^k state enumeration','odd global-antiperiod ZERO uses the determinant theorem and is not inferred from runtime','full order89 supersedes only the old selected order89 probes, not unrelated prior records','no numerical collision/divisibility identifies recurrence with Golden, Stone, Fibonacci project, D5 or geometric carriers'],
         'status':'PASS_FULL89_FLINT_REPAIR_FULL96_105_FACTORIZATION_REFLECTION_COLLISION_AND_DIVISIBILITY_ATLAS'}
    (ROOT/'II_KL_recurrence_order_value_89_96_105.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    fields=['recurrence_order','tap_value','reflected_value','matrix_order','global_antiperiod_h','gcd_matrix_with_order','gcd_matrix_with_value','gcd_matrix_with_order_plus_value','v2_matrix_order','k_divides_matrix_order','v_divides_matrix_order','k_plus_v_divides_matrix_order']
    with (ROOT/'II_KL_recurrence_order_value_89_96_105.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:r.get(k) for k in fields} for r in rows89+rows_new)
    print(json.dumps({'full89':s89,'new96_105':len(rows_new),'reflection_verified':out['reflection_theorem']['verified_pairs'],'collision_classes':len(coll),'cross_order':out['collision_quotient']['cross_order_classes'],'largest':largest,'formula_hits':formula_hits,'runtime_total':round(time.time()-t,3)},indent=2))

if __name__=='__main__': main()
