⚙️ Reproducing the Environment 
To reproduce the development environment:
```
# 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1

# 2️⃣ Create and Activate Python Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install Required Packages
pip install --upgrade pip
pip install -r requirements.txt

#4️⃣ Verify Setup
python --version
pip list
```
5️⃣ Notes

The data/ folder is ignored in Git. Place your local datasets in data/ (do not commit them).

All notebooks and scripts are configured to use this environment.
