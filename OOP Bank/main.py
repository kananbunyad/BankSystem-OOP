from user import User
from Bankapp.admin import Admin
from operate import Operate



if __name__ == '__main__':
    # Record the number of login failures of the administrator, if it reaches 3 times, it will end directly.
    count = 0
    # Create Administrator Objects
    admin = Admin()
    while True:
        # Display Welcome Page
        admin.welcome()
        # Login check
        ret = admin.login()
        if ret:
            # Does the record exit?
            is_quit = False
            # Load user information from a file first
            userinfo = User.load_user()
            # Create an Operational Object
            op = Operate(userinfo)
            while True:
                # Display operation menu
                admin.menu()
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
                    op.del_user()
                elif num == 3:
                    op.query_money()
                elif num == 4:
                    op.save_money()
                elif num == 5:
                    op.get_money()
                elif num == 6:
                    op.transfer_money()
                elif num == 7:
                    op.change_pwd()
                elif num == 8:
                    op.lock_user()
                elif num == 9:
                    op.unlock_user()
                elif num == 10:
                    op.show_users()
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