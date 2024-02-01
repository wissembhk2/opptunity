from app.models.users import Users
from app.utils.database import sessionLocal
import bcrypt
from sqlalchemy.exc import IntegrityError
def add_user(name, email, password, status, google_id=None, is_google_account=False):
    # Create an instance of the Users class with the provided details
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = Users(
        name=name,
        email=email,
        password=hashed_password.decode('utf-8'),
        status=status,
        google_id=google_id,
        is_google_account=is_google_account,
        # created_at is automatically set to the current time
    )
    
    # Create a new database session
    session = sessionLocal()

    try:
        # Add the new user to the session and commit the transaction
        session.add(new_user)
        session.commit()
        print(f"User {name} added successfully.")
    except Exception as e:
        # If there's an error, rollback the transaction and print the error
        session.rollback()
        print(f"Error adding user {name}: {e}")
        return e
    finally:
        # Close the session whether or not there was an error
        session.close()

def sign_in(email, submitted_password):
    # Create a new database session
    session = sessionLocal()
    
    try:
        # Query the database for the user by email
        user = session.query(Users).filter(Users.email == email).first()

        # If a user is found, check the submitted password against the stored hash
        if user and bcrypt.checkpw(submitted_password.encode('utf-8'), user.password.encode('utf-8')):
            # Password is correct
            print(f"User {user.name} signed in successfully.")
            return True
        else:
            # User not found or password is incorrect
            print("Invalid login credentials.")
            return False
    except Exception as e:
        # If there's an error, print the error
        print(f"Error signing in: {e}")
        return False
    except IntegrityError:
        session.rollback()  # Rollback the session on error
        print(f"Error: The email {email} is already in use.")
        return False
    finally:
        # Close the session whether or not there was an error
        session.close()