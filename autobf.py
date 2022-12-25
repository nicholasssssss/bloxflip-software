import os, colorama, random, bloxflip, time, rainbowtext

Currency = bloxflip.Currency
token = open('authtoken.txt', 'r').read()



#colors
g = colorama.Fore.GREEN
w = colorama.Fore.WHITE
r = colorama.Fore.RED
y = colorama.Fore.YELLOW
b = colorama.Fore.BLUE

class autoplay:

    def automines():
        
            amount = int(input('amount of games: ')); bet_amount = int(input('bet amount: ')); mine_amount = int(input('mines: ')); auth_token = token
            #bet_amount : int = betamountinput; mine_amount : int = minesamountinput; auth_token : str = token.read()
            for i in range(amount):
                if bet_amount < 5:
                    print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}bet amount must be higher than 5!\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                try:
                    start_game = bloxflip.Mines.Create(betamount=bet_amount, mines=mine_amount, auth=token)
                    if start_game.status_code == 400:
                        print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}Failed to start game | {w}Bet amount prob higher than balance\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                        return 0 
                    bloxflip.Currency.Balance(auth=token)
                except Exception as e:
                    print("invalid auth token")
                    print(f'{r}{e}')
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
                            bloxflip.Mines.Choose(choice=int(a), auth=token)
                        except:
                            balance = Currency.Balance(auth=token)
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
                    bloxflip.Mines.Cashout(auth=token)
                    balance = Currency.Balance(auth=token)
                    print(f'''
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    {g}you won! |{w} balance: {balance}
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
                            ''')
                except:
                    balance = Currency.Balance(auth=token)
                    print(f'''
    🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
    {r}you lost! |{w} balance: {balance}
    🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                            ''')
                    
    def autotowers():
        repeat = int(input('amount of games: '))
        difficulty = str(input('difficulty (hard, easy): '))
        bet_amount = int(input('bet amount: '))
        click_amount = int(input('click amount: '))
        for i in range(repeat):
            if difficulty == 'easy'  or difficulty == 'hard':
                pass
            else:
                print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}invalid difficulty |{w} difficulty must be easy or hard\🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                return 0
            try:
                bloxflip.Login(a=token)
            except:
                print(f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}invalid auth token\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                return 0
            try:
                balance = int(bloxflip.Currency.Balance(auth=token))
                bloxflip.Towers.Create(betamount=bet_amount, difficulty=difficulty, auth=token)
                print(f'''
        🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
        {y}Attempting to click towers
        🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
                ''')
            except Exception as e:
                print(f"\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n{r}invalid auth token\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
                print(f'{r}{e}')
            try:
                count = 0
                for x in range(click_amount):
                    a = random.randint(0, 2)
                    bloxflip.Towers.Choose(choice=a, auth=token)
                    count += 1
            except:
                print(f"""
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
        {r}you lost! |{w} balance: {balance}
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                """)
            try:
                bloxflip.Towers.Cashout(auth=token)
                balance = int(bloxflip.Currency.Balance(auth=token))
                print(f"""
        🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
        {g}you won! |{w} balance: {balance}
        🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩            
                """)
            except:
                balance = int(bloxflip.Currency.Balance(auth=token))
                print(f"""
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
        {r}you lost! |{w} balance: {balance}
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
                """)
                            
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

ainput = int(input(f'''
//////////////////////////////////////////////////////////////////////////////////////
Mady by Geek#0001, Modified by static#4444, and sum from vipqix altough almost nothing, phish#7381 too

1. auto mines                             | 2. auto towers
3. mines cachout                          | 4. towers cachout
5. balance ckecker                        | 6. about tool
7. balance monitor                        | 8. token checker
9. crash monitor                          | 10. rain monitor
11. token changer                         | 12. exit

//////////////////////////////////////////////////////////////////////////////////////
----->
INPUT: {g}'''))
print(w)

if ainput == 1:
    autoplay.automines()

elif ainput == 2:
    autoplay.autotowers()

elif ainput == 3:
    try:
        bloxflip.Mines.Cashout(auth=token)
        print(f'{w}cashed out! balance: {g}{bloxflip.Currency.Balance(auth=token)}')
    except:
        print(f'no active game')

elif ainput == 4:
    try:
        bloxflip.Mines.Cashout(auth=token)
        print(f'{w}cashed out! balance: {g}{bloxflip.Currency.Balance(auth=token)}')
    except:
        print(f'no active game')

elif ainput == 5:
    balance = int(bloxflip.Currency.Balance(auth=token))
    print(f'{w}balance: {balance}')

elif ainput == 6:
    print(f'''


{rainbowtext.text('░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗  ████████╗██╗░░██╗██╗░██████╗')}
{rainbowtext.text('██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝  ╚══██╔══╝██║░░██║██║██╔════╝')}
{rainbowtext.text('███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░  ░░░██║░░░███████║██║╚█████╗░')}
{rainbowtext.text('██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░  ░░░██║░░░██╔══██║██║░╚═══██╗')}
{rainbowtext.text('██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░  ░░░██║░░░██║░░██║██║██████╔╝')}
{rainbowtext.text('╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░')}

{w}Me, {g}Vipqix{w}, have worked on this tool from soruces from {g}geek{w}, {g}static{w}.
i did all the work. jus kidding, i had developed aids from this, brain damage, and more
but this did take me a while to make, and i did learn a lot from this, so
expect more tools from me, and i hope you enjoy this tool, and i hope you
have a great day, and i hope you have a great life. - {g}Vipqix{w}

who made what?
----------------------------------
| auto mines - geek & static     |  
| auto towers - geek             |           
| mines cachout - vipqix         |         
| towers cachout - vipqix        |  ░░██╗██████╗░ ██╗░░░░░░█████╗░██╗░░░██╗███████╗  ██╗░░░██╗░█████╗░██╗░░░░░██╗░░░░░
| balance checker - vipqix       |  ░██╔╝╚════██╗ ██║░░░░░██╔══██╗██║░░░██║██╔════╝  ╚██╗░██╔╝██╔══██╗██║░░░░░██║░░░░░
| about tool - vipqix            |  █╔╝░░█████╔╝ ██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░  ░╚████╔╝░███████║██║░░░░░██║░░░░░
| balance monitor - vipqix       |  ╚██╗░░╚═══██╗ ██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░  ░░╚██╔╝░░██╔══██║██║░░░░░██║░░░░░
| token checker - vipqix         |  ░╚██╗██████╔╝ ███████╗╚█████╔╝░░╚██╔╝░░███████╗  ░░░██║░░░██║░░██║███████╗███████╗
| crash monitor - vipqix         |  ░░╚═╝╚═════╝░ ╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
| exit - vipqix                  |
----------------------------------      
    ''')

elif ainput == 7:
    os.system('cls'); counter = 0
    while True:
        balance = int(bloxflip.Currency.Balance(auth=token))
        print(f'{w}balance: {g}{balance}'); counter += 1; print(f'{w}times checked: {g}{counter}') 
        time.sleep(1)

elif ainput == 8:
    try:
        balance = int(bloxflip.Currency.Balance(auth=token))
        print(f'{w}token: {g}valid')
    except:
        print(f'{w}token: {r}invalid')

elif ainput == 9:
    autoplay.crashmonitor()

elif ainput == 10:
    exit()

elif ainput == 11:
    os.system('start authtoken.txt')

elif ainput == 12:
    exit()

else:
    print('invalid input')
