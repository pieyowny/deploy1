import os


def create_file(path, content=""):
    """Helper untuk membuat file jika belum ada"""
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATED] {path}")
    else:
        print(f"[SKIPPED] {path} (already exists)")


def main():

    print("\n=== Membuat Struktur Project KEPOYA ===\n")

    # Folder utama
    os.makedirs("kepoya/templates", exist_ok=True)
    os.makedirs("kepoya/static", exist_ok=True)

    # Kosongan app.py
    create_file(
        "kepoya/app.py",
        """from flask import Flask

app = Flask(__name__)

# Tambahkan routing nanti di sini

if __name__ == "__main__":
    app.run(debug=True)
"""
    )

    # HTML kosong
    html_files = [
        "welcome.html",
        "home.html",
        "buat_pertanyaan.html",
        "share.html",
    ]

    for html in html_files:
        create_file(f"kepoya/templates/{html}", f"<!-- {html} -->")

    # CSS dan JS kosong
    create_file("kepoya/static/style.css", "/* style.css */")
    create_file("kepoya/static/script.js", "// script.js")

    print("\n=== DONE! Struktur KEPOYA berhasil dibuat ===\n")


if __name__ == "__main__":
    main()
