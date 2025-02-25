# Message Hiding in Images (Steganography)

## 📌 Project Description
This is a simple **GUI-based Steganography tool** built using **Python and Tkinter** that allows users to **hide and reveal secret messages** inside images using the **LSB (Least Significant Bit) technique**.

## 🚀 Features
- **Hide Text Messages** inside PNG/JPG images.
- **Retrieve Hidden Messages** from encoded images.
- **Secure with a Password** to prevent unauthorized access.
- **Simple & User-friendly Interface** using Tkinter.

## 🛠️ Technologies Used
- **Python** 🐍
- **Tkinter** (GUI Development)
- **PIL (Pillow)** (Image Processing)
- **Stegano** (LSB Encoding)

## 📥 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/vighneshmadankar/MCA_Project_Hiding_Massage_in_Image
   cd MCA_Project_Hiding_Massage_in_Image
   ```
2. **Install required dependencies**
   ```bash
   pip install pillow stegano
   ```
3. **Run the application**
   ```bash
   python app.py
   ```

## 🖥️ Usage
1. **Open an Image** using the GUI.
2. **Enter a Secret Message** and click "Hide Data".
3. **Save the Encoded Image**.
4. **To Reveal the Message**, open the encoded image and enter the correct password.

## 📌 Notes
- The tool uses **LSB Steganography**, so image quality remains unchanged.
- Works best with **PNG images** to prevent quality loss.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to improve.

