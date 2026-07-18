#!/usr/bin/env python3
"""Canonical exhibit set for the Company-in-a-Box. Navy/amber/teal house palette.
Each function saves a crisp 2x PNG. Run: python3 charts.py <outdir>  (builds all).
Import individual functions to build one exhibit into a specific doc folder."""
import sys, pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

NAVY='#0f3d5c'; AMBER='#c8862a'; TEAL='#12856f'; SLATE='#5a6472'; LIGHT='#e2e8ef'; RED='#c0392b'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.edgecolor':'#c8d2dc',
    'axes.labelcolor':'#1a1f2b','text.color':'#1a1f2b','xtick.color':SLATE,'ytick.color':SLATE,
    'figure.dpi':200,'savefig.dpi':200,'axes.spines.top':False,'axes.spines.right':False})

def _save(fig, path):
    fig.tight_layout(); fig.savefig(path, bbox_inches='tight', facecolor='white'); plt.close(fig)

def market_growth(path):
    # Only verified points: 2025 actuals (solar 267,032; HP 60,000+). 2026 = market +50% forecast, labelled.
    fig, ax = plt.subplots(figsize=(6.6,3.5))
    yrs=['2025 (actual)','2026 (forecast +50%)']; solar=[267,401]; hp=[60,90]
    x=np.arange(len(yrs)); w=0.34
    b1=ax.bar(x-w/2, solar, w, label='Solar PV installs (000s)', color=[NAVY,'#3a6a88'])
    b2=ax.bar(x+w/2, hp, w, label='Heat pump installs (000s)', color=[AMBER,'#e0a95a'])
    for i,v in enumerate(solar): ax.text(i-w/2,v+6,f'{v}',ha='center',fontsize=9.5,color=NAVY,fontweight='bold')
    for i,v in enumerate(hp): ax.text(i+w/2,v+6,f'{v}',ha='center',fontsize=9.5,color=AMBER,fontweight='bold')
    ax.set_ylabel('Installations (thousands)'); ax.set_xticks(x); ax.set_xticklabels(yrs)
    ax.legend(frameon=False, fontsize=9, loc='upper left'); ax.set_ylim(0,460)
    ax.set_title('UK renewable installations — 2025 record, +50% forecast for 2026', fontsize=11, color=NAVY, fontweight='bold', pad=10)
    ax.text(0.5,-0.22,'2025 = verified MCS actuals · 2026 = market +50% growth forecast applied (illustrative)',
            transform=ax.transAxes, ha='center', fontsize=7.5, color=SLATE)
    _save(fig, path)

def competitor_matrix(path):
    fig, ax = plt.subplots(figsize=(6.6,4.6))
    # x = UK-nativeness, y = renewables vertical depth
    pts={'SalesOps CRM':(3.0,8.2,TEAL,'*',420),'Payaca':(9.0,8.8,NAVY,'o',180),'Reonic':(5.5,8.5,AMBER,'o',180),
         'Commusoft':(8.5,5.0,SLATE,'o',150),'Simpro':(6.5,4.0,SLATE,'o',150),
         'BigChange':(7.5,3.0,SLATE,'o',150),'Jobber/ServiceM8':(4.0,2.2,SLATE,'o',150)}
    for name,(x,y,c,m,s) in pts.items():
        ax.scatter(x,y,s=s,c=c,marker=m,edgecolors='white',linewidths=1.2,zorder=3)
        ax.annotate(name,(x,y),xytext=(0,-16 if name!='SalesOps CRM' else 14),textcoords='offset points',
                    ha='center',fontsize=8.5,color='#1a1f2b',fontweight='bold' if name=='SalesOps CRM' else 'normal')
    ax.axhline(5,color=LIGHT,lw=1,zorder=1); ax.axvline(5,color=LIGHT,lw=1,zorder=1)
    ax.set_xlim(0,10); ax.set_ylim(0,10)
    ax.set_xlabel('UK-native presence & localisation  →'); ax.set_ylabel('Renewables vertical depth  →')
    ax.set_title('Competitive positioning — the renewables-depth vs UK-presence gap', fontsize=11, color=NAVY, fontweight='bold', pad=10)
    ax.text(0.3,9.3,'Deep vertical\nfit',fontsize=7.5,color=SLATE); ax.text(7.7,0.4,'UK-established',fontsize=7.5,color=SLATE)
    _save(fig, path)

