import os, colorama, random, bloxflip

Currency = bloxflip.Currency
token = open('authtoken.txt', 'r')
#colors
g = colorama.Fore.GREEN
w = colorama.Fore.WHITE
r = colorama.Fore.RED
y = colorama.Fore.YELLOW
b = colorama.Fore.BLUE

class autoplay:

    def automines():
        
            amount = int(input('amount of games: ')); bet_amount = int(input('bet amount: ')); mine_amount = int(input('mines: ')); auth_token = token.read()
            #bet_amount : int = betamountinput; mine_amount : int = minesamountinput; auth_token : str = token.read()
            for i in range(amount):
                if bet_amount < 5:
                    print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}bet amount must be higher than 5!\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                try:
                    start_game = bloxflip.Mines.Create(betamount=bet_amount, mines=mine_amount, auth=auth_token)
                    if start_game.status_code == 400:
                        print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}Failed to start game | {w}Bet amount prob higher than balance\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                        return 0 
                    bloxflip.Currency.Balance(auth=auth_token)
                except:
                    print("invalid auth token")
                    return 0
                times = range(mine_amount)
                print(f'''
    🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
    {y}Attempting to click mines
    🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
                ''')
                try:
                    for x in times:
                        try:
                            a = random.randint(0, 24)
                            bloxflip.Mines.Choose(choice=int(a), auth=auth_token)
                        except:
                            balance = Currency.Balance(auth=auth_token)
                            print(f'''
    🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
    {r}you lost! |{w} balance: {balance}
    🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                            ''')
                            return
                    
                except:
                    print(f"{r}failed to click mines")
                    return 0
                try:
                    bloxflip.Mines.Cashout(auth=auth_token)
                    balance = Currency.Balance(auth=auth_token)
                    print(f'''
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    {g}you won! |{w} balance: {balance}
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
                            ''')
                except:
                    balance = Currency.Balance(auth=auth_token)
                    print(f'''
    🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
    {r}you lost! |{w} balance: {balance}
    🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                            ''')

    def autotowers():
        repeat = int(input('amount of games: '))
        difficulty = str(input('difficulty (hard, normal, easy): '))
        bet_amount = int(input('bet amount: '))
        click_amount = int(input('click amount: '))
        auth_token = token.read()
        if difficulty == 'easy' or difficulty == 'normal' or difficulty == 'hard':
            pass
        else:
            print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}invalid difficulty |{w} difficulty must be easy, normal or hard\🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
            return 0
        try:
            bloxflip.Login(a=auth_token)
        except:
            print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}invalid auth token\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
            return 0
        for i in range(repeat):
            try:
                balance = int(bloxflip.Currency.Balance(auth=auth_token))
                bloxflip.Towers.Create(betamount=bet_amount, difficulty=difficulty, auth=auth_token)
                print(f'''
        🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
        {y}Attempting to click towers
        🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
                ''')
            except:
                print(f"\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}invalid auth token\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
            try:
                count = 0
                for x in range(click_amount):
                    a = random.randint(0, 2)
                    bloxflip.Towers.Choose(choice=a, auth=auth_token)
                    count += 1
            except:
                print(f"""
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
        {r}you lost! |{w} balance: {balance}
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                """)
            try:
                bloxflip.Towers.Cashout(auth=auth_token)
                balance = int(bloxflip.Currency.Balance(auth=auth_token))
                print(f"""
        🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
        {g}you won! |{w} balance: {balance}
        🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩            
                """)
            except:
                balance = int(bloxflip.Currency.Balance(auth=auth_token))
                print(f"""
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
        {r}you lost! |{w} balance: {balance}
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                """)
                return 0






os.system('cls')
print(f'''
{r                            }░█████╗░██╗░░░██╗████████╗░█████╗░  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
{colorama.Fore.YELLOW         }██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
{g                            }███████║██║░░░██║░░░██║░░░██║░░██║  ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
{   b                         }██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
{colorama.Fore.MAGENTA        }██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
{colorama.Fore.LIGHTMAGENTA_EX}╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
{colorama.Fore.RESET}
''')

ainput = int(input('''
//////////////////////////////////////////////////////////////////////////////////////
Mady by Geek#2526, Modified by static#4444, and sum from Vipqix#0001 altough almost nothing

1. auto mines                             | 2. auto towers
//////////////////////////////////////////////////////////////////////////////////////
'''))

if ainput == 1:
    autoplay.automines()
elif ainput == 2:
    autoplay.autotowers()
else:
    print('invalid input')
    ainput()
