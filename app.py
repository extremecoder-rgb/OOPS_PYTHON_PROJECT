class devbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Devbook !! How would you like to proceed?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have successfully signed up!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu.")
        else:
            uname = input("Enter your username here -> ")
            pwd = input("Enter your password here -> ")
            if uname == self.username and pwd == self.password:
                print("You have successfully signed in!")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again.")
        print("\n")
        self.menu()

    def post(self):
        if self.loggedin:
            content = input("Write your post here -> ")
            print(f"Your post: {content} has been published!")
        else:
            print("You need to sign in first to write a post.")
        print("\n")
        self.menu()


obj = devbook()