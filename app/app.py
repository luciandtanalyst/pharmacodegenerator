import streamlit as st
from code_generator import LaetusCode
from PIL import Image
import zipfile

def main():
    st.set_page_config(page_title="Laetus Code Generator")
    logo = Image.open("company_logo.jpg")
    col_1, col_2, col_3 = st.columns([1, 3, 1])
    with col_2:
        st.image(logo, width=600)
    st.title("Laetus Code Generator")

    st.divider()

    file_format = st.radio("Choose the file format to save",
             ["jpg", "png", "svg"],
             captions=["Jpg image format", "Png image format", "Svg vector format"])

    st.divider()

    st.header("Generate one code")
    code_number = st.number_input("Code number", value=3, step=1, min_value=3, max_value=131070, key="single_code")

    if st.button("Generate"):
        bar_code = LaetusCode(code_number)
        generators = {
            "jpg": bar_code.to_jpg,
            "png": bar_code.to_png,
            "svg": bar_code.to_svg
        }

        #Generate a preview only image for the streamlit application
        byte_img_preview = generators["png"]().getvalue()
        st.image(byte_img_preview)

        #Generate the file for download
        byte_img = generators[file_format]().getvalue()
        st.download_button(
            label=f"Download {file_format}",
            data = byte_img,
            file_name=f"{code_number}.{file_format}"
        )
    
    st.divider()

    st.header("Generate a sequence of codes")
    col_1, col_2 = st.columns(2)
    with col_1:
        first_code = st.number_input("First code", value=3, step=1, min_value=3, max_value=131070)
    with col_2:
        last_code = st.number_input("Last code", value=4, step=1, min_value=3, max_value=131070)

    if first_code >= last_code:
        st.error("The last code must be greater than the first code")
    else:
        pass


    
        

if __name__ == "__main__":
    main()
