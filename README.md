### Project Name: **Inventory Insight**

### README:

#### Project Overview:
Inventory Insight is a comprehensive data processing and visualization tool designed for managing supplier inventory data. The project automates the retrieval, consolidation, and analysis of inventory files across different suppliers, providing a clear graphical view of stock levels and distributions.

#### Features:
- **Data Consolidation:** Automatically gathers and consolidates CSV and text data files from predefined directory paths, ensuring up-to-date inventory data.
- **Dynamic Visualization:** Utilizes Plotly and Dash to create interactive bar graphs and histograms to display inventory balances and distributions.
- **Configurable Paths:** Easily configurable file paths and column settings through a centralized configuration file.
- **Search Functionality:** Includes a search feature to filter data based on article numbers directly from the web interface.

#### How to Set Up and Run:
1. **Clone the Repository:**
   ```
   git clone https://your-repository-url.com/inventory-insight.git
   cd inventory-insight
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Paths:**
   Update the `path/to/your/documents` in the `mapp_konfiguration` dictionary to point to your specific data directories.

4. **Run the Application:**
   To start the server and access the web interface:
   ```
   python dash-app.py
   ```

5. **View and Analyze Data:**
   Open your web browser and go to `http://127.0.0.1:8050/` to view the dashboard. Select suppliers and enter article numbers to filter and analyze inventory data.

#### Project Structure:
- **dash-app.py:** Main Dash application for data visualization.
- **kolumn_check.py:** Utility script to verify the integrity of column names in CSV files.
- **main.py:** Processes files from backup directories and stores consolidated data.
- **mappLista.py:** Contains configurations for directory paths and file settings for each supplier.

#### Contributing:
Feel free to fork the repository, make changes, and submit a pull request if you have improvements or additional features you'd like to add.
