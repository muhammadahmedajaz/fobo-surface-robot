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
        (4.8,'FOUR ROTATING UNITS','Two front and two rear motor / propeller\nunits on MG996R servo mounts.\nTeal symbols mark approximate locations.'),
        (3.3,'TWO REAR BOOSTERS','Rear propellers appear in the footage.\nTheir controller and wiring remain\nto be documented.'),
        (1.8,'READ WITH THE RECEIVER CODE','The supplied RX uses CH2 for all four\nservo commands. Physical motor-index\nmapping is not established by this sketch.'),
    ]
    for y,title,body in notes:
        ax.text(8.15,y,title,fontsize=11,weight='bold',color=INK,va='top')
        ax.text(8.15,y-.32,body,fontsize=10.2,color=INK,va='top',linespacing=1.45)
    ax.text(.45,.34,'LAYOUT SKETCH • NOT A FABRICATION DRAWING • Shaft sealing, final dimensions and booster wiring need the builder’s account.',fontsize=9,color='#52616b')
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    out=ROOT/'assets/figures'
    out.mkdir(parents=True,exist_ok=True)
    fig.savefig(out/'mechanical-layout-concept.png',dpi=160)
    fig.savefig(out/'mechanical-layout-concept.svg')
    plt.close(fig)


if __name__=='__main__':
    draw()
