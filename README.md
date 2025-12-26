# 🥗 SmartPlate AI: Your Personal Food Companion

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-green)
![Status](https://img.shields.io/badge/Status-Live-success)

**SmartPlate AI** is a multimodal AI application designed to help users make healthier food choices and reduce food waste. By leveraging Google's **Gemini Pro Vision** models, the app can "see" your food to estimate nutritional content or "look" at ingredients to suggest gourmet recipes.

---

## 📸 Demo & Screenshots

### 1. Nutrition Analysis (Pasta)
The AI analyzes the image to identify the food type and calculate estimated calories and macros.
![Pasta Analysis]("C:\Users\Sai Kiran\OneDrive\Pictures\Screenshots\Screenshot 2025-12-26 115010.png")

### 2. Complex Meal Detection (Thali)
Even with multiple items on a single plate (Roti, Pickle, Namkeen), the AI breaks down each item individually.
![Thali Analysis](assets/Screenshot%202025-12-20%20161746.png)

### 3. AI Chef & Recipe Generator
Upload an image of ingredients (or a dish), add extra items from your fridge, and get detailed cooking instructions.
![Recipe Generator](assets/Screenshot%202025-12-20%20161843.png)

---

## ✨ Key Features

* **🥗 AI Nutritionist:** Estimates total calories and provides a table breakdown of Carbs, Fats, and Protein for any food image.
* **👨‍🍳 Smart Chef:** Identifies visible ingredients and suggests 2-3 creative recipes.
* **➕ Multi-modal Input:** Combines visual data (image) with text input (extra ingredients) for personalized recipe suggestions.
* **🛡️ Robust Error Handling:** Includes auto-retry logic to handle API rate limits smoothly without crashing.
* **📊 Clean UI:** Built with Streamlit for a responsive, dashboard-like experience.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python framework for data apps)
* **AI Model:** [Google Gemini 1.5 Flash](https://deepmind.google/technologies/gemini/) (Vision + Text capabilities)
* **Language:** Python 3.10+
* **Utilities:** `python-dotenv` (Environment management), `PIL` (Image processing)

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/smartplate-ai.git](https://github.com/your-username/smartplate-ai.git)
cd smartplate-ai

```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Set up API Key

1. Get your free API key from [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the project root.
3. Add your key:
```env
GOOGLE_API_KEY=your_actual_api_key_here

```



### 5. Run the App

```bash
streamlit run app.py

```

---

## 💡 How It Works

1. **Vision Analysis:** The image is passed to the Gemini 1.5 Flash model.
2. **Prompt Engineering:**
* *For Nutrition:* We use a structured prompt asking for a JSON-like table output and a health assessment.
* *For Recipes:* We use a creative prompt that fuses the visual list of ingredients with the user's text input.


3. **Response Handling:** The app parses the AI's response and renders it using Streamlit's Markdown and Table components.

---

## 🔮 Future Improvements

* **Save History:** Allow users to save their daily calorie logs.
* **Dietary Filters:** Add checkboxes for "Vegan", "Gluten-Free", or "Keto" recipe constraints.
* **Export:** Download the shopping list for generated recipes as a PDF.

---
