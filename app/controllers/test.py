upload_dir = "../uploaded_files/"
file_name = "test.pdf"
with open(f"{upload_dir}{file_name}", "w") as file:
    file.writelines("test")
