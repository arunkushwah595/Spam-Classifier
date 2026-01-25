# Render Deployment Guide - PostgreSQL Setup

## Step 1: Create PostgreSQL Database on Render

1. Go to [render.com](https://render.com) and sign up/log in
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `spamguard-db`
   - **Database Name**: `spamguard`
   - **User**: `postgres` (or custom)
   - **Region**: `Oregon` (or your preference)
   - **Plan**: `Free`
4. Click **"Create Database"**
5. Wait 2-3 minutes for creation
6. Copy the **Internal Database URL** (looks like: `postgresql://user:password@host/dbname`)

## Step 2: Deploy Web Service on Render

1. Push your project to GitHub
2. On Render, click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `spamguard`
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

## Step 3: Add Environment Variables

In Render Web Service settings, go to **"Environment"** and add:

```
DATABASE_URL=postgresql://user:password@host/spamguard
SECRET_KEY=<generate-a-secure-random-key>
FLASK_ENV=production
```

### Generate Secure SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Or use: `openssl rand -hex 32`

## Step 4: Deploy

1. Click **"Deploy"**
2. Render will build and deploy automatically
3. Your app will be live at: `https://spamguard-xxxx.onrender.com`

## Step 5: Initialize Database

After first deployment:

1. Go to your Render Web Service
2. Open **"Shell"** tab
3. Run:
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

## Database Connection Details

Your PostgreSQL database includes:
- ✅ Automatic backups
- ✅ SSL encryption
- ✅ Daily maintenance windows
- ⚠️ Free tier has limits (512 MB database, 90 days if unused)

## Troubleshooting

**If deployment fails:**
- Check build logs in Render dashboard
- Verify all dependencies are in `requirements.txt`
- Ensure `Procfile` exists and is correct

**If database connection fails:**
- Verify `DATABASE_URL` is correct in Environment Variables
- Check PostgreSQL database is running on Render
- Test locally first with SQLite

**If app restarts frequently:**
- Check error logs in Render
- Verify web service memory is adequate
- Check for syntax errors in `app.py`

## Local Testing Before Deployment

To test with PostgreSQL locally:

```bash
# Install PostgreSQL
# Create a database, then set environment variable:
export DATABASE_URL="postgresql://user:password@localhost/spamguard"
python app.py
```

## Switching Back to SQLite (if needed)

Simply don't set `DATABASE_URL` environment variable, and the app will use SQLite automatically.

---

**Your app is now ready for production! 🚀**
