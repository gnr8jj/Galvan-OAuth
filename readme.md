# Lab 05-07: Securing APIs using OAuth 2.0 with GitHub

## Setup Instructions

### 1. Clone / Download this project

### 2. Create a GitHub OAuth App
1. Go to **GitHub → Settings → Developer Settings → OAuth Apps → New OAuth App**
2. Fill in:
   - **Homepage URL:** `http://localhost:5000`
   - **Authorization Callback URL:** `http://localhost:5000/callback`
3. Copy your **Client ID** and **Client Secret**

### 3. Configure Credentials
Open `app.py` and replace the placeholders:
```python
client_id='Ov23lix9WwMOVJOOKfgM',    
client_secret='ebb11308d58ba2587c88cbe1b3dac559eee61f02',
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the App
```bash
python app.py
```

### 6. Test the Routes
| Route | Description |
|-------|-------------|
| `http://localhost:5000/` | Home page |
| `http://localhost:5000/login` | Redirect to GitHub login |
| `http://localhost:5000/callback` | GitHub callback (auto) |
| `http://localhost:5000/profile` | View profile (protected) |
| `http://localhost:5000/logout` | Logout |
| `http://localhost:5000/api/secure-data` | Bonus protected route |

---

## Project Structure
```
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── login.png
    ├── auth.png
    ├── profile.png
    ├── unauthorizedprofile.png
    └── localhost5000.png
```
