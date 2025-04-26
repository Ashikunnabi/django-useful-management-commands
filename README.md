
# Django Management Commands

This repository contains a collection of useful Django management commands designed to simplify and automate various tasks in your Django projects.

## Available Commands

### 1. **`add_bulk_user_from_excel.py`**
Bulk create users from an Excel file.

**Description**:  
This command allows you to import multiple users from an Excel file into your database. The file should contain necessary user details such as username, email, password, etc.

**Usage**:
```bash
python manage.py add_bulk_user_from_excel path/to/your/excel_file.xlsx
```

### 2. **`add_bulk_user_from_excel_template.xlsx`**
Template Excel file for bulk user import.

**Description**:  
This file provides a sample template structure for the Excel file required by the `add_bulk_user_from_excel.py` command. Ensure that your file follows this template for a successful import.

**Usage**:  
This is just a template and is not executable.

### 3. **`generate_fake_data.py`**
Populate your database with large amounts of realistic fake data.

**Description**:  
This command generates fake data (using the Faker library) for populating models in your Django application. It helps in testing or developing with mock data.

**Usage**:
```bash
python manage.py generate_fake_data --models User,Product,Order
```

You can specify which models to populate using the `--models` argument.

### 4. **`get_all_logged_in_users.py`**
Get all currently logged in users' information.

**Description**:  
This command retrieves the list of currently logged-in users along with their session data. It is useful for monitoring user activity or debugging authentication issues.

**Usage**:
```bash
python manage.py get_all_logged_in_users
```

### 5. **`invalidate_expired_tokens.py`**
Automatically find and delete/invalidate expired authentication tokens.

**Description**:  
This command checks for expired authentication tokens and either invalidates or deletes them to maintain the integrity of your authentication system.

**Usage**:
```bash
python manage.py invalidate_expired_tokens
```

### 6. **`repair_model_relations.py`**
Scan and repair broken foreign key relations across your models.

**Description**:  
This command scans your database for broken foreign key relationships and gives you the option to fix them by deleting, nullifying, or setting a default ID for the foreign key.

**Usage**:
```bash
python manage.py repair_model_relations --apps orders users --fix --action nullify
```

### 7. **`restore_fixtures.py`**
Restore multiple fixture files easily.

**Description**:  
This command helps you restore multiple fixture files to your database with ease.

**Usage**:
```bash
python manage.py restore_fixtures --fixtures path/to/fixture1.json,path/to/fixture2.json
```

### 8. **`sync_storage_with_db.py`**
Find orphaned uploaded files on S3 or local filesystem that are not referenced in the database.

**Description**:  
This command checks your storage (local or S3) for unused files that are not referenced in the database and helps you clean them up.

**Usage**:
```bash
python manage.py sync_storage_with_db --dry-run
```

### 9. **`user_logout.py`**
Log out a user based on their session ID or username.

**Description**:  
This command allows you to log out a user by their session ID or username. It’s useful for forcefully logging out users in case of suspicious activity or clearing old sessions.

**Usage**:
```bash
python manage.py user_logout --username username
```

## Requirements

Before running these commands, ensure you have the following dependencies installed:

1. Django (version X.X.X)
2. Faker (for generating fake data)
3. tabulate (for nice table formatting in the command line)

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
