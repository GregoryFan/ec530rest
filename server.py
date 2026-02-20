from fastapi import FastAPI
import request_test
app = FastAPI()

accounts = {}

@app.get("/")
def home():
    return {"message": "Test API is running"}

# Create Account with just Username, no Password, and ID
@app.post("/create_account/{username}")
def create_account(username: str):
    if username in [account["username"] for account in accounts.values()]:
        return {"error": "Username already exists"}, 409
    account_id = len(accounts) + 1  
    accounts[account_id] = {"username": username}
    return {"account_id": account_id, "username": username}, 200

# Get Account by ID
@app.get("/get_account/{account_id}")
def get_account(account_id: int):
    account = accounts.get(account_id)
    if account:
        return {"account_id": account_id, "username": account["username"]}, 200
    else:
        return {"error": "Account not found"}, 404
    
# Add Text Notes to Account
@app.post("/add_note/{account_id}/{note}")
def add_note(account_id: int, note: str):
    account = accounts.get(account_id)
    if account:
        if "notes" not in account:
            account["notes"] = []
        account["notes"].append(note)
        return {"message": "Note added successfully"}, 200
    else:
        return {"error": "Account not found"}, 404
    
# Get Notes for Account
@app.get("/get_notes/{account_id}") 
def get_notes(account_id: int):
    account = accounts.get(account_id)
    if account:
        notes = account.get("notes", [])
        return {"account_id": account_id, "notes": notes}, 200
    else:
        return {"error": "Account not found"}, 404
    
# Get Deaths by Industry
@app.get("/get_deaths_by_industry/{account_id}")
def get_deaths_by_industry(account_id: int):
    account = accounts.get(account_id)
    if account:
        if "notes" not in account:
            account["notes"] = []
        death_data = request_test.test_get_deaths_by_industry()
        account["notes"].append(death_data)
        return {"message": "Death data added to notes"}, 200
    else:
        return {"error": "Account not found"}, 404
