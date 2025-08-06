
# Unit Converter Web Application

A responsive and user-friendly **Unit Converter** web application built with **FastAPI** (Python) backend and a modern HTML/CSS/JavaScript frontend.

---

## Features

- Convert between units in different categories:
  - Length
  - Weight
  - Temperature
  - Storage
  - Speed
  - Volume
  - Area
  - Time
- Dynamic dropdowns based on selected category
- Real-time conversion without page reload (AJAX)
- Responsive and beautiful design compatible with all devices
- Easy to extend and customize conversion logic
- Made by Lakshit Verma

---

## Project Structure

```
project-root/
│
├── backend/
│   ├── main.py                 # FastAPI backend API & server
│   ├── venv/                   # Python virtual environment folder (optional)
│
├── frontend/
│   ├── index.html              # Frontend HTML page
│   ├── static/
│       ├── style.css           # CSS styles
│       ├── script.js           # Frontend JavaScript
```

---

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Jinja2

---

## Installation and Running Locally

1. Clone the repo:

    ```bash
    git clone https://github.com/yourusername/unit-converter.git
    cd unit-converter/backend
    ```

2. Create and activate virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate      # Linux/Mac
    venv\Scripts\activate         # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

5. Open your browser at [http://localhost:8000](http://localhost:8000) to access the app.

---

## Deployment

You can deploy this app on free cloud platforms like:

- [Railway.app](https://railway.app/)
- [Render.com](https://render.com/)
- [Heroku (deprecated free tier)](https://www.heroku.com/)

Just push the full project code to GitHub and connect it to any of these platforms. Configure the start command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

---

## How to Use

1. Enter the numeric value to convert.
2. Select a conversion category.
3. Choose the unit to convert from and the unit to convert to.
4. Click **Convert** to get the converted value displayed below.

---

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for suggestions and bugs.

---

## License

This project is open source and free to use.

---

## Contact

Made by Lakshit Verma  
GitHub: https://github.com/yummyPancake2607

```

---

**How to use this README:**

- Replace `https://github.com/yourusername/unit-converter.git` with your public repo URL.
- Add any contact info you want.
- Put this file `README.md` in your project root folder.
- It will show nicely on GitHub/Render/Railway repos.

If you want, I can help generate `requirements.txt` and other deployment files too!
```
Project url https://roadmap.sh/projects/unit-converter