# Magdalena Isaya Makweta — Portfolio Website

A professional, responsive portfolio website built with **Python Flask**, **Bootstrap 5**, and **Tailwind CSS** (via CDN).

## Features

- Clean, modern, fully responsive design
- Profile picture placeholder (easy to replace)
- About, Skills, Projects, Research & Contact sections
- 5 default project cards (links can be updated later)
- Published research paper section with direct ISROSET link
- Bootstrap Icons (professional icons, no emojis)
- Sticky navigation with smooth scrolling
- Mobile-friendly

## Quick Start

```bash
# 1. Create & activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

## Replace the Profile Picture

1. Place your photo in:
   ```
   static/img/profile.jpg
   ```
2. In `templates/index.html`, find the `<img>` tag inside the hero section and change the `src` to:
   ```html
   src="{{ url_for('static', filename='img/profile.jpg') }}"
   ```

## Update Project Links

Edit the `PROJECTS` list in `app.py` and replace `"#"` with the real project URL when ready.

## Tech Stack

- **Backend:** Python Flask
- **Frontend:** Bootstrap 5 + Tailwind CSS (CDN)
- **Icons:** Bootstrap Icons
- **Fonts:** Inter + Poppins (Google Fonts)

## Contact

- Email: magdalenaisaya4@gmail.com
- Phone: 0616 348 700
- GitHub: https://github.com/magdalenaisaya4-cell
