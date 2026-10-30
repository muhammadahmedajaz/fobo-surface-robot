"""Draw a conceptual FOBO component layout from recovered build descriptions.

Positions are schematic. This is not an as-built dimensional drawing.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch, Circle, Rectangle

ROOT = Path(__file__).resolve().parents[1]
INK, RED, TEAL, GREY, GOLD = '#182b3a', '#b52b3a', '#087f8c', '#e4e9ec', '#e9c46a'


def draw():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none', 'svg.hashsalt': 'fobo-mechanical-2026'})
    fig, ax = plt.subplots(figsize=(13.5, 9))
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 13.5), ylim=(0, 9))
    ax.axis('off')
    ax.text(.45, 8.65, 'FOBO / PHYSICAL ARRANGEMENT', fontsize=21, weight='bold', color=INK)
    ax.text(.45, 8.28, 'Conceptual top view from build notes and footage • no dimensions inferred', fontsize=11, color=INK)

    ax.add_patch(FancyBboxPatch((.45, .9), (7.25), 7.0, boxstyle='round,pad=.15', facecolor='#f4f7f8', edgecolor='none'))
    for x in (1.4, 5.5):
        shape=[(x,1.35),(x+1.45,1.35),(x+1.45,6.8),(x+.72,7.45),(x,6.8)]
        ax.add_patch(Polygon(shape, closed=True, facecolor=RED, edgecolor=INK, lw=1.4))
        ax.add_patch(Rectangle((x+.18,1.62),1.08,4.95, facecolor='#292d32', edgecolor='none'))
        ax.text(x+.72,4.1,'HULL',rotation=90,ha='center',va='center',color='white',weight='bold',fontsize=12)
    for y in (3.0,5.8):
        ax.add_patch(Rectangle((2.85,y),2.65,.25,facecolor='#707c85',edgecolor='none'))
    ax.add_patch(FancyBboxPatch((2.95,3.45),2.45,2.05,boxstyle='round,pad=.08',facecolor=GREY,edgecolor=INK,lw=1.3))
    ax.text(4.17,5.04,'CENTRAL BAY',ha='center',fontsize=12,weight='bold',color=INK)
    ax.text(4.17,4.67,'Electronics / dry box',ha='center',fontsize=10,color=INK)
    ax.add_patch(FancyBboxPatch((3.44,3.77),1.47,.52,boxstyle='round,pad=.05',facecolor=GOLD,edgecolor=INK,lw=1))
    ax.text(4.17,4.02,'Battery',ha='center',va='center',fontsize=11,color=INK)

    for x in (2.12,6.22):
        for y in (6.3,2.65):
            ax.add_patch(Circle((x,y),.28,facecolor=TEAL,edgecolor='white',lw=1.7))
            ax.annotate('',xy=(x+.52,y+.43),xytext=(x,y),arrowprops={'arrowstyle':'->','color':TEAL,'lw':2})
        ax.add_patch(Circle((x,1.58),.18,facecolor='white',edgecolor=INK,lw=1.4))
        ax.plot([x-.40,x+.40],[1.58,1.58],color=INK,lw=4,solid_capstyle='round')
    ax.text(4.17,7.52,'FRONT',ha='center',va='bottom',fontsize=11,weight='bold',color=INK)
    ax.text(4.17,1.05,'REAR',ha='center',va='bottom',fontsize=11,weight='bold',color=INK)

    notes=[
        (7.8,'TWO HULLS','XPS core with fiberglass covering.\nShape here is schematic; use photos\nfor the physical outline.'),
        (6.3,'CENTRAL COMPARTMENT','Electronics bay, separate waterproof\nbox and centrally placed battery\nwere described in the build notes.'),
        (4.8,'FOUR ROTATING UNITS','Four 680 RPM DC motor / propeller\nunits on MG996R servo mounts.\nTeal symbols mark approximate locations.'),
        (3.3,'TWO REAR BOOSTERS','Rear propellers appear in the footage.\nTheir controller and wiring remain\nto be documented.'),
        (1.8,'READ WITH THE RECEIVER CODE','The supplied RX uses CH2 for all four\nservo commands. Physical motor-index\nmapping is not established by this sketch.'),
    ]
    for y,title,body in notes:
        ax.text(8.15,y,title,fontsize=11,weight='bold',color=INK,va='top')
        ax.text(8.15,y-.32,body,fontsize=10.2,color=INK,va='top',linespacing=1.45)
    ax.text(.45,.34,'LAYOUT SKETCH • Approximate reported envelope: 23 × 17 × 13 in • Mounting positions are schematic.',fontsize=9,color='#52616b')
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    out=ROOT/'assets/figures'
    out.mkdir(parents=True,exist_ok=True)
    fig.savefig(out/'mechanical-layout-concept.png',dpi=160)
    fig.savefig(out/'mechanical-layout-concept.svg')
    plt.close(fig)


def save(fig, name):
    out = ROOT/'assets/figures'
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out/(name+'.png'), dpi=160)
    fig.savefig(out/(name+'.svg'))
    plt.close(fig)


def propulsion_modes():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.5))
    modes = [
        ('FORWARD', 'All four units drive forward', [(0,.68)]*4),
        ('LATERAL', 'Servo mounts redirect thrust', [(.68,0)]*4),
        ('PIVOT', 'Two motor groups oppose each other', [(0,-.68),(0,-.68),(0,.68),(0,.68)]),
    ]
    for ax,(title, caption, vectors) in zip(axes,modes):
        ax.set(xlim=(0,4.4),ylim=(0,4.7))
        ax.set_aspect('equal'); ax.axis('off')
        ax.text(2.2,4.4,title,ha='center',color=INK,fontsize=15,weight='bold')
        for x in (1.0,2.7):
            ax.add_patch(FancyBboxPatch((x,.65),.65,2.95,boxstyle='round,pad=.02',facecolor=GREY,edgecolor=INK,lw=1.1))
        ax.add_patch(Rectangle((1.65,1.9),1.05,.35,facecolor='#7c8992',edgecolor='none'))
        positions=[(1.325,1.3),(1.325,2.9),(3.025,1.3),(3.025,2.9)]
        for (x,y),(dx,dy) in zip(positions,vectors):
            ax.add_patch(Circle((x,y),.14,facecolor=TEAL,edgecolor='white',lw=1))
            ax.annotate('',xy=(x+dx,y+dy),xytext=(x,y),arrowprops={'arrowstyle':'-|>','color':TEAL,'lw':2.5,'mutation_scale':16})
        ax.text(2.2,.2,caption,ha='center',color=INK,fontsize=10)
    fig.suptitle('FOBO / REPORTED THRUST DIRECTIONS',fontsize=19,weight='bold',color=INK,y=.98)
    fig.text(.5,.02,'Conceptual force arrows • Mount orientation and motor polarity must match the physical installation',ha='center',fontsize=10,color='#52616b')
    fig.subplots_adjust(top=.88,bottom=.09,left=.03,right=.97,wspace=.06)
    save(fig,'propulsion-modes')


def actuator_packaging():
    fig,ax=plt.subplots(figsize=(13.5,6.6))
    ax.set(xlim=(0,13.5),ylim=(0,6.6));ax.axis('off')
    ax.text(.45,6.13,'FOBO / LOW-COST ACTUATOR PACKAGING',fontsize=21,weight='bold',color=INK)
    ax.text(.45,5.72,'XPS cavities, hot glue and silicone — as described by the builder',fontsize=12,color=INK)
    foam='#f0dbb7'
    for x in (.65,7.25):
        ax.add_patch(FancyBboxPatch((x,1.85),5.1,2.7,boxstyle='round,pad=.05',facecolor=foam,edgecolor=INK,lw=1.2))
        ax.add_patch(Rectangle((x+.55,2.35),3.75,1.6,facecolor='#73b7b0',edgecolor=TEAL,lw=1))
        ax.text(x+.2,4.12,'XPS',fontsize=10,weight='bold',color=INK)
    ax.text(3.2,5.05,'DC MOTOR',ha='center',fontsize=14,weight='bold',color=INK)
    ax.add_patch(FancyBboxPatch((1.6,2.65),2.95,1.0,boxstyle='round,pad=.03',facecolor='#64727d',edgecolor=INK,lw=1.2))
    ax.text(3.075,3.15,'680 RPM motor',ha='center',va='center',fontsize=11,color='white')
    ax.plot([4.55,6.1],[3.15,3.15],color=INK,lw=5,solid_capstyle='round')
    ax.annotate('Shaft outside foam',xy=(5.9,3.15),xytext=(4.6,1.35),ha='center',fontsize=10,color=INK,arrowprops={'arrowstyle':'->','color':INK})
    ax.text(9.8,5.05,'MG996R SERVO',ha='center',fontsize=14,weight='bold',color=INK)
    ax.add_patch(FancyBboxPatch((8.2,2.63),2.95,1.05,boxstyle='round,pad=.02',facecolor='#64727d',edgecolor=INK,lw=1.2))
    ax.text(9.675,3.15,'Servo body',ha='center',va='center',fontsize=11,color='white')
    ax.text(3.2,1.58,'Hot glue + silicone around the body',ha='center',fontsize=10,color=INK)
    ax.text(9.8,1.58,'Servo-sized cavity, then glue/silicone sealing',ha='center',fontsize=10,color=INK)
    ax.add_patch(FancyBboxPatch((.6,.45),12.3,.55,boxstyle='round,pad=.05',facecolor='#fff0df',edgecolor='none'))
    ax.text(6.75,.72,'Observed failure: water entered one servo during the final round.',ha='center',va='center',fontsize=12,color=INK,weight='bold')
    ax.text(.6,.12,'Conceptual section • Output coupling, clearances and sealing interfaces are not dimensioned.',fontsize=9,color='#52616b')
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    save(fig,'actuator-packaging')


if __name__=='__main__':
    draw()
    propulsion_modes()
    actuator_packaging()
