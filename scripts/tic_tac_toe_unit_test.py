import unittest
import tic_tac_toe

class Test_tic_tac_toe(unittest.TestCase):
    
    def test_check_game_logic(self):
        correctness_check_list = [[1,4,7],[3,4,5],[6,7,8],[2,5,8],[2,4,6],[0,1,2],[0,4,8],[0,3,6]]
        for each_logic in correctness_check_list:
            test_list = ['']*9
            for each_element in each_logic:
                test_list.insert(each_element,'X')
            #print(test_list)
            self.assertEqual(tic_tac_toe.check_game_logic(test_list),'1')


        game_end_check_list = ['X','0','X','X','0','X','0','X','0']
        self.assertEqual(tic_tac_toe.check_game_logic(game_end_check_list),'9')

    def test_game_end(self):
        # Comment out the following line on tic_tac_toe.py before running this test or 
        # catch it in try_catch block
        # print (f"{player_one} wins the game, {player_two} better luck next time")
        
        game_end_variables = ["1","2","9"]

        try:
            for variables in game_end_variables:
                self.assertEqual(tic_tac_toe.game_end(variables),False)
        except NameError:
            print("Player_names not defined")
        
        
        not_game_end_variables = ["3",7,"10","sfsdfssf"]
        for variables in not_game_end_variables:
            self.assertEqual(tic_tac_toe.game_end(variables),True)
        
if __name__=="__main__":
    unittest.main()

