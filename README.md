# Product Price Calculation API

This is a Flask-based API for calculating product prices based on the given MRP per unit and quantity (case size). It provides a simple form for user input and displays the calculated results in a tabular form on the same page. The results can also be exported as a CSV file.

## Prerequisites

- Python (version 3.6 or above)
- Flask (version 2.0.1 or above)
- Axios (version 0.21.4 or above)
- Alpine.js (version 2.8.2 or above)
- Bootstrap (version 4.3.1 or above)

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/product-price-calculation-api.git
   ```

2. Navigate to the project directory:
   ```shell
   cd product-price-calculation-api
   ```

3. Install the required dependencies:
   ```shell
   pip install flask
   ```

## Usage

1. Start the Flask development server:
   ```shell
   python main.py
   ```

2. Open your web browser and go to `http://localhost:5000` to access the application.

3. Enter the product name, MRP per unit, and quantity (case size) in the provided form fields.

4. Click the "Calculate" button to perform the price calculation.

5. The calculated results will be displayed in a tabular form below the form.

6. To collapse or expand the results, click the "Collapse Results" button.

7. To export the results as a CSV file, click the "Export CSV" button. The file will be downloaded automatically.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
