"""Feature A: User authentication module."""

def authenticate_user(username, password):
    """Authenticate a user with username and password."""
    # Placeholder implementation
    return username == "admin" and password == "secret"

def get_user_permissions(user_id):
    """Get permissions for a user."""
    return ["read", "write"]

