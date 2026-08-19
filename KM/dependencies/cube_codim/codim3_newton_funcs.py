#!/usr/bin/env python3
from __future__ import annotations
import json,time,sys,hashlib
from pathlib import Path
import sympy as sp
from flint import arb,ctx,__version__ as flint_version
ROOT=Path(__file__).resolve().parent; SRC=ROOT/'source_recovery';ctx.prec=160
split=arb('0.5').atan();quarter=arb.pi()/4
rS,CS,SS=sp.symbols('r C S')
xS=rS*CS;yS=rS*SS
psiS=(4-xS*xS)*(4-yS*yS)*(9-(xS+yS)**2)*(9-(xS-yS)**2)
pS=(9+xS*xS-yS*yS)*yS;qS=(9-xS*xS+yS*yS)*xS
Bexpr=-sp.diff(psiS,rS);Aexpr=(pS+qS)*rS
fB=sp.lambdify((rS,CS,SS),Bexpr,'math');fBr=sp.lambdify((rS,CS,SS),sp.diff(Bexpr,rS),'math')
fA=sp.lambdify((rS,CS,SS),Aexpr,'math');fAr=sp.lambdify((rS,CS,SS),sp.diff(Aexpr,rS),'math')

def psi(x,y):return (4-x*x)*(4-y*y)*(9-(x+y)**2)*(9-(x-y)**2)
def pp(x,y):return (9+x*x-y*y)*y
def qq(x,y):return (9-x*x+y*y)*x
def R(th,branch):
 c=th.cos();s=th.sin();return 2/c if branch==0 else 3/(c+s)
def root_bracket(th,levbox,branch,it=54):
 rr=R(th,branch);cc=th.cos();ss=th.sin();lolev=levbox.lower();hilev=levbox.upper()
 a,b=0.,1.
 for _ in range(it):
  m=(a+b)/2;z=psi(arb(m)*rr*cc,arb(m)*rr*ss)
  if z>hilev:a=m
  else:b=m
 lo=a;a,b=0.,1.
 for _ in range(it):
  m=(a+b)/2;z=psi(arb(m)*rr*cc,arb(m)*rr*ss)
  if z<lolev:b=m
  else:a=m
 return lo,b

def poly_mul(a,b):
 out=[arb(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def radial_B_Br(r,th):
 c=th.cos();s=th.sin();bs=[c*c,s*s,(c+s)**2,(c-s)**2]; aa=[arb(4),arb(4),arb(9),arb(9)]
 co=[arb(1)]
 for A,b in zip(aa,bs):co=poly_mul(co,[A,-b])
 s2=r*r
 P1=sum((arb(i)*co[i]*s2**(i-1) for i in range(1,len(co))),arb(0))
 P2=sum((arb(i*(i-1))*co[i]*s2**(i-2) for i in range(2,len(co))),arb(0))
 B=-2*r*P1;Br=-2*P1-4*s2*P2
 return B,Br

def A_Ar(r,th):
 c=th.cos();s=th.sin();x=r*c;y=r*s
 p=(9+x*x-y*y)*y;q=(9-x*x+y*y)*x;P=p+q
 Px=2*x*y + 9-3*x*x+y*y
 Py=9+x*x-3*y*y+2*x*y
 A=r*P;Ar=P+r*(Px*c+Py*s)
 return A,Ar

def outward(z,padrel=2e-14):
 lo=float(z.lower());hi=float(z.upper());pad=padrel*max(1.,abs(lo),abs(hi));return [lo-pad,hi+pad]
def integrate(la,lb,N=600,with_deriv=True):
 lev=arb(str(la)).union(arb(str(lb)));u=arb(0);du=arb(0);cells=0;minB=None
 for branch,(T0,T1) in enumerate([(arb(0),split),(split,quarter)]):
  for i in range(N):
   t0=T0+(T1-T0)*i/N;t1=T0+(T1-T0)*(i+1)/N;th=t0.union(t1);w=t1-t0
   lo,hi=root_bracket(th,lev,branch);tt=arb(lo).union(arb(hi));r=tt*R(th,branch)
   cc=th.cos();ss=th.sin();B=fB(r,cc,ss);Br=fBr(r,cc,ss)
   if not (B>0):raise ArithmeticError(('B sign',la,lb,branch,i,str(B)))
   A=fA(r,cc,ss);Ar=fAr(r,cc,ss);F=A/(lev*B);u+=2*F*w
   if with_deriv:
    dF=-A/(lev*lev*B)-(Ar*B-A*Br)/(lev*B**3);du+=2*dF*w
   xlo=float(B.lower());minB=xlo if minB is None else min(minB,xlo);cells+=1
 return {'level':[la,lb],'u':outward(u),'du_dc':outward(du) if with_deriv else None,'cells':cells,'min_B_lower':minB}

