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
client_id='YOUR_GITHUB_CLIENT_ID',         # <-- your Client ID here
client_secret='YOUR_GITHUB_CLIENT_SECRET', # <-- your Client Secret here
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
    ├── 1_login_page.png
    ├── 2_github_authorization.png
    ├── 3_successful_login.png
    ├── 4_unauthorized_access.png
    └── 5_logout_result.png
```

---

## Critical Thinking Answers

**i. What happens when a user accesses /profile without logging in?**  
The server returns a `401 Unauthorized` response with the message "Unauthorized: Please login first."

**ii. What data is returned after successful login?**  
GitHub returns the authenticated user's profile data including username (login), avatar URL, public repos count, followers, email, and more.

**iii. Why is OAuth considered more secure than traditional login?**  
OAuth never exposes the user's password to the third-party app. Instead, it uses short-lived access tokens. The credentials stay with the identity provider (GitHub), reducing the risk of credential theft.

**iv. What challenges did you encounter?**  
*(Fill this in based on your experience)*

**v. What did you learn from this activity?**  
*(Fill this in based on your experience)*