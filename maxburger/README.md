# 🍔 Max Burger & More — Franchise Web App

A full-stack franchise website for **Max Burger & More** with:
- Beautiful React frontend (Vite)
- Flask Python backend
- AI-powered chatbot (Claude)
- Franchise inquiry form → auto-saves to CSV
- Sections: Home, About, Why Us, Menu, Locations, Contact

---

## 🗂️ Project Structure

```
maxburger/
├── backend/
│   ├── app.py              ← Flask server (API + serves production build)
│   ├── requirements.txt    ← Python dependencies
│   └── franchise_inquiries.csv  ← Auto-created when first form is submitted
├── frontend/
│   ├── src/
│   │   ├── App.jsx         ← Full React app (all sections + chatbot)
│   │   └── main.jsx        ← React entry point
│   ├── public/
│   │   └── logo.jpg        ← Max Burger logo
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
└── README.md
```

---

## 🚀 Quick Start

### 1. Set up environment

```bash
# Set your Anthropic API key (for the chatbot)
export ANTHROPIC_API_KEY=your_key_here
```

### 2. Install Python dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Install Node dependencies

```bash
cd frontend
npm install
```

---

## 🛠️ Running in Development

Open **two terminals**:

**Terminal 1 — Backend:**
```bash
cd backend
python app.py
# Runs on http://localhost:5000
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm run dev
# Runs on http://localhost:5173
# API calls are proxied to :5000
```

Visit: **http://localhost:5173**

---

## 🏭 Running in Production

```bash
# Build React frontend
cd frontend
npm run build

# Serve everything via Flask
cd backend
python app.py
# Visit http://localhost:5000
```

---

## 📊 Franchise Inquiries CSV

Every time someone submits the franchise form, their details are saved to:
```
backend/franchise_inquiries.csv
```

**Columns:**
- Name, Email, Phone, City, State, Investment_Budget, Experience, Message, Timestamp

You can open this file in Excel/Google Sheets to manage leads.

---

## 🤖 Chatbot

The chatbot is powered by Claude (claude-sonnet-4-20250514). It acts as "Max" — a friendly franchise assistant that knows:
- Investment details and models
- Revenue potential
- Franchise process
- Menu and locations
- How to contact the team

Requires: `ANTHROPIC_API_KEY` environment variable set.

---

## 🎨 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + Vite |
| Styling | Inline CSS + Google Fonts |
| Backend | Python Flask |
| AI Chatbot | Anthropic Claude API |
| Data Storage | CSV (franchise_inquiries.csv) |
| Fonts | Fredoka One + Nunito |
| Color Palette | Amber (#D4820A), Brown (#7B3F00), Red (#C0392B) |

---

## 📞 Brand Contact

- Instagram: [@maxburgerandmore](https://instagram.com/maxburgerandmore)
- Email: maxburgerandmore@gmail.com
- Location: Jodhpur, Rajasthan, India

---

*Built for Max Burger & More franchise expansion* 🍔
