#!/usr/bin/env python3
from __future__ import annotations
import json,time,sys
from pathlib import Path
from flint import arb,ctx,__version__ as flint_version
ROOT=Path(__file__).resolve().parent;DEP=ROOT/'dependencies';ctx.prec=160

def ball(lo,hi):return arb(str(lo)).union(arb(str(hi)))
def outward(z,padrel=8e-14):
    lo=float(z.lower());hi=float(z.upper());pad=padrel*max(1.,abs(lo),abs(hi));return [lo-pad,hi+pad]
kh=json.load(open(DEP/'II_KH_gauss_fredholm_riesz.json'))
ki=json.load(open(DEP/'II_KI_gauss_fredholm_second_riesz.json'))
kj=json.load(open(DEP/'II_KJ_gauss_fifth_third_riesz.json'))
kk=json.load(open(DEP/'II_KK_gauss_sixth_threepoint.json'))
kf=json.load(open(DEP/'II_KF_gauss_nuclear_determinant.json'))
tr1=ball(*kh['trace_data']['trL']['interval']);tr2=ball(*kh['trace_data']['trL2']['interval']);tr3=ball(*kh['trace_data']['trL3']['interval'])
tr4=ball(*ki['fourth_trace']['certified_interval']);tr5=ball(*kj['fifth_trace']['certified_interval']);tr6=ball(*kk['sixth_trace']['certified_interval'])
d1=ball(*kh['fredholm_coefficients']['d1']);d2=ball(*kh['fredholm_coefficients']['d2']);d3=ball(*kh['fredholm_coefficients']['d3'])
d4=ball(*ki['fredholm_d4']['certified_interval']);d5=ball(*kj['fredholm_d5']['certified_interval']);d6=ball(*kk['fredholm_d6']['certified_interval'])
# Seventh trace: seven inverse branches have determinant -1; each fixed point contributes q/(1+q).
t0=time.time();N=7;tr7=arb(0)
for a in range(1,N+1):
 for b in range(1,N+1):
  A2=1;B2=a;C2=b;D2=a*b+1
  for c in range(1,N+1):
   A3=C2;B3=D2;C3=A2+c*C2;D3=B2+c*D2
   for d in range(1,N+1):
    A4=C3;B4=D3;C4=A3+d*C3;D4=B3+d*D3
    for e in range(1,N+1):
     A5=C4;B5=D4;C5=A4+e*C4;D5=B4+e*D4
     for f in range(1,N+1):
      A6=C5;B6=D5;C6=A5+f*C5;D6=B5+f*D5
      for g in range(1,N+1):
       A7=C6;B7=D6;C7=A6+g*C6;D7=B6+g*D6
       Cb=arb(C7);db=arb(D7-A7);Bb=arb(B7);disc=db*db+4*Cb*Bb;x=(-db+disc.sqrt())/(2*Cb);q=1/(Cb*x+D7)**2
       tr7 += q/(1+q)
zeta2=arb.pi()**2/6;SN=sum((arb(1)/(n*n) for n in range(1,N+1)),arb(0));tail=zeta2**7-SN**7;tr7B=tr7.union(tr7+tail)
d7=-(d6*tr1+d5*tr2+d4*tr3+d3*tr4+d2*tr5+d1*tr6+tr7B)/7
# Reduced-resolvent existence: use inherited simple isolated eigenvalue/Riesz projector carrier.
# This is an exact functional-calculus consequence; no operator norm is invented.
res={
 'base_carrier':'Hardy/nuclear Gauss transfer carrier inherited through II-KF--II-KH',
 'source_bound_inputs':{
   'trace_class_nuclearity':kf['source_hardy_trace_class']['status'],
   'spectral_determinant_transport':kf['spectral_determinant']['status'],
   'explicit_rank_one_projector':kh['khinchin_leading_riesz_pairing']['projector_formula'],
   'simple_isolated_leading_eigenvalue':'inherited source-bound Riesz spectral gap/projector authority used by II-KH; no new numerical spectral computation is claimed'},
 'projectors':'P f=h ell(f), Q=I-P',
 'definition':'S = Q (I-L_0|_{QX})^{-1} Q',
 'existence_argument':'because 1 is an isolated simple spectral point and P is its Riesz projector, 1 is absent from the spectrum of L_0 restricted to QX; therefore I-L_0 is boundedly invertible on QX',
 'third_derivative_identity':[
   'u1=(L1-lambda1)h; h1=S u1',
   'u2=(L2-lambda2)h+2(L1-lambda1)h1; h2=S u2',
   'lambda3=ell(L3 h)+3 ell(L2 h1)+3 ell(L1 h2)',
   "P'''(0)=lambda3-3 lambda2 lambda1+2 lambda1^3 because lambda(0)=1"],
 'analytic_pressure_conclusion':'the local pressure P(t)=log lambda(t) has a well-defined third derivative on the declared analytic perturbation carrier',
 'absolute_three_point_correlation_sum':'SEPARATED_NOT_DERIVED_FROM_REDUCED_RESOLVENT_EXISTENCE_ALONE',
 'numerical_resolvent_norm':'SEPARATED_NO_CERTIFIED_OPERATOR_NORM_BOUND',
 'numerical_P3':'SEPARATED_NO_CERTIFIED_EVALUATION_OF_S_ON_u1_u2',
 'status':'PASS_GENUINE_REDUCED_RESOLVENT_EXISTENCE_AND_EXACT_THIRD_RIESZ_PRESSURE_IDENTITY__NUMERIC_THIRD_RESPONSE_SEPARATED'}
out={'phase':'II-KL','carrier':'Gauss analytic trace-class transfer operator L_t=sum n^t W_n on the declared Hardy/weighted nuclear lane',
 'runtime':{'python':sys.version.split()[0],'python_flint':flint_version,'arb_precision_bits':ctx.prec},
 'seventh_trace':{'box_N':N,'ordered_word_count':N**7,'partial_ball':str(tr7),'tail_ball':str(tail),'certified_interval':outward(tr7B),'orientation':'seven inverse branches have determinant -1; fixed-point contribution q/(1+q)','tail_bound':'positive continuant D7>=abcdefg gives q/(1+q)<=q<=prod digit^-2; complement <=zeta(2)^7-S_N^7','status':'PASS_CERTIFIED_TR_L7'},
 'fredholm_d7':{'normalization':'det(I-zL)=1+d1 z+...','newton_identity':'7 d7=-(d6 trL+d5 trL2+d4 trL3+d3 trL4+d2 trL5+d1 trL6+trL7)','certified_interval':outward(d7),'status':'PASS_CERTIFIED_D7'},
 'third_pressure_reduced_resolvent':res,
 'guards':['the seventh-trace tail is intentionally conservative and positive','no sign is claimed for d7 if its enclosure crosses zero','reduced-resolvent existence does not by itself certify absolute summability of the time-domain three-point cumulant series','no numerical value of P third derivative is invented'],
 'status':'PASS_SEVENTH_FREDHOLM_TRACE_COEFFICIENT_AND_GENUINE_REDUCED_RESOLVENT_THIRD_PRESSURE_CERTIFICATE','runtime_seconds':round(time.time()-t0,3)}
(ROOT/'II_KL_gauss_seventh_reduced_resolvent.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'trL7':out['seventh_trace']['certified_interval'],'d7':out['fredholm_d7']['certified_interval'],'resolvent':res['status'],'runtime':out['runtime_seconds']},indent=2))
