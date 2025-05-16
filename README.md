# Capstone-Project

Capstone Project for Meta Back-End Developer Professional Certificate

## Admin Login (for Reviewers)

-   Visit: `http://127.0.0.1:8000/admin/`
-   Username: admindjango1
-   Password: employee@123!

**(This is the same as the details for the mysql)**

#### Details for an authenticated user:

```json
{
	"username": "newuser",
	"password": "securepassword123",
	"email": "newuser@example.com"
}
```

## Tests

I have added changed the tests to SQLite so as that they run in memory and don't require messing around with MySQL permissions etc
