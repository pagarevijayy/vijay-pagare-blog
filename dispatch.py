import datetime
import os

# Configuration
CONTENT_BASE = "content"
INCOMING_FILE = "incoming.txt"


def dispatch():
    if not os.path.exists(INCOMING_FILE):
        print(f"❌ {INCOMING_FILE} not found. Nothing to dispatch.")
        return

    with open(INCOMING_FILE, "r") as f:
        lines = f.readlines()

    # The first line of our "Handshake" will always be the target folder
    # Format: #target: diary | essay | rfc
    target_folder = lines[0].replace("#target:", "").strip()
    content = "".join(lines[1:])

    # Generate filename based on date and slug
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S+05:30")
    datestamp = now.strftime("%Y-%m-%d")

    # Extract title for the filename slug
    title_line = [l for l in lines if l.startswith("title =")][0]
    slug = (
        title_line.split("=")[1]
        .strip()
        .replace("'", "")
        .replace('"', "")
        .lower()
        .replace(" ", "-")
    )

    filename = f"{datestamp}-{slug}.md"
    filepath = os.path.join(CONTENT_BASE, target_folder, filename)

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as f:
        f.write(content.replace("INSERT_TIMESTAMP", timestamp))

    print(f"✅ Dispatched to: {filepath}")
    print(f"🚀 Run 'hugo server -D' to preview.")


if __name__ == "__main__":
    dispatch()
