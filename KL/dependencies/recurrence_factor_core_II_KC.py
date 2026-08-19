#!/usr/bin/env python3
from __future__ import annotations
import json,math,hashlib,time
from collections import Counter,defaultdict
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parent
x=sp.symbols('x');P=3
order10=json.loads((ROOT/'II_KC_binary_recurrence_mod3_order10.json').read_text())

def coefflow(poly):
 pp=sp.Poly(poly,x,modulus=P);return [int(pp.nth(i))%P for i in range(pp.degree()+1)]
def mulmod(a,b,g):
 d=len(g)-1;tmp=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b):tmp[i+j]=(tmp[i+j]+ai*bj)%P
 for n in range(len(tmp)-1,d-1,-1):
  c=tmp[n]%P
  if c:
   for i in range(d):tmp[n-d+i]=(tmp[n-d+i]-c*g[i])%P
 return tmp[:d]
def powx(n,g):
 d=len(g)-1;one=[1]+[0]*(d-1);base=[0]*d
 if d==1:base[0]=(-g[0])%P
 else:base[1]=1
 out=one
 while n:
  if n&1:out=mulmod(out,base,g)
  base=mulmod(base,base,g);n//=2
 return out
def root_order(gpoly):
 g=coefflow(gpoly);d=len(g)-1;N=P**d-1;o=N;one=[1]+[0]*(d-1)
 for r,e in sp.factorint(N).items():
  for _ in range(e):
   if o%r==0 and powx(o//r,g)==one:o//=r
   else:break
 return int(o)
def charpoly(c):
 k=len(c);e=x**k
 for i,a in enumerate(c):e-=int(a)*x**i
 return sp.Poly(e,x,modulus=P)
def factor_record(c):
 cp=charpoly(c);_,fac=sp.factor_list(cp,modulus=P);orders=[];parts=[]
 for g,e in fac:
  ro=root_order(g);pp=1
  while pp<e:pp*=P
  bo=ro*pp;orders.append(bo);parts.append((g.degree(),int(e),ro,bo,str(g.as_expr())))
 mo=math.lcm(*orders) if orders else 1;gfull=coefflow(cp)
 one=[1]+[0]*(len(c)-1);minus=[2]+[0]*(len(c)-1)
 anti=(mo%2==0 and powx(mo//2,gfull)==minus)
 return cp,parts,mo,(mo//2 if anti else None)

def mask_coeff(mask,k):return [(mask>>i)&1 for i in range(k)]
