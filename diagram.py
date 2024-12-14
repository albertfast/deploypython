import matplotlib.pyplot as plt
import numpy as np

TEXT_PROPS = dict(ha='center', va='center', fontsize=12,
                  bbox=dict(boxstyle="round", facecolor="wheat", edgecolor="black"))
POSITIONS = {
    'Start': (0.1, 0.8),
    'Input total': (0.3, 0.8),
    'total >= 90?': (0.5, 0.8),
    'total >= 80?': (0.5, 0.6),
    'total >= 70?': (0.5, 0.4),
    'total >= 60?': (0.5, 0.2),
    'grade = \'A\'': (0.7, 0.8),
    'grade = \'B\'': (0.7, 0.6),
    'grade = \'C\'': (0.7, 0.4),
    'grade = \'D\'': (0.7, 0.2),
    'grade = \'F\'': (0.9, 0.2),
    'End': (0.9, 0.5)
}


def draw_arrows(ax, positions):
    arrows = [
        ('Start', 'Input total'), ('Input total', 'total >= 90?'),
        ('total >= 90?', 'grade = \'A\''), ('total >= 90?', 'total >= 80?'),
        ('total >= 80?', 'grade = \'B\''), ('total >= 80?', 'total >= 70?'),
        ('total >= 70?', 'grade = \'C\''), ('total >= 70?', 'total >= 60?'),
        ('total >= 60?', 'grade = \'D\''), ('total >= 60?', 'grade = \'F\''),
        ('grade = \'A\'', 'End'), ('grade = \'B\'', 'End'),
        ('grade = \'C\'', 'End'), ('grade = \'D\'', 'End'),
        ('grade = \'F\'', 'End')
    ]
    for start, end in arrows:
        start_pos = positions[start]
        end_pos = positions[end]
        ax.annotate('', xy=end_pos, xytext=start_pos, arrowprops=dict(arrowstyle="->", lw=1.5))


def create_flowchart():
    fig, ax = plt.subplots(figsize=(10, 5))
    # Draw nodes
    for text, pos in POSITIONS.items():
        ax.text(*pos, text, **TEXT_PROPS)
    # Draw arrows
    draw_arrows(ax, POSITIONS)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()


# Call the function to create the flowchart
create_flowchart()
