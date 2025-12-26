import streamlit as st
import os
import time
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
from google.api_core import exceptions

st.set_page_config(
    page_title="SmartPlate AI",
    page_icon="🥗",
    layout="wide"
)

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-flash-latest')

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2921/2921822.png", width=100)
    st.title("🥗 SmartPlate")
    st.markdown("---")
    st.write("This AI agent uses computer vision to analyze your food.")

    st.header("How to use:")
    st.markdown("""
    1. **Upload** a photo of food.
    2. **Analyze** its calories.
    3. **Generate** recipes from ingredients.
    """)

    st.info("💡 Pro Tip: Clearer images give better calorie estimates.")


def get_gemini_response(input_prompt, image):
    for attempt in range(3):
        try:
            response = model.generate_content([input_prompt, image])
            return response.text
        except exceptions.ResourceExhausted:
            time.sleep(2)
            continue
        except Exception as e:
            if "429" in str(e) or "Quota" in str(e):
                time.sleep(2)
                continue
            return f" An error occurred: {str(e)}"

    return "**Traffic Limit Hit**: Server is too busy right now. Please wait 1 minute."


st.title("🍽️ SmartPlate AI: Your Food Companion")
st.markdown("### Identify calories or get recipe ideas in seconds.")
st.write("---")

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📸 Upload Image")
    uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Your Plate", use_container_width=True)
    else:
        st.info("Waiting for upload...")

with col2:
    st.subheader("🔍 Analysis Options")

    tab1, tab2 = st.tabs(["🍎 Nutrition Tracker", "👨‍🍳 Chef's Kitchen"])

    with tab1:
        st.write("Analyze the macro-nutrients of your meal.")
        if st.button("Calculate Calories", key="nutrition_btn", type="primary"):
            if image:
                with st.spinner("Analyzing pixels for calories..."):
                    prompt = """
                    You are an expert nutritionist. Analyze the food in the image.

                    Format your response as a MARKDOWN TABLE with these columns:
                    | Item | Estimated Calories | Carbs(g) | Fat(g) | Protein(g) |

                    After the table, provide a short 1-sentence health verdict.
                    """
                    response = get_gemini_response(prompt, image)

                    if "Traffic Limit Hit" in response or "Error" in response:
                        st.error(response)
                    else:
                        st.success("Analysis Complete!")
                        st.markdown(response)
            else:
                st.warning("Please upload an image first!")

    with tab2:
        st.write("Turn these ingredients into a new meal.")
        extra_ingredients = st.text_input("Any extra ingredients in your fridge?", placeholder="e.g. spinach, butter")

        if st.button("Get Recipe Ideas", key="recipe_btn"):
            if image:
                with st.spinner("Chef is writing recipes..."):
                    prompt = f"""
                    You are a Michelin-star chef. 
                    1. Identify ingredients in the image.
                    2. Combine them with: {extra_ingredients} (if provided).
                    3. Suggest 2 gourmet recipes.

                    Format as:
                    ### 🍲 [Recipe Name]
                    * **Time:** [Time]
                    * **Difficulty:** [Easy/Medium/Hard]
                    * **Instructions:** [Brief summary]
                    """
                    response = get_gemini_response(prompt, image)

                    if "Traffic Limit Hit" in response or "Error" in response:
                        st.error(response)
                    else:
                        st.success("Recipes Generated!")
                        st.markdown(response)
            else:
                st.warning("Please upload an image first!")