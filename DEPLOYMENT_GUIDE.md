# Deployment and Troubleshooting Guide

## 1. Troubleshooting Dependencies

### Common Dependency Errors and Solutions

1. **Version Conflicts**
   ```
   Error: "package X has requirements Y>=1.0 but package Z needs Y<1.0"
   Solution:
   - Check which version of Y works with both X and Z
   - Use pip install package==version to test specific versions
   - Update requirements.txt with working versions
   ```

2. **Missing Dependencies**
   ```
   Error: "ModuleNotFoundError: No module named 'package'"
   Solution:
   - pip install missing_package
   - Add to requirements.txt
   ```

3. **Compilation Errors**
   ```
   Error: "error: command 'gcc' failed"
   Solution:
   - Look for pre-compiled wheels instead
   - Use binary packages (like psycopg2-binary instead of psycopg2)
   ```

### Quick Fix Commands
```bash
# Create fresh virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Generate requirements file
pip freeze > requirements.txt

# Install specific version
pip install package==1.2.3

# Uninstall package
pip uninstall package
```

## 2. Deployment Process

### Local Testing Before Deployment
1. **Clean Environment Test**
   ```bash
   # Create new test environment
   python -m venv test_env
   source test_env/bin/activate
   pip install -r requirements.txt

   # Run your application
   uvicorn main:app --reload
   ```

2. **Database Testing**
   ```bash
   # Test database connections
   alembic upgrade head

   # Check if tables were created
   psql -U your_user -d your_database -c "\dt"
   ```

### Heroku Deployment Steps
1. **Prepare Your App**
   ```bash
   # Initialize git if not already done
   git init

   # Create necessary files
   touch .python-version
   echo "3.11" > .python-version
   ```

2. **Configure Heroku**
   ```bash
   # Login to Heroku
   heroku login

   # Create Heroku app
   heroku create your-app-name

   # Add PostgreSQL
   heroku addons:create heroku-postgresql:mini

   # Set environment variables
   heroku config:set VARIABLE_NAME=value
   ```

3. **Deploy**
   ```bash
   # Add files
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main

   # Run migrations
   heroku run alembic upgrade head
   ```

## 3. Testing Dependencies Locally

### Method 1: Using Virtual Environments
```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# If successful, your dependencies are compatible
# If not, you'll see error messages similar to Heroku's
```

### Method 2: Using Docker (More Similar to Heroku)
```dockerfile
# Create Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and run Docker container
docker build -t myapp .
docker run -p 8000:8000 myapp
```

### Common Gotchas
1. **Version Pinning**
   - Always specify exact versions in requirements.txt
   - Use `==` instead of `>=` when possible

2. **Dependencies of Dependencies**
   - Some packages might conflict through their sub-dependencies
   - Use `pip freeze` to see all installed packages

3. **Platform Differences**
   - Some packages might work locally but not on Heroku
   - Test in clean virtual environment or Docker

4. **Database URLs**
   - Local: `postgresql://user:password@localhost:5432/dbname`
   - Heroku: Will be in `DATABASE_URL` environment variable

## Need Help?
- Check Heroku logs: `heroku logs --tail`
- Look at pip error messages carefully
- Test in clean environment before deploying
- Keep track of working versions
