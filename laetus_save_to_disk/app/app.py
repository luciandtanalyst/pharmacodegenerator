import streamlit as st
from PIL import Image
from code_generator import LaetusCode
import os


def main():
    st.set_page_config(page_title="Laetus Code Generator")
    #Display logo
    img = Image.open("company_logo.jpg")
    col_1, col_2, col_3 = st.columns([1, 3, 1])
    with col_2:
        st.image(img, width=600)
    #Display Title
    st.title("Laetus Code Generator")

    with st.form(key="Generate a code"):
        st.header("Generate a code")
        code_number = st.number_input("Code number", value=3, step=1, min_value=3, max_value=131070, key="single_code")
        submit_button = st.form_submit_button("Generate")
        if 3 <= code_number <= 131070:
            bar_code = LaetusCode(code_number)
            _, exit_message = bar_code.draw_code()
            st.write(exit_message)
        else: st.write("To generate a valid Laetus code, enter an integer between 3 and 131070.")

    with st.form(key="Generate multiple codes"):
        st.header("Generate code sequence")
        start_number = st.number_input("Starting number", value=3, step=1, min_value=3, max_value=131069)
        finish_number = st.number_input("Ending number", value=4, step=1, min_value=3, max_value=131070)
        submit_button = st.form_submit_button("Generate Sequence")
        
        if 3<=start_number<finish_number<=131070 and submit_button:
            
            total_steps = finish_number - start_number+1
            progress_bar = st.progress(0)
            status_text = st.empty()

            for i, number in enumerate(range(start_number, finish_number+1)):
                bar_code = LaetusCode(number)
                exit_code, exit_message = bar_code.draw_code()
                if exit_code == 1:
                    st.write(exit_message)
                    break
                progress_perc = (i+1)/total_steps
                progress_bar.progress(progress_perc)
                status_text.text(f"Processing code: {number} ({i+1}/{total_steps})")
                
            else: st.write("All codes were successfully saved in JPG format.")
        
        elif (finish_number <= start_number) and submit_button:
            st.write("The ending number must be greater than the starting number.")
            

        else: st.write("Enter valid integers between 3 and 131070.")

if __name__ == "__main__":
    main()