def pricing_tiers(path):
    fig, ax = plt.subplots(figsize=(6.6,3.4))
    tiers=['1-10','11-20','21-30','31-69','70-199','200-499','500+']; pln=[100,90,80,70,60,50,40]; gbp=[20,18,16,14,12,10,8]
    x=np.arange(len(tiers))
    ax.plot(x,pln,'-o',color=NAVY,label='PLN / user / month',lw=2)
    ax.plot(x,gbp,'-o',color=TEAL,label='≈ GBP / user / month',lw=2)
    for i,v in enumerate(pln): ax.text(i,v+3,f'{v}',ha='center',fontsize=8,color=NAVY)
    for i,v in enumerate(gbp): ax.text(i,v-6,f'£{v}',ha='center',fontsize=8,color=TEAL)
    ax.set_xticks(x); ax.set_xticklabels(tiers); ax.set_xlabel('Users (seats)'); ax.set_ylabel('Price / user / month')
    ax.legend(frameon=False,fontsize=9); ax.set_ylim(0,115)
    ax.set_title("RRUP per-seat pricing ladder (Polish list) — vs Payaca's £999+/mo flat", fontsize=10.5, color=NAVY, fontweight='bold', pad=10)
    _save(fig, path)

def sales_funnel(path):
    fig, ax = plt.subplots(figsize=(6.2,3.8))
    stages=['Outreach','Replies','Demos','Trials','Paid']; vals=[1000,150,60,30,12]
    colors=[NAVY,'#1d5578',TEAL,AMBER,'#b8791f']
    maxw=1.0
    for i,(s,v,c) in enumerate(zip(stages,vals,colors)):
        w=maxw*(v/vals[0])**0.5
        ax.add_patch(plt.Rectangle((0.5-w/2,len(stages)-1-i),w,0.8,color=c))
        ax.text(0.5,len(stages)-1-i+0.4,f'{s}: {v:,}',ha='center',va='center',color='white',fontsize=9.5,fontweight='bold')
    ax.set_xlim(0,1); ax.set_ylim(-0.2,len(stages)); ax.axis('off')
    ax.set_title('Illustrative acquisition funnel (assumption-based — validate with pilot)', fontsize=10.5, color=NAVY, fontweight='bold')
    _save(fig, path)

def scenario_fan(path):
    fig, ax = plt.subplots(figsize=(6.6,3.6))
    yrs=['Year 1','Year 2','Year 3']; x=np.arange(3)
    base=[48,168,360]; bear=[22,86,190]; bull=[80,300,640]
    ax.fill_between(x,bear,bull,color=NAVY,alpha=0.12,label='Bear–Bull range')
    ax.plot(x,base,'-o',color=NAVY,lw=2.4,label='Base case'); ax.plot(x,bull,'--',color=TEAL,lw=1.5,label='Bull')
    ax.plot(x,bear,'--',color=RED,lw=1.5,label='Bear')
    for i,v in enumerate(base): ax.text(i,v+14,f'£{v}k',ha='center',fontsize=8.5,color=NAVY,fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylabel('Illustrative UK revenue (£000s)')
    ax.legend(frameon=False,fontsize=8.5,loc='upper left')
    ax.set_title('Revenue scenario fan — ILLUSTRATIVE, driven by Assumptions Register (⚠️)', fontsize=10, color=NAVY, fontweight='bold', pad=10)
    _save(fig, path)

def risk_heatmap(path):
    fig, ax = plt.subplots(figsize=(5.6,4.4))
    grid=np.array([[1,2,3,3,4],[2,2,3,4,4],[2,3,3,4,5],[3,3,4,5,5],[3,4,5,5,5]])
    cmap=matplotlib.colors.LinearSegmentedColormap.from_list('r',['#e8f3ef','#f6e6c9','#eec07a','#dd8a6a','#c0392b'])
    ax.imshow(grid,cmap=cmap,aspect='auto',origin='lower',vmin=1,vmax=5)
    # place a few named risks
    risks={'Deal ambiguity':(3,4),'Polsat claim':(1,3),'Competition':(3,3),'50/50 deadlock':(2,4),'Localisation gap':(2,2)}
    for name,(cx,cy) in risks.items():
        ax.text(cx,cy,name,ha='center',va='center',fontsize=7.2,color='#1a1f2b',fontweight='bold')
    ax.set_xticks(range(5)); ax.set_xticklabels(['V.Low','Low','Med','High','V.High'],fontsize=8)
    ax.set_yticks(range(5)); ax.set_yticklabels(['V.Low','Low','Med','High','V.High'],fontsize=8)
    ax.set_xlabel('Likelihood'); ax.set_ylabel('Impact')
    ax.set_title('Risk heatmap — likelihood × impact', fontsize=11, color=NAVY, fontweight='bold', pad=10)
    _save(fig, path)

ALL = {'market_growth':market_growth,'competitor_matrix':competitor_matrix,'pricing_tiers':pricing_tiers,
       'sales_funnel':sales_funnel,'scenario_fan':scenario_fan,'risk_heatmap':risk_heatmap}

if __name__ == '__main__':
    outdir = pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.'); outdir.mkdir(parents=True, exist_ok=True)
    only = sys.argv[2] if len(sys.argv)>2 else None
    for name, fn in ALL.items():
        if only and name != only: continue
        p = outdir / f'{name}.png'; fn(str(p)); print('built', p)
