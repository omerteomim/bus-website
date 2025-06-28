# 🚌 Bus Website

A clean, modern web application for checking real-time bus arrival information. Made to create yourself a website for your favorite buses.

## ✨ Features

- **Real-time Bus Information**: Check current bus arrival times and status
- **Hebrew/RTL Support**: Fully localized interface in Hebrew with right-to-left text direction

- **The application displays**:
    - Bus line numbers with route information
    - Real-time arrival predictions

## 📁 Project Structure

```
bus-website/
├── .github/
    ├── workflows/
        ├── deply.yaml
├── index.html
├── lambda_function.py  
├── main.tf        
├── README.md           
└── variables.tf            
```
## 🚀 Getting Started

### Prerequisites

- AWS Access key and secret access key in repository secrets.
- AWS Region where you want to deploy the backend in repository secrets.
- Github pages configured for Github Actions.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/omerteomim/bus-website.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd bus-website
   ```
3. **Apply your favorite buses and stations to the lambda_function.py**
   - Check in https://curlbus.app/operators for your lines info and configure the BUS_ROUTES list in lambda_function.py

4. **Push to your repository**
   
5. **Search your github pages domain** 
   - https://$(YOUR_GITHUB_USERNAME)$.github.io/bus-website/

## 🙏 Acknowledgments
  **Bus data provided by** - [curlbus.app](https://curlbus.app/)

## 👨‍💻 Author

**Omer Teomim**
- GitHub: [@omerteomim](https://github.com/omerteomim)

## 📞 Support

If you have any questions or need help with the project, please open an issue on GitHub.

---

Made with ❤️ for better public transportation accessibility