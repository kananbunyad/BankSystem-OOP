from userstaff import Userstaff
from accounting import Accounting
from useroperate import Useroperate



if __name__ == '__main__':
    # Record the number of login failures of the administrator, if it reaches 3 times, it will end directly.
    count = 0
    # Create Administrator Objects
    user = Userstaff("user","test")
    while True:
        # Display Welcome Page
        user.welcome()
        # Login check
        ret = user.login()
        if ret:
            # Does the record exit?
            is_quit = False
            # Load user information from a file first
            userinfo = Accounting.load_staffuser()
            # Create an Operational Object
            op = Useroperate(userinfo)
            while True:
                # Display operation menu
                user.menu()
                # Getting the user's action
                while True:
                    try:
                        num = int(input('Please select the operation:'))
                        break
                    except:
                        print("Your input is not integer, please try again")
                if num == 0:
                    print('Sign out')
                    is_quit = True
                    break
                elif num == 1:
                    op.new_user()
                elif num == 2:
                    op.resignation()
                elif num == 3:
                    op.display_staff()
                else:
                    print('The operation code is incorrect. Please re-enter it.')
            if is_quit:
                break
        else:
            print('Account or password error, login failure')
            count += 1
            if count >= 3:
                print('Errors have reached the upper limit and no login is allowed')
                break
    print('OVER')