#13. Secure Login System (Decorators)
#A web application wants to ensure that users are authenticated before accessing
#sensitive functions. Create a decorator that checks whether the user is logged in before allowing access to a function.


def login_required(function):
    def wrapper(is_logged_in):
        if is_logged_in:
            function()
        else:
            print("Please log in first")
    return wrapper


@login_required
def view_profile():
    print("Welcome to your profile")


view_profile(True)   # Logged in
view_profile(False)  # Not logged in
