import discord
from discord.ext import commands

class ConnectFour:


    red = '\N{LARGE RED CIRCLE}'
    blue = '\N{LARGE BLUE CIRCLE}'
    blank = '\N{MEDIUM BLACK CIRCLE}'
    
    
    def __init__(self, bot):
        self.bot = bot
        
    def grid_maker(self):
        rows = 7
        cols = 7
        grid = []
        for i in range(rows):
            line = []
            for value in range(cols):
                line.append(blank)
            grid.append(line)
        return grid


    async def display_grid(self, ctx, grid):
        fmt = ''
        for i in reversed(grid):
            fmt += ' '+' '.join(i)+' \n'
        numbers = ' '
        for i in range(1,len(grid[0]+1)):
            numbers += str(i) + ' '
        fmt += '\n' + numbers
        await self.bot.send_message(ctx.message.channel, fmt)

    async def display_grid(self, ctx, grid):
        pass
        
        

    async def start_game(self, ctx, p1, p2):
        grid = self.grid_maker()
        await self.display_grid()
        cycles = int(len(grid)*len(grid[0])/2)
        
        
    @commands.command(pass_context=True)
    async def four_row(self, ctx, player: discord.Member):
        p1 = ctx.message.author
        p2 = player
        
        await self.start_game(ctx, p1, p2)
        
        
        

    
    
def setup(bot):
    bot.add_cog(ConnectFour(bot))


            
# player1 = await self.bot.wait_for_message(timeout=60, author=player1, check=move_check)


#     def player_one(grid,colour):
#         player1 = input("P1 Select a column: ")
#         while player1:
#             for i in range(len(grid)):
#                 if grid[i][int(player1)] == 'blank':
#                     grid[i][int(player1)] = colour
#                     coordinate = [i,int(player1)]
#                     returnvalue = [grid,coordinate]
#                     return returnvalue
#                 else:
#                     pass
#             print("Column Full! Try another Column")
#             player1 = input("Select a column: ")
#         print("Player 1 gives up!")
#         return False


#     def player_two(grid,colour):
#         player2 = input("P2 Select a column: ")
#         while player2 != '':
#             for i in range(len(grid)):
#                 if grid[i][int(player2)] == '\N{MEDIUM BLACK CIRCLE}':
#                     grid[i][int(player2)] = colour
#                     coordinate = [i,int(player2)]
#                     returnvalue = [grid,coordinate]
#                     return returnvalue
#                 else:
#                     pass
#             player2 = int(input("Select a column: "))
#             print("Column Full! Try another Column!")
#         print("Player 2 gives up!")
#         return False

            
#     def main():
#         colour1 = '\N{LARGE BLUE CIRCLE}'
#         colour2 = '\N{LARGE RED CIRCLE}'
#         grid = grid_maker()
#         cycles = int(len(grid)*len(grid[0])/2)
#         for i in range(cycles):
#             #PLAYER ONE
#             display_grid(grid)
#             values = player_one(grid,colour1)
#             if values == False:
#                 display_grid(grid)
#                 print("Player 2 Wins!")
#                 break
#             grid = values[0]
#             coordinate = values[1]
#             if win_condition(coordinate,grid,colour1) == True:
#                 display_grid(grid)
#                 print("Player 1 Wins!")
#                 break
#             #PLAYER TWO
#             display_grid(grid)
#             values = player_two(grid,colour2)
#             if values == False:
#                 display_grid(grid)
#                 print("Player 1 Wins!")
#                 break
#             grid = values[0]
#             coordinate = values[1]
#             if win_condition(coordinate,grid,colour2) == True:
#                 display_grid(grid)
#                 print("Player 2 Wins!")
#                 break
            
    

    
#     def win_condition(coordinate,grid,colour):
#         row_num = coordinate[0]
#         col_num = coordinate[1]
#         #HORIZONTAL CHECK
#         horizontal_counter = 0
#         horizontal_row = ''.join(grid[row_num])
#         for value in horizontal_row:
#             if value == colour:
#                 horizontal_counter += 1
#             else:
#                 horizontal_counter = 0
#             if horizontal_counter == 4:
#                 print(str(horizontal_counter)+" in a Row")
#                 return True
#         #VERTICAL CHECK
#         vertical_counter = 0
#         for i in range(row_num+1):
#             if grid[i][col_num] == colour:
#                 vertical_counter += 1
#             else:
#                 vertical_counter = 0
#             if vertical_counter == 4:
#                 print(str(vertical_counter)+" in a Column")
#                 return True
#         #DIAGONAL CHECK
#         diagonal_counter_one = 0
#         diagonal_counter_two = 0
#         for num in range(4):
#             try:
#                 if grid[row_num-num][col_num+num] == colour:
#                     diagonal_counter_one += 1
#             except:
#                 pass
#             try:
#                 if grid[row_num-num][col_num-num] == colour:
#                     diagonal_counter_two += 1
#             except:
#                 pass
#         if diagonal_counter_one == 4:
#             print(str(diagonal_counter_one)+" in a Diagonal")
#             return True
#         if diagonal_counter_two == 4:
#             print(str(diagonal_counter_two)+" in a Diagonal")
#             return True
#         #Return Statement
#         return False


# def move_check(message):
#     num = message.content
#     if num.isdigit():
#         if num > 7 or num < 1:
#             return False
#         else:
#             return True
#     else:
#         return False
    
