def save_file(uploaded_file, destination: str):
    with open(destination, "wb") as f:
        f.write(uploaded_file.file.read())
    return destination
