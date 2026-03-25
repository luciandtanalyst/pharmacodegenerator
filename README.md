# Laetus (Pharma) Code Generator

This project was developed out of the necessity to automate the mass generation of Laetus codes used in the pharmaceutical industry for various packaging elements: boxes, leaflets, vial labels, etc.

## 🎯 Why this project?

Most online generators limit the number of codes per session, which can be frustrating in professional workflows. This application eliminates those barriers, allowing for the rapid generation of hundreds or thousands of codes required in pharma production lines.

## ✨ Current Features

* **Precise Algorithm**: Converts integers into binary strings according to the Laetus standard.
* **Web Interface**: Built with **Streamlit** for an intuitive and user-friendly experience.
* **Two Operation Modes**:
    * `laetus_save_to_disk`: Generates and saves `.jpg` images directly to a local folder (ideal for server-side processing).
    * `laetus_generator_zip`: Allows downloading the generated codes as a `.zip` archive directly through the browser.
* **Containerization**: Runs instantly via **Docker**, eliminating the need for manual Python dependency management.

## 🎨 Customization (White Label)

To personalize the application with your own branding:
1. Locate the `company_logo.jpg` file in the project directory.
2. Replace it with your own company logo.
3. **Important**: Keep the filename exactly as `company_logo.jpg` for the application to load it correctly.

## 🛠️ Tech Stack

* **Python** (Core Logic)
* **Streamlit** (Web UI)
* **Docker & Docker Compose** (Deployment)
* **Pillow** (Image Generation)

## 📦 Installation and Setup

Ensure you have **Docker** and **Docker Compose** installed on your system.

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/luciandtanalyst/pharmacodegenerator.git](https://github.com/luciandtanalyst/pharmacodegenerator.git)
    ```
2.  **Navigate to the project folder and run**:
    ```bash
    docker compose up -d
    ```
3.  **Access the application in your browser**: 
    [http://localhost:8503](http://localhost:8503)

## 🗺️ Roadmap (Future Versions)

- [ ] Merge the two variants into a single application with an output method selector.
- [ ] Implement a **CLI** (Command Line Interface) script for headless operation.
- [ ] Add support for vector formats (e.g., `.svg` or `.eps`).

---

> [!CAUTION]
> **Disclaimer**: The user is solely responsible for verifying the generated codes before printing on materials destined for pharmaceutical production.
