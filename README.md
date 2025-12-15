# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# ⚙️ Features:

- Just play the 2048 game for fun

# 🚀 Getting Started :

### 📦 Prerequisites :
- Python >= 3.11

### 🏗️ Setup :

1. In your terminal, clone the repo
```bash
git clone https://github.com/abdmnhjs/2048.git
```

2. Move into the project folder
```bash
cd 2048
```

3. Create a .env file and add these environment variables :
```bash
# Replace [stripe-secret-key] by your Stripe secret key in the sandbox, it must begin by sk_test, do not use the key for real transactions but only for testing please
# Replace [username] and [password] with your own PostgreSQL credentials
# You define the database name when creating the variable
# Example: postgresql://postgres:mypassword@localhost:5432/next-app-rdv-db
DATABASE_URL=postgresql://[username]:[password]@localhost:5432/[database-name]
STRIPE_SECRET_KEY=[stripe-secret-key]
```

4. Install the dependencies
```bash
npm i
```

5. Generate the prisma client
```bash
npx prisma generate
```

6. Apply the migrations (this will create the tables in your database according to the Prisma schema)
```bash
npx prisma migrate dev
```

7. Run the web server
```bash
npm run dev
```



