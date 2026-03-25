import streamlit as st
from PIL import Image
from code_generator import LaetusCode
import io
import zipfile


def main():
    st.set_page_config(page_title="Laetus Code Generator")
    #Display logo
    img = Image.open("company_logo.jpg")
    col_1, col_2, col_3 = st.columns([1, 3, 1])
    with col_2:
        st.image(img, width=600)
    #Display Title
    st.title("Laetus Code Generator")

    st.header("Generate a code")
    code_number = st.number_input("Code number", value=3, step=1, min_value=3, max_value=131070, key="single_code")
    
    if st.button("Generate Code"):
        bar_code = LaetusCode(code_number)
        img_obj = bar_code.draw_code()
        
        buf = io.BytesIO()
        img_obj.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        
        st.image(img_obj)
        st.download_button(
            label="Download JPG",
            data=byte_im,
            file_name=f"{code_number}.jpg",
            mime="image/jpeg"
        )

    st.divider()

    st.header("Generate code sequence")
    col1, col2 = st.columns(2)
    with col1:
        start_number = st.number_input("Starting number", value=3, step=1, min_value=3, max_value=131070)
    with col2:
        finish_number = st.number_input("Ending number", value=4, step=1, min_value=3, max_value=131070)
    
    if start_number >= finish_number:
        st.error("The ending number must be greater than the starting number.")
    else:
        if st.button("Prepare ZIP for Download"):
            zip_buffer = io.BytesIO()
            total_steps = finish_number - start_number + 1
            progress_bar = st.progress(0)
            status_text = st.empty()

            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
                for i, number in enumerate(range(start_number, finish_number + 1)):
                    bar_code = LaetusCode(number)
                    img_obj = bar_code.draw_code()
                    
                    img_byte_arr = io.BytesIO()
                    img_obj.save(img_byte_arr, format='JPEG')
                    
                    zip_file.writestr(f"{number}.jpg", img_byte_arr.getvalue())
                    
                    progress_perc = (i + 1) / total_steps
                    progress_bar.progress(progress_perc)
                    status_text.text(f"Processing code: {number} ({i+1}/{total_steps})")
            
            st.success("ZIP archive created successfully!")
            st.download_button(
                label="Download ZIP",
                data=zip_buffer.getvalue(),
                file_name=f"laetus_codes_{start_number}_{finish_number}.zip",
                mime="application/zip"
            )

if __name__ == "__main__":
    main()
