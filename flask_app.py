"""
=============================================================
TASK 4: Flask Mini Project - Student Notes Manager
Author: Ronak | Alfido Tech Internship
=============================================================
"""

from flask import Flask, render_template_string, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
NOTES_FILE = "notes.json"

def load_notes():
    try:
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                return json.load(f)
    except Exception:
        pass
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Student Notes Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f0f4f8; }
        .navbar { background: #1a237e !important; }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/">📚 Student Notes Manager</a>
            <a href="/add" class="btn btn-light btn-sm">+ Add Note</a>
        </div>
    </nav>
    <div class="container">
        <h4 class="mb-3">All Notes <span class="badge bg-secondary">{{ notes|length }}</span></h4>
        {% if notes %}
        <div class="row">
        {% for note in notes %}
        <div class="col-md-6 mb-3">
            <div class="card p-3">
                <div class="d-flex justify-content-between align-items-start">
                    <div>
                        <h5 class="mb-1">{{ note.title }}</h5>
                        <span class="badge bg-primary mb-2">{{ note.subject }}</span>
                        <p class="text-muted small mb-1">{{ note.content }}</p>
                        <small class="text-muted">📅 {{ note.date }}</small>
                    </div>
                    <a href="/delete/{{ loop.index0 }}"
                       class="btn btn-outline-danger btn-sm"
                       onclick="return confirm('Delete this note?')">🗑️</a>
                </div>
            </div>
        </div>
        {% endfor %}
        </div>
        {% else %}
        <div class="alert alert-info">
            No notes yet! <a href="/add">Add your first note</a>.
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

ADD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Add Note</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f0f4f8; }
        .navbar { background: #1a237e !important; }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/">📚 Student Notes Manager</a>
        </div>
    </nav>
    <div class="container">
    <div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card p-4">
            <h4 class="mb-3">📝 Add New Note</h4>
            {% if error %}
            <div class="alert alert-danger">{{ error }}</div>
            {% endif %}
            <form method="POST" action="/add">
                <div class="mb-3">
                    <label class="form-label fw-bold">Title *</label>
                    <input type="text" name="title" class="form-control"
                           placeholder="e.g. Python Loops" required>
                </div>
                <div class="mb-3">
                    <label class="form-label fw-bold">Subject *</label>
                    <select name="subject" class="form-select" required>
                        <option value="">-- Select Subject --</option>
                        <option>Python</option>
                        <option>Data Science</option>
                        <option>Flask/Web Dev</option>
                        <option>Machine Learning</option>
                        <option>Other</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label fw-bold">Note Content *</label>
                    <textarea name="content" class="form-control" rows="4"
                              placeholder="Write your note here..." required></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-100">Save Note</button>
                <a href="/" class="btn btn-outline-secondary w-100 mt-2">Cancel</a>
            </form>
        </div>
    </div>
    </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    notes = load_notes()
    return render_template_string(HOME_HTML, notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        title   = request.form.get("title", "").strip()
        subject = request.form.get("subject", "").strip()
        content = request.form.get("content", "").strip()
        if not title or not subject or not content:
            return render_template_string(ADD_HTML, error="All fields are required!")
        note = {
            "title":   title,
            "subject": subject,
            "content": content,
            "date":    datetime.now().strftime("%d %b %Y, %I:%M %p")
        }
        notes = load_notes()
        notes.append(note)
        save_notes(notes)
        return redirect(url_for("home"))
    return render_template_string(ADD_HTML, error=None)

@app.route("/delete/<int:index>")
def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
    return redirect(url_for("home"))

if __name__ == "__main__":
    print("=" * 50)
    print("  TASK 4: Flask Notes App Running!")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)