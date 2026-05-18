import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Class activity photos with captions ──
# Replace image paths with actual photo filenames when available
# e.g., photos[0]["path"] = "photos/field_trip.jpg"

photos = [
    {
        "title": "Nature Trail Field Trip",
        "caption": "We explored the forest trails\nand learned about local ecosystems.",
        "color": "#a5d6a7",
        "emoji": "🏕️",
        "category": "Field Trip"
    },
    {
        "title": "Soccer Tournament Day",
        "caption": "10-Ruby showed amazing teamwork\nat the inter-class soccer tournament!",
        "color": "#81d4fa",
        "emoji": "⚽",
        "category": "Sports"
    },
    {
        "title": "Art Class Creations",
        "caption": "Our colorful artworks were displayed\nat the school hallway exhibit.",
        "color": "#f48fb1",
        "emoji": "🎨",
        "category": "Arts"
    },
    {
        "title": "Museum Visit",
        "caption": "We visited the National Museum\nand explored Philippine history.",
        "color": "#ffe082",
        "emoji": "🏛️",
        "category": "Field Trip"
    },
    {
        "title": "Dance Festival",
        "caption": "Our class performed a folk dance\nroutine for the school festival.",
        "color": "#ce93d8",
        "emoji": "💃",
        "category": "Arts"
    },
    {
        "title": "Science Lab Experiments",
        "caption": "Hands-on chemistry experiments —\nwe loved watching the reactions!",
        "color": "#b2ebf2",
        "emoji": "🔬",
        "category": "Science"
    },
    {
        "title": "Foundation Day",
        "caption": "Celebrating the school's anniversary\nwith parades and performances.",
        "color": "#f8bbd0",
        "emoji": "🎉",
        "category": "Events"
    },
    {
        "title": "Science Fair",
        "caption": "10-Ruby's hydroponics project\nbagged the Best Study award.",
        "color": "#c8e6c9",
        "emoji": "🌱",
        "category": "Science"
    },
]


def display_gallery(photos):
    """Display class activity photos in a matplotlib grid with captions."""

    cols = 4
    rows = (len(photos) + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(16, rows * 5))
    fig.patch.set_facecolor("#fce4ec")

    # Flatten axes for easy indexing
    axes_flat = axes.flatten() if rows > 1 else [axes] if cols == 1 else axes.flatten()

    for i, ax in enumerate(axes_flat):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        if i < len(photos):
            photo = photos[i]

            # ── Photo placeholder (colored rectangle) ──
            # Replace with:  img = plt.imread(photo["path"])
            #                ax.imshow(img)
            rect = mpatches.FancyBboxPatch(
                (0.05, 0.3), 0.9, 0.65,
                boxstyle="round,pad=0.02",
                facecolor=photo["color"],
                edgecolor="#ad1457",
                linewidth=2
            )
            ax.add_patch(rect)

            # Emoji / icon in center of placeholder
            ax.text(0.5, 0.635, photo["emoji"],
                    ha="center", va="center",
                    fontsize=36, transform=ax.transAxes)

            # Category badge
            ax.text(0.5, 0.32,
                    f"[ {photo['category']} ]",
                    ha="center", va="top",
                    fontsize=8, color="#ad1457",
                    fontweight="bold", transform=ax.transAxes)

            # Title
            ax.text(0.5, 0.22,
                    photo["title"],
                    ha="center", va="top",
                    fontsize=9.5, color="#4a148c",
                    fontweight="bold", wrap=True,
                    transform=ax.transAxes)

            # Caption
            ax.text(0.5, 0.10,
                    photo["caption"],
                    ha="center", va="top",
                    fontsize=7.5, color="#880e4f",
                    style="italic", wrap=True,
                    transform=ax.transAxes)

        else:
            # Empty cell
            ax.set_facecolor("#fce4ec")

    plt.suptitle(
        "🌸  10-Ruby Class Highlights  🌸",
        fontsize=18, fontweight="bold",
        color="#ad1457", y=1.01
    )

    plt.tight_layout(pad=2.5)
    plt.savefig("gallery_output.png", dpi=150,
                bbox_inches="tight", facecolor="#fce4ec")
    print("✨ Gallery saved as gallery_output.png")
    plt.show()


# ── Print summary ──
print("=" * 50)
print("      🌸 10-Ruby Class Activities 🌸")
print("=" * 50)

for i, photo in enumerate(photos, 1):
    print(f"  {i:>2}. [{photo['category']:<10}] {photo['title']}")
    print(f"       ↳ {photo['caption'].replace(chr(10), ' ')}")

print("=" * 50)
print(f"  Total photos: {len(photos)}")
print("=" * 50)

display_gallery(photos)
